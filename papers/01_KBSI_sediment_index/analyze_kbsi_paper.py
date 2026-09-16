"""Extract and analyze the KBSI paper.

The PDF contains the paper text and figures, but not the original sampling data.
This script therefore separates document-level analysis from optional numerical
recalculation using user-provided CSV files.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Iterable

import pandas as pd
from pypdf import PdfReader


SECTION_PATTERN = re.compile(
    r"(?m)^(?:\d+(?:\.\d+)*\.?\s+.+|Abstract|References|Conclusions?)\s*$"
)
CAPTION_PATTERN = re.compile(r"(?mi)^\s*(Figure|Fig\.?|Table)\s+\d+[^\n]*")
NUMBER_PATTERN = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?%?")
REQUIRED_SEDIMENT_COLUMNS = ["TAN", "AVS", "TOC", "Metals_TierII", "mud_fraction"]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def extract_pages(pdf_path: Path) -> list[str]:
    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        pages.append((page.extract_text() or "").replace("\x00", ""))
    return pages


def page_hash(text: str) -> str:
    return hashlib.sha256(normalize_text(text).encode("utf-8")).hexdigest()


def find_duplicate_pages(pages: list[str]) -> list[tuple[int, int]]:
    seen: dict[str, int] = {}
    duplicates = []
    for index, text in enumerate(pages, start=1):
        digest = page_hash(text)
        if digest in seen and len(normalize_text(text)) > 100:
            duplicates.append((seen[digest], index))
        else:
            seen[digest] = index
    return duplicates


def collect_captions(pages: Iterable[str]) -> list[str]:
    captions = []
    for page in pages:
        captions.extend(match.group(0).strip() for match in CAPTION_PATTERN.finditer(page))
    return list(dict.fromkeys(captions))


def collect_numbers(pages: Iterable[str]) -> list[str]:
    numbers = []
    for page in pages:
        numbers.extend(NUMBER_PATTERN.findall(page))
    return numbers


def calculate_pca(sediment_path: Path, output_dir: Path) -> str:
    """Calculate PC1 from a sediment CSV when the raw variables are available."""
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler

    data = pd.read_csv(sediment_path)
    missing = [column for column in REQUIRED_SEDIMENT_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(
            "Sediment CSV is missing columns: " + ", ".join(missing)
        )

    transformed = data[REQUIRED_SEDIMENT_COLUMNS].copy()
    for column in ["TAN", "AVS", "TOC", "Metals_TierII"]:
        if (transformed[column] < 0).any():
            raise ValueError(f"{column} contains negative values")
        transformed[column] = (transformed[column] + 1e-9).map(__import__("math").log)
    transformed["mud_fraction"] = transformed["mud_fraction"].clip(0, 1)
    transformed["mud_fraction"] = transformed["mud_fraction"].map(
        lambda value: __import__("math").asin(value**0.5)
    )

    scaled = StandardScaler().fit_transform(transformed)
    pca = PCA()
    scores = pca.fit_transform(scaled)
    result = data.copy()
    result["PC1"] = scores[:, 0]
    result.to_csv(output_dir / "pca_scores.csv", index=False)

    loadings = pd.DataFrame(
        {"variable": REQUIRED_SEDIMENT_COLUMNS, "PC1_loading": pca.components_[0]}
    )
    loadings.to_csv(output_dir / "pca_loadings.csv", index=False)
    explained = pca.explained_variance_ratio_ * 100
    return (
        f"PCA completed. PC1 explains {explained[0]:.2f}% of variance. "
        "See pca_scores.csv and pca_loadings.csv."
    )


def calculate_kbsi(
    taxon_path: Path, indicator_path: Path, output_dir: Path
) -> str:
    """Calculate KBSI from long-format taxon frequencies and indicator values."""
    taxon_data = pd.read_csv(taxon_path)
    indicator_data = pd.read_csv(indicator_path)
    required_taxon = {"sample_id", "taxon", "frequency"}
    required_indicator = {"taxon", "tolerance", "weight"}
    if not required_taxon.issubset(taxon_data.columns):
        raise ValueError("Taxon CSV needs sample_id, taxon, and frequency columns")
    if not required_indicator.issubset(indicator_data.columns):
        raise ValueError("Indicator CSV needs taxon, tolerance, and weight columns")

    merged = taxon_data.merge(indicator_data, on="taxon", how="inner")
    merged["weighted_tolerance"] = (
        merged["tolerance"] * merged["frequency"] * merged["weight"]
    )
    merged["weighted_denominator"] = merged["frequency"] * merged["weight"]
    grouped = merged.groupby("sample_id", as_index=False).agg(
        numerator=("weighted_tolerance", "sum"),
        denominator=("weighted_denominator", "sum"),
    )
    grouped["KBSI"] = (10 - grouped["numerator"] / grouped["denominator"]) * 10
    grouped["class"] = pd.cut(
        grouped["KBSI"],
        bins=[-float("inf"), 40, 50, 60, 70, float("inf")],
        labels=["E", "D", "C", "B", "A"],
        right=False,
    )
    grouped.to_csv(output_dir / "kbsi_scores.csv", index=False)
    return "KBSI completed. See kbsi_scores.csv."


def build_report(
    pdf_path: Path,
    pages: list[str],
    output_dir: Path,
    pca_result: str | None,
    kbsi_result: str | None,
) -> None:
    all_text = "\n\n".join(
        f"--- PDF page {index} ---\n{text}" for index, text in enumerate(pages, start=1)
    )
    (output_dir / "extracted_text.txt").write_text(all_text, encoding="utf-8")

    duplicates = find_duplicate_pages(pages)
    captions = collect_captions(pages)
    numbers = collect_numbers(pages)
    headings = list(dict.fromkeys(match.group(0).strip() for match in SECTION_PATTERN.finditer(all_text)))

    report = [
        "# KBSI PDF 자동 분석 보고서",
        "",
        f"- 원문: `{pdf_path.name}`",
        f"- PDF 페이지 수: {len(pages)}",
        f"- 추출 문자 수: {len(all_text):,}",
        "",
        "## 자동 점검 결과",
        "",
        "- PDF 텍스트 추출: 완료",
        f"- 중복으로 추정되는 페이지 쌍: {len(duplicates)}개",
        f"- Figure/Table 캡션: {len(captions)}개",
        f"- 숫자 토큰: {len(numbers):,}개",
        "",
        "### 중복 페이지",
        "",
    ]
    if duplicates:
        report.extend(f"- PDF {first}쪽과 PDF {second}쪽" for first, second in duplicates)
    else:
        report.append("- 동일한 텍스트의 중복 페이지를 찾지 못함")

    report.extend(["", "### 추출된 Figure/Table 캡션", ""])
    report.extend(f"- {caption}" for caption in captions)
    report.extend(["", "### 추출된 주요 제목", ""])
    report.extend(f"- {heading}" for heading in headings)
    report.extend(
        [
            "",
            "## 해석상 주의",
            "",
            "- 이 PDF에는 KBSI 개발에 사용한 원자료 CSV가 포함되어 있지 않으므로 PCA와 KBSI 재계산은 자동으로 수행하지 않음.",
            "- Figure의 생태학적 의미는 캡션과 추출 가능한 수치를 기반으로 하며, 이미지 자체의 시각적 판독은 별도 확인이 필요함.",
            "- PDF에 수정 표시본과 무표시본이 함께 있으면 동일한 논문이 중복될 수 있음.",
        ]
    )
    if pca_result:
        report.extend(["", "## PCA 재계산", "", f"- {pca_result}"])
    if kbsi_result:
        report.extend(["", "## KBSI 재계산", "", f"- {kbsi_result}"])

    (output_dir / "AUTOMATED_ANALYSIS_REPORT.md").write_text(
        "\n".join(report) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze the KBSI research PDF")
    parser.add_argument("pdf", type=Path, help="Path to the KBSI PDF")
    parser.add_argument(
        "--output-dir", type=Path, default=Path("kbsi_analysis_output"), help="Output directory"
    )
    parser.add_argument("--sediment-data", type=Path, help="Optional sediment CSV for PCA")
    parser.add_argument("--taxon-data", type=Path, help="Optional long-format taxon CSV for KBSI")
    parser.add_argument("--indicator-table", type=Path, help="Optional indicator CSV for KBSI")
    args = parser.parse_args()

    if not args.pdf.exists():
        raise FileNotFoundError(args.pdf)
    if (args.taxon_data is None) != (args.indicator_table is None):
        parser.error("--taxon-data and --indicator-table must be provided together")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pages = extract_pages(args.pdf)
    pca_result = None
    kbsi_result = None
    if args.sediment_data:
        pca_result = calculate_pca(args.sediment_data, args.output_dir)
    if args.taxon_data and args.indicator_table:
        kbsi_result = calculate_kbsi(args.taxon_data, args.indicator_table, args.output_dir)
    build_report(args.pdf, pages, args.output_dir, pca_result, kbsi_result)
    print(f"Analysis complete: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
