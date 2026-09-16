"""Simulate and calculate a KBSI-like analysis.

IMPORTANT: The generated data are synthetic demonstrations, not the paper's
observations. They must never be reported as field measurements.
"""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


TABLE_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([0-9.]+)\s*\|\s*(\d+)\s*\|$"
)
ENVIRONMENT_COLUMNS = ["TAN", "AVS", "TOC", "Metals_TierII", "mud_fraction"]


def load_indicator_table(path: Path) -> pd.DataFrame:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = TABLE_ROW.match(line.strip())
        if match:
            rows.append(
                {
                    "number": int(match.group(1)),
                    "taxon": match.group(2).strip(),
                    "tolerance": float(match.group(3)),
                    "weight": float(match.group(4)),
                }
            )
    indicators = pd.DataFrame(rows).drop_duplicates(subset=["number"])
    if len(indicators) != 137:
        raise ValueError(f"Expected 137 indicator taxa, found {len(indicators)}")
    return indicators


def sigmoid(values: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-np.clip(values, -30, 30)))


def generate_environment(n_samples: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    latent_stress = rng.normal(0, 1, n_samples)
    data = pd.DataFrame({"sample_id": [f"S{i:03d}" for i in range(1, n_samples + 1)]})

    # Positive loadings are intentional: higher latent stress should increase
    # all five synthetic sediment variables, as in the reported PC1 pattern.
    data["TAN"] = np.exp(0.2 + 0.70 * latent_stress + rng.normal(0, 0.35, n_samples))
    data["AVS"] = np.exp(-0.1 + 0.75 * latent_stress + rng.normal(0, 0.35, n_samples))
    data["TOC"] = np.exp(0.6 + 0.95 * latent_stress + rng.normal(0, 0.30, n_samples))
    data["Metals_TierII"] = np.exp(-0.2 + 0.90 * latent_stress + rng.normal(0, 0.35, n_samples))
    data["mud_fraction"] = np.clip(
        sigmoid(-0.1 + 0.80 * latent_stress + rng.normal(0, 0.45, n_samples)), 0.01, 0.99
    )
    data["synthetic_latent_stress"] = latent_stress
    return data


def calculate_pca(environment: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    transformed = environment[ENVIRONMENT_COLUMNS].copy()
    for column in ["TAN", "AVS", "TOC", "Metals_TierII"]:
        transformed[column] = np.log(transformed[column])
    transformed["mud_fraction"] = np.arcsin(np.sqrt(transformed["mud_fraction"]))

    scaled = StandardScaler().fit_transform(transformed)
    model = PCA()
    scores = model.fit_transform(scaled)
    pc1 = scores[:, 0]
    if np.corrcoef(pc1, environment["synthetic_latent_stress"])[0, 1] < 0:
        pc1 *= -1
        model.components_[0] *= -1

    scored = environment.copy()
    scored["PC1"] = pc1
    loadings = pd.DataFrame(
        {"variable": ENVIRONMENT_COLUMNS, "PC1_loading": model.components_[0]}
    )
    loadings["reported_loading_reference"] = [0.66, 0.69, 0.86, 0.82, 0.76]
    loadings["explained_variance_percent"] = model.explained_variance_ratio_[0] * 100
    return scored, loadings


def generate_taxa(
    environment: pd.DataFrame, indicators: pd.DataFrame, seed: int
) -> pd.DataFrame:
    rng = np.random.default_rng(seed + 1)
    rows = []
    stress = environment["PC1"].to_numpy()
    for sample_id, sample_stress in zip(environment["sample_id"], stress):
        for row in indicators.itertuples(index=False):
            threshold = (row.tolerance - 5.0) / 1.6
            probability = 0.02 + 0.62 * sigmoid(1.25 * (sample_stress - threshold))
            if rng.random() < probability:
                expected_frequency = 1.0 + 12.0 * probability
                frequency = max(1, int(rng.poisson(expected_frequency)))
                rows.append(
                    {
                        "sample_id": sample_id,
                        "taxon": row.taxon,
                        "frequency": frequency,
                    }
                )
    return pd.DataFrame(rows)


def calculate_kbsi(taxa: pd.DataFrame, indicators: pd.DataFrame) -> pd.DataFrame:
    merged = taxa.merge(indicators, on="taxon", how="inner")
    merged["numerator"] = merged["tolerance"] * merged["frequency"] * merged["weight"]
    merged["denominator"] = merged["frequency"] * merged["weight"]
    scores = merged.groupby("sample_id", as_index=False).agg(
        numerator=("numerator", "sum"), denominator=("denominator", "sum"), taxa=("taxon", "nunique")
    )
    scores["KBSI"] = (10 - scores["numerator"] / scores["denominator"]) * 10
    scores["condition_class"] = pd.cut(
        scores["KBSI"],
        bins=[-np.inf, 40, 50, 60, 70, np.inf],
        labels=["E", "D", "C", "B", "A"],
        right=False,
    )
    return scores


def write_outputs(
    output_dir: Path,
    environment: pd.DataFrame,
    loadings: pd.DataFrame,
    taxa: pd.DataFrame,
    scores: pd.DataFrame,
    indicators: pd.DataFrame,
    seed: int,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    environment.to_csv(output_dir / "synthetic_environment.csv", index=False)
    loadings.to_csv(output_dir / "synthetic_pca_loadings.csv", index=False)
    taxa.to_csv(output_dir / "synthetic_taxon_frequencies.csv", index=False)
    biological_data = (
        taxa.pivot_table(
            index="sample_id",
            columns="taxon",
            values="frequency",
            aggfunc="sum",
            fill_value=0,
        )
        .reset_index()
    )
    biological_data.to_csv(output_dir / "synthetic_biological_data.csv", index=False)
    scores.to_csv(output_dir / "synthetic_kbsi_scores.csv", index=False)
    indicators.to_csv(output_dir / "indicator_values_used.csv", index=False)

    correlations = environment[ENVIRONMENT_COLUMNS + ["PC1"]].corr(numeric_only=True)["PC1"]
    report = [
        "# Synthetic KBSI analysis",
        "",
        "> WARNING: Every observation in this folder is simulated. It is not the paper's field data and must not be reported as an empirical result.",
        "",
        f"- random seed: {seed}",
        f"- synthetic sample units: {len(environment)}",
        f"- indicator taxa used: {len(indicators)}",
        f"- samples with at least one detected synthetic taxon: {len(scores)}",
        "",
        "## PCA",
        "",
        f"- synthetic PC1 explained variance: {loadings['explained_variance_percent'].iloc[0]:.2f}%",
        "- PC1 correlations:",
    ]
    report.extend(f"  - {name}: {value:.3f}" for name, value in correlations.items())
    report.extend(
        [
            "",
            "## KBSI summary",
            "",
            f"- mean KBSI: {scores['KBSI'].mean():.2f}",
            f"- median KBSI: {scores['KBSI'].median():.2f}",
            f"- minimum KBSI: {scores['KBSI'].min():.2f}",
            f"- maximum KBSI: {scores['KBSI'].max():.2f}",
            "",
            "## Files",
            "",
            "- synthetic_environment.csv: simulated sediment variables and PC1",
            "- synthetic_pca_loadings.csv: PCA loadings and reported loading references",
            "- synthetic_taxon_frequencies.csv: simulated long-format taxon frequencies",
            "- synthetic_biological_data.csv: simulated sample-by-taxon abundance matrix",
            "- synthetic_kbsi_scores.csv: calculated KBSI and classes",
            "- indicator_values_used.csv: 137 indicator values parsed from Table 3",
        ]
    )
    (output_dir / "SYNTHETIC_ANALYSIS_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a synthetic KBSI demonstration")
    parser.add_argument("--indicator-table", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("synthetic_analysis_output"))
    parser.add_argument("--samples", type=int, default=320)
    parser.add_argument("--seed", type=int, default=20260916)
    args = parser.parse_args()

    indicators = load_indicator_table(args.indicator_table)
    environment = generate_environment(args.samples, args.seed)
    environment, loadings = calculate_pca(environment)
    taxa = generate_taxa(environment, indicators, args.seed)
    scores = calculate_kbsi(taxa, indicators)
    write_outputs(args.output_dir, environment, loadings, taxa, scores, indicators, args.seed)
    print(f"Synthetic analysis complete: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
