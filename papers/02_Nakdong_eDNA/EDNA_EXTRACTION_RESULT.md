# 퇴적물 eDNA 자료 추출 및 PDF·Excel 비교 결과

## 1. 분석 범위와 근거 표기

- 요청 기준: `EDNA_EXTRACTION_PROMPT.md`.
- PDF: `D:\퇴적물 과제\제출자료\퇴적물 최종보고서_최종(26.03.03).pdf`, 총 221쪽.
- Excel: `D:\퇴적물 과제\2. 새분석\eDNA\퇴적물 DNA, 하천 유형 추가_eDNA_다양도 지수 등.xlsx`, 2개 워크시트.
- PDF의 **파일 페이지**를 먼저 쓰고 괄호 안에 **인쇄된 본문 페이지**를 병기한다. 예: PDF 78쪽(본문 65쪽). 목차의 안내 쪽수보다 실제 본문 위치를 우선했다.
- Excel 주소는 `'Sheet1'!G2` 형식이다. 부록의 행별 주소와 열 머리글을 결합하면 개별 값의 셀을 찾을 수 있다.
- PDF 전체 텍스트와 Excel의 모든 시트·비어 있지 않은 셀·수식·저장 계산값·피벗테이블 구조를 조사했다. eDNA 실험방법, 관련 표 및 핵심 통계 그림은 렌더링한 페이지와 대조했다. 그림 32의 작은 분석 화면은 과정 예시로 확인했으며, 읽을 수 없는 축·수치를 실제 결과로 추정하지 않았다.
- **[추출 사실]**은 원본 기록, **[재계산]**은 첨부 셀에서 직접 계산한 값, **[해석]**은 분석자의 판단이다. 외부 문헌이나 웹 자료로 빈칸을 보충하지 않았다. 첨부 문서 속 계획·제안 문구는 자료의 내용으로 취급했다.

## 2. PDF에서 확인한 내용

### 2.1 연구 목적과 eDNA의 위치

**[추출 사실]** 퇴적물에 서식하는 저서성 대형무척추동물 중심의 건강성 평가 지수를 개발하고, DNA 분류 기술로 퇴적물 내 수생생물 다양성을 분석하는 것이 연구의 일부이다. 형태 동정이 어려운 실지렁이류·깔따구류의 분류 문제를 보완하기 위해 eDNA를 접목한다고 설명한다. 근거: PDF 6~7쪽(요약), 14~19쪽(본문 1~6쪽), 44~45쪽(31~32쪽), 47~50쪽(34~37쪽).

보고서의 두 생물지수는 구분해야 한다.

| 구분 | PDF에서 확인한 대상·규모 | 근거 |
|---|---|---|
| 현장 출현개체 기반 KBSI | 전체 출현 218분류군 중 지표 137분류군. 320표본단위 중 지표생물 미출현 11개를 제외한 309표본단위로 PC1 구간 분석 | 90쪽(77쪽), 104~105쪽(91~92쪽), 129~132쪽(116~119쪽) |
| eDNA 기반 e-KBSI | PC1을 기반으로 eDNA 지표분류군 277개의 내성치와 지표가중치를 제시 | 137~142쪽(124~129쪽), 표 37 |
| 연구성과 | 출현개체 기반 137분류군 외에 eDNA 기반 277분류군을 추가 발굴했다고 기술 | 146쪽(133쪽) |

**[해석]** 보고서에서 ‘종’이라고 부르더라도 속명 단독, `sp.`, `aff.` 및 상위 분류군 항목이 포함되므로, 277개를 모두 확정된 종 수준 동정으로 간주하지 않았다. 또한 218, 137, 277을 서로 합산해 총 종수로 해석할 수 없다.

### 2.2 조사지점·하천 유형·시기

**[추출 사실]** PDF 58~61쪽(45~48쪽), 표 14·16은 유역면적과 고도에 따른 유형 구분 및 조사계획을 제시한다.

| 유형 | 표 14의 명칭 | 유역면적·고도 표기 |
|---|---|---|
| Type 1 | Mountain streams | 유역면적 <250 km², 고도 >450 m |
| Type 2 | Highland small streams | <250 km², 150~450 m |
| Type 3 | Lowland small streams | <250 km², <150 m |
| Type 4 | Highland large streams | 250~4000 km², 150~450 m |
| Type 5 | Lowland large streams | 250~4000 km², <150 m |
| Type 6 | Rivers | 원문은 **<4000 km²**, 고도 ‘-’로 기재 |

Type 6의 부등호는 앞 유형과 겹치지만 원문대로 보존했다. 정확한 의도는 첨부 자료에서 확인되지 않음. 이 표의 괄호 안 숫자 714·231·51 등은 표에 실린 분류 규모이며, 본 과제 80개 조사지점의 실제 유형별 수와 혼동하면 안 된다.

표 16의 계획은 2022년 한강 20지점, 2023년 낙동강·금강 각 20지점, 2024년 영산강·섬진강 합계 20지점, 총 80지점이다. 유형별 계획은 하천 56, 호소 8, 산단하천 8, 도시관류 8지점이고 연 4회 조사이다. 계획의 Type I~VI와 Excel의 River·Lake·Industry·Urban·Reservoir는 같은 분류 수준이 아니다.

조사지점의 위치는 GPS로 기록하고, 모래 이하 세립질이 우세한 대표 퇴적구역을 선정했다고 기술한다. PDF 58~59쪽(45~46쪽).

| 연도 | 실제 조사시기 기록 | 근거 |
|---|---|---|
| 2022 | 과업 시작 지연으로 1차 6~7월, 2차 8월, 3차 8~9월, 4차 10~11월 | 64~65쪽(51~52쪽), 표 21 |
| 2023 | 1차 4월, 2차 5월, 3차 9월, 4차 10월 | 65~66쪽(52~53쪽), 표 22·23 및 이어진 표 |
| 2024 | 결과 도출을 앞당기기 위해 3~6월 조사. 지점별 1차 3월, 2차 4~5월, 3차 5월, 4차 6월 | 66~67쪽(53~54쪽), 표 24와 이어진 표 |

표 19·20 및 표 24의 제목과 실제 표 내용 사이에 편집상 불일치가 있어 4절에 별도로 기록했다. 같은 ‘1차~4차’를 모든 연도에서 동일한 계절로 치환하지 않았다. 위 날짜는 조사 일정이며, 개별 eDNA 추출·PCR·시퀀싱 날짜는 첨부 자료에서 확인되지 않음.

### 2.3 eDNA 시료 채취·추출·PCR·시퀀싱

**[추출 사실]** 아래는 PDF 77~79쪽(64~66쪽)의 직접적인 eDNA 방법이다. 일반 생물 코어 시료나 퇴적물 화학분석 시료의 깊이·양을 섞지 않았다.

| 단계 | 실제 기재 내용 | 근거 |
|---|---|---|
| 채취 위치·기질 | 생물 시료 조사지점 인근 15 cm 이내, 입자크기 2 mm 이하의 가는 흙 | 77쪽(64쪽) |
| 채취 깊이·용기·반복 | 퇴적심도 약 1 cm, 스파츌라 또는 약수저로 50 mL conical tube에 채취, 지점당 3시료 | 동일 |
| 오염 방지 | 지점별로 채취 도구를 구분하여 사용 | 동일 |
| 표기·보관 | 지점명·채집날짜·샘플 용도를 표기, 아이스박스와 드라이아이스로 냉동보관(-80°C)했다고 기술 | 78쪽(65쪽) |
| 표적 | 저서성 대형무척추동물, COI(Cytochrome c oxidase subunit I) | 동일 |
| 프라이머 | Forward mLCOIintF(Leray et al., 2013), Reverse jgHCO2198(Geller et al., 2013) | 동일 |
| DNA 추출 | 퇴적물 10 g + CTAB, lysis 후 chloroform과 isoamyl alcohol 이용 | 동일 |
| 저해물질 제거 | 부식산·페놀 등 PCR 저해요인을 PCR inhibitor removal kit(Zymo Research, USA)로 제거 | 동일 |
| 1차 PCR 확인 | 1.5% agarose gel 전기영동, Qubit 및 dsDNA HS assay kit로 농도 확인 | 동일 |
| 2차 PCR | Nextera XT index kit(Illumina, USA)로 target amplicon용 index 부착 단계 수행. 산물·농도는 1차와 같은 방식으로 확인 | 동일 |
| 정제 | AMPure XP Bead(Beckman Coulter, USA) 사용 | 동일 |
| 시퀀싱 | MiSeq(Illumina, USA) system, NGS | 동일 |
| 분석 | QIIME2 pipeline, NCBI nt database로 taxonomy assignment | 동일 |
| 분류 일치율 | 원문에 **‘≤ identity per 97%’**로 표기. 부등호를 임의로 반대로 고치지 않음 | 동일, 페이지 영상 대조 |
| 그림 32 | 현장채집 → eDNA library 제작 → MiSeq → QIIME2 pipeline의 사진·분석 화면 예시 | 79쪽(66쪽) |

**첨부 자료에서 확인되지 않음:** 프라이머 염기서열, PCR 반응 조성·온도·시간·cycle 수, 음성·양성 대조군 결과, 추출 blank, 시료별 DNA 수율과 순도, 시퀀싱 read 길이·깊이, paired-end 설정, Q-score 절단값, trimming·denoising·chimera 제거 설정, ASV 추론 도구, 희소화 깊이, 계통수, accession 번호, 지점당 3시료의 pooling 여부 및 Excel 행과의 대응표.

**[해석]** COI amplicon 시퀀싱과 분류할당 절차는 metabarcoding에 해당하는 분석 구성으로 읽힌다. 다만 보고서의 `metabarcoding` 명시 표기는 PDF 148~149쪽(135~136쪽)의 주암호·신갈저수지 플랑크톤 논문 성과 제목에도 나오므로, 그 논문 결과를 본 퇴적물 자료의 결과로 가져오지 않았다. 보관 온도는 보고서 기재값이며 실제 온도 기록은 없다.

### 2.4 하상 기질·수질·퇴적물 환경변수

**[추출 사실]** PDF 51~56쪽(38~43쪽)은 입도 및 TOC·공극수 암모니아·AVS·금속 분석법을 기술한다. 입도는 0.063 mm 표준체로 실트·점토를 구분하고, 2 mm 체로 모래·자갈을 구분한다. TOC는 원소분석법, 공극수 암모니아성 질소는 UV-Vis 630 nm, AVS는 산휘발성 황화물 분석, 총수은 및 As·Cd·Cr·Cu·Hg·Ni·Pb·Zn은 금속 분석법을 사용한다. 인증표준물질, 방법검출한계, 정량한계, 정밀도·정확도 등 정도관리 절차도 기재되어 있다. 이는 화학분석의 정도관리이며 eDNA의 음성대조군 확인을 대신하지 않는다.

PDF 67쪽(54쪽)은 같은 지점·시기에 수심(cm), 유속(Craig Method 또는 유속계), 수온·pH·전기전도도·용존산소(현장 YSI)를 조사했다고 기술한다.

PDF 83~85쪽(70~72쪽), 그림 36~40의 결과 서술은 다음과 같다.

- 공극수 암모니아: 오염 하천·산단 하천·농업용 저수지에서 높은 경향.
- AVS: 산단 하천에서 높은 경향.
- TOC: 하류·오염 하천·일부 산단 하천·농업용 저수지에서 높은 경향.
- 세립질 관련 서술: 하류·오염·산단 하천, 호소·농업용수에서 높은 경향. 본문은 ‘점토 비율’이라고도 표현한다.

**[해석]** `Mud`, `Fine substrate`, ‘세립질’, ‘점토’의 용어가 혼용되므로 모두를 동일한 점토 함량으로 단정하지 않았다. 수질 변수와 퇴적물 변수도 구분했다. Excel에는 이들 원측정값 대신 PC1만 있다.

### 2.5 환경변수 통계와 PCA

**[추출 사실]** PDF 86~89쪽(73~76쪽): NH3-N/TAN, AVS, TOC, Heavy metal Eq.는 자연로그 변환, 세립질 비율은 `ln[asin(sqrt(x))]` 변환을 기재한다. 표준점수로 계량화한 후 PCA를 수행한다. 변환 후 TAN·AVS의 K-S 검정 p는 각각 0.003, 0.002로 그림에 표시된다. 따라서 ‘변환 후 모두 정규성 검정을 통과했다’고 요약하지 않았다.

표 28(PDF 88쪽, 본문 75쪽; 앞의 빈모류 표 28과 번호 중복)의 환경변수 Pearson 상관계수:

| 변수쌍 | r | 원문 유의성 |
|---|---:|---|
| ln(TAN)–ln(AVS) | 0.48 | p<0.001 |
| ln(TAN)–ln(TOC) | 0.46 | p<0.001 |
| ln(TAN)–ln(Heavy metal Eq.) | 0.36 | p<0.001 |
| ln(TAN)–ln(Fine substrate) | 0.31 | p<0.001 |
| ln(AVS)–ln(TOC) | 0.45 | p<0.001 |
| ln(AVS)–ln(Heavy metal Eq.) | 0.44 | p<0.001 |
| ln(AVS)–ln(Fine substrate) | 0.32 | p<0.001 |
| ln(TOC)–ln(Heavy metal Eq.) | 0.66 | p<0.001 |
| ln(TOC)–ln(Fine substrate) | 0.64 | p<0.001 |
| ln(Heavy metal Eq.)–ln(Fine substrate) | 0.58 | p<0.001 |

표 29(PDF 89쪽, 본문 76쪽):

| 항목 | Axis 1 | Axis 2 | Axis 3 |
|---|---:|---:|---:|
| 고유값 | 2.9 | 0.9 | 0.5 |
| 설명분산(%) | 58.0 | 17.2 | 10.8 |
| 누적 설명분산(%) | 58.0 | 75.2 | 86.0 |
| ln(TAN) 상관계수 | -0.66** | 0.03** | 0.00** |
| ln(AVS) | -0.69** | -0.01** | -0.06** |
| ln(TOC) | -0.86** | 0.08** | -0.02** |
| ln(Heavy metal Eq.) | -0.82** | -0.01** | -0.03** |
| ln(Fine substrate) | -0.76** | -0.03** | 0.01 |

별표와 수치는 원문 그대로다. 그림 42의 PC1 방향과 표 29의 부호 불일치는 4절 참조. Excel PC1의 원변수·loading·점수 산식이 없으므로 PCA 재현은 불가능하다.

### 2.6 일반 저서동물 군집·다양도·환경 관계: eDNA 결과와 구분

**[추출 사실]** PDF 80쪽(67쪽)은 McNaughton 우점도(DI), Shannon 다양도(H′), Margalef 풍부도(R1), `Pilou` 균등도(J)를 사용했다고 명시한다. 원문의 `Pilou`는 해당 표기 그대로 기록했고, Excel의 지수를 이 정의와 자동으로 동일시하지 않았다.

PDF 100~103쪽(87~90쪽), 표 32·그림 46은 **현장 저서성 대형무척추동물**의 지점별 군집 결과이다. 보고된 평균±값은 DI 0.73±0.13, H′ 1.72±0.54, J 0.69±0.14, R1 1.49±0.59이다. 해당 문단만으로 ±가 표준편차인지 표준오차인지 확정하지 않았다. 높은 H′는 초강2 3.30, 함평천 2.70, 유등천5 2.66, 영동 2.61이며, 낮은 H′는 경천지1 0.46, C옥구천 0.71, 원평천2 0.83이다. 이 수치는 Excel의 eDNA 조사행 값과 집계 단위 및 측정 기반이 다르다.

표 33(PDF 105쪽, 92쪽)의 현장 지표종에서 Limnodrilus hoffmeisteri의 상대출현빈도는 73.8%, 개체수 점유율은 30.6%다. Excel에서 그 종이 우점종으로 기록된 행 비율과는 다른 지표이다.

표 34(PDF 109쪽, 96쪽)의 80지점 연평균 현장 군집지수와 환경변수 간 Pearson r:

| 환경변수 | 우점도 | 종다양도 | 종풍부도 | 종균등도 |
|---|---:|---:|---:|---:|
| ln(TAN) | 0.18 | -0.26* | -0.30** | -0.19 |
| ln(AVS) | 0.21 | -0.24* | -0.30** | -0.26* |
| ln(TOC) | 0.13 | -0.22 | -0.21 | -0.21 |
| ln(HM) | 0.10 | -0.15 | -0.15 | -0.15 |
| ln[asin(sqrt(Mud f))] | 0.16 | -0.24* | -0.25* | -0.19 |

본문 PDF 105~106쪽의 유의성 설명과 연결하면 *는 p<0.05, **는 p<0.01이다. 보고서는 전반적으로 관계가 약하거나 유의하지 않아 이 수리적 군집지수만으로 퇴적생태계 건강성 평가가 어렵다고 판단한다. 세립질의 단순한 기질, 유기물 흡착, 혐기화와 내성종 우점의 연결은 **보고서 저자의 해석**이다.

PDF 110~113쪽(97~100쪽), 그림 53~56은 빈모류·깔따구류의 군화 및 CCA 결과다. 빈모류는 TAN과 세립질 비율, 깔따구류는 세립질 비율과 AVS의 영향이 크다고 서술한다. TOC는 깔따구류, 중금속은 빈모류에서 상대적 영향이 작다고 한다. 해당 결과를 eDNA의 Bray-Curtis/UniFrac 분석으로 바꾸어 부르지 않았다. CCA의 permutation p값·축별 설명분산 및 군화 거리 정의는 해당 결과에서 확인되지 않는다.

PDF 114~128쪽(101~115쪽), 그림 57~71은 TAN·AVS·TOC·중금속·세립질 구배별 현장 지표종의 Weibull 누적확률분포이다. 예를 들어 TAN에 대해 동양하루살이는 민감한 편, 빈모류 일부는 넓은 내성 범위를 보이고, AVS에 대해 참실지렁이·실지렁이는 넓은 내성 범위를 보인다고 설명한다. 이는 eDNA 표 37의 계수와 동일한 결과가 아니다.

### 2.7 eDNA 지표종·e-KBSI 통계

**[추출 사실]** 표 37의 277개 항목은 부록 A에 모두 추출했다. 내성치 범위는 0.0~10.0, 지표가중치 범위는 1~5이다. 일부 예시는 다음과 같다.

| 분류군 | 내성치 t | 가중치 g | PDF(본문) |
|---|---:|---:|---|
| Amphichaeta | 0.0 | 5 | 137(124) |
| Cladotanytarsus vanderwulpi | 2.2 | 1 | 138(125) |
| Dicrotendipes nervosus | 3.3 | 1 | 139(126) |
| Limnodrilus hoffmeisteri | 4.8 | 1 | 140(127) |
| Tanytarsus formosanus | 4.2 | 1 | 141(128) |
| Tubifex tubifex | 5.6 | 1 | 142(129) |

그림을 직접 확인한 e-KBSI 구간의 수치는 다음과 같다.

| 위치 | 본문·그림에 표시된 수치 | 주의할 원문 차이 |
|---|---|---|
| 그림 78, PDF 142쪽(129쪽) | y=-6.18x+54.68, n=79, r=-0.80. 본문은 PC1과 e-KBSI의 극히 유의한 음의 관계라고 설명 | 그림 y축은 KBSI, 캡션은 e-KBSI. 그림에 숫자 p값은 없음 |
| 그림 79, PDF 143쪽(130쪽) | n=79, R²=0.82, p<0.001. 80지점 중 1지점 이상치 제외라는 본문 설명 | 본문·그림 식의 종속변수명은 KBSI, 산점도 축과 캡션은 e-KBSI |
| 그림 80, 같은 쪽 | x축 KBSI, y축 e-KBSI, n=79, r=0.75, p<0.001 | 본문은 ‘75% 설명력’ 및 ‘그림 31’, 캡션은 환경인자와 KBSI 변동계수 비교로 기재되어 실제 그림과 다름 |

그림 79의 표시 회귀식은 다음과 같다. 좌변 이름은 원문에서 KBSI로 되어 있다.

```text
KBSI = -0.43 ln(TAN, mg/L)
       -3.33 ln(AVS, μmol/gWW)
       -0.25 ln(TOC, %)
       -3.97 ln(Heavy metal Eq.)
       -4.58 ln[asin(sqrt(Mud f))]
       +38.80
```

표시 편상관계수는 TAN -0.11, AVS -0.39***, TOC -0.02, 중금속 -0.23*, Mud -0.42***이다. 보고서의 본문 나열 순서와 절댓값 크기 순서는 일치하지 않는다.

**[해석]** 그림 80의 r=0.75를 제곱하면 0.5625이므로, 단순 선형관계에서 약 56.25%에 해당한다. ‘75% 설명력’은 그림의 r 표기와 맞지 않는다. 어느 표시가 잘못되었는지는 원자료가 없으므로 확정할 수 없다. 그림 79의 R²=0.82와 그림 80의 r=0.75도 서로 다른 분석 결과다. 표 37의 t·g를 산출한 중간 데이터, e-KBSI 시료별 점수, 제외한 1지점의 이름은 첨부 자료에서 확인되지 않음.

PDF 148쪽(135쪽), 153~154쪽(140~141쪽)은 생물·퇴적환경·eDNA의 3종 DB 구축과 통합 활용, KBSI·e-KBSI의 병행 활용을 성과 및 활용계획으로 설명한다. **DB가 구축되었다는 서술과 해당 DB 전체가 이번 Excel에 포함되었다는 것은 다르다.**

## 3. Excel에서 확인한 내용

### 3.1 모든 시트와 표의 구조

| 시트 | 확인한 범위·객체 | 내용 |
|---|---|---|
| Sheet2 | 사용범위 A1:A76, 피벗테이블 `피벗 테이블1` A3:A76 | A3 ‘행 레이블’, A5:A75 우점종 71개 명칭, A76 ‘총합계’. 피벗 원본은 `'Sheet1'!K2:K321` |
| Sheet1 | A1:M321 | 13열, 조사행 320개 |
| Sheet1 | O2:O72 및 Q2:Q72 | 71개 우점종과 그 종이 우점한 조사행의 PC1 평균. 머리글 없음. P열은 빈 구분열 |

두 시트는 모두 visible이며 숨김 행·열, 병합셀, Excel Table 객체, 차트·삽입그림은 없다. Sheet2는 단순 종목록처럼 보이지만 실제 피벗테이블이다. A4는 빈칸이고 A76에 숫자 총합은 없다. Sheet1 N열도 빈 구분열이다.

| 열 | 머리글·범위 | 기록의 의미와 한계 |
|---|---|---|
| A | 차수, A2:A321 | 2022_1차~2024_4차. 날짜 자체는 없음 |
| B | 코드, B2:B321 | 지점 코드 |
| C | 지점명, C2:C321 | 원문 명칭 유지 |
| D | 수계, D2:D321 | Han, Geum, Nakdong, Yeongsan-Seomjin |
| E | 하천유형, E2:E321 | River, Industry, Lake, Urban, Reservoir |
| F | PC1, F2:F321 | 모든 행 숫자. 원변수·산식·loading 없음 |
| G | 다양도지수, G2:G321 | 241개 숫자, 79개 빈 셀 |
| H | 균등도지수, H2:H321 | 동일 |
| I | 풍부도지수, I2:I321 | 동일 |
| J | 우점도지수, J2:J321 | 동일 |
| K | 우점종, K2:K321 | 241개 명칭, 79개 빈 문자열 |
| L | 우점 분류군, L2:L321 | 241개 분류군, 79개 빈 문자열 |
| M | 우점종 ASV count, M2:M321 | 241개 정수, 79개 빈 문자열. 총 read 수·총 ASV 수와 다름 |

**[추출 사실]** G:J에는 지수명만 있고 Shannon·Simpson·Pielou·Margalef라는 영문 명칭, 정의·산식·로그 밑은 없다. 이 네 열은 Excel 수식이 아니라 저장된 숫자이다. 따라서 PDF 일반 군집지수 정의를 eDNA 지수에 그대로 적용했다고 확정할 수 없다. 특히 J열을 Simpson으로, I열을 관찰 종수 또는 ASV richness로 바꾸어 부르지 않았다.

**[재계산]** 80개 서로 다른 지점 코드에 각 4개 조사행이 있으며 `차수+코드` 중복은 없다. D열은 수계당 80행씩이다. 연도별 조사 지점이 달라 연도와 수계가 함께 변한다.

### 3.2 수식·피벗 검증

Q2의 수식은 `=AVERAGEIFS($F$2:$F$321,$K$2:$K$321,O2)`이며 Q72까지 같은 패턴으로 내려간다. 전체 수식은 71개이다. F열을 K열 우점종 조건으로 평균한 값과 저장 계산값을 독립적으로 대조했다. 검증 결과 및 71개 전체 값은 부록 B에 제시한다. 원본을 재계산하거나 수정하지 않았다.

**[해석]** Q열은 우점종이 나타난 행 전체의 PC1 평균도, ASV count로 가중한 평균도 아니다. 그 종이 **K열의 우점종으로 기록된 행**만 동일 가중으로 평균한다. PDF의 내성치 t 또는 지표가중치 g와 다른 통계량이므로 대응시켜 대체할 수 없다. Sheet2 역시 전체 검출분류군 목록이 아니라 K열의 우점종 목록이다.

### 3.3 누락과 실제 0값

**[재계산]** eDNA 값이 있는 행은 241/320(75.3125%), 비어 있는 행은 79/320(24.6875%)다. 79행 모두 G:J가 함께 비고 K:M도 빈 문자열이다. A:F는 전부 채워져 있다. 누락 원인이 추출 실패·PCR 실패·필터링·미검출 중 무엇인지, 생물이 없어서인지 여부는 **첨부 자료에서 확인되지 않음**.

`'Sheet1'!G204:I204`의 **0**은 누락이 아니다. J204는 1이고 우점종 및 count도 기록되어 있다. 누락을 0으로 대체하지 않았다. 79행의 정확한 주소와 전체 320행 값은 부록 C에 제시한다.

**[재계산]** 영산호2는 4차수 모두 eDNA 값이 비어 있다(`'Sheet1'!G258:M258`, `G278:M278`, `G298:M298`, `G318:M318`). 다른 79지점에는 적어도 1차수의 지수값이 있다. 이 지점이 PDF e-KBSI 분석에서 제외한 ‘이상치 1지점’과 같은 지점인지는 첨부 자료에서 확인되지 않음.

### 3.4 유형·차수·시료별 차이

유형별·차수별 표와 최소·최대 값은 부록 D에 직접 계산하여 제시한다. 계산은 빈칸을 제외한 산술평균이며 0은 포함한다. PC1은 320행, 네 지수는 241행을 사용한다. 유형별 PC1 평균과 지수 평균의 유효 표본수가 다름을 표시했다.

**[재계산]** 유형별 지수 평균은 Reservoir에서 다양도 1.5933·풍부도 2.4817로 가장 높고, Lake에서 다양도 1.0383·균등도 0.4218로 가장 낮다. Lake의 평균 우점도는 0.8181로 가장 높다. 다만 유형별 유효행 수는 16~165로 불균형하다.

**[해석]** 이것은 첨부 파일의 기술통계다. 유형 차이의 통계적 유의성이나 인과관계를 뜻하지 않는다. 같은 지점의 반복측정, 누락률 차이, 연도·수계 및 조사시기 차이가 함께 존재한다. 특히 Reservoir는 2024년 자료에만 있어 유형 효과와 연도·수계 효과를 분리해 단정할 수 없다. 이번 추출에서는 새로운 가설검정 p값을 만들지 않았다.

우점 분류군 기록은 깔따구류 94, 실지렁이류 83, 지렁이류 39, 이매패류 9, 복족류 4, 다모류 4, 하루살이류 3, 자포동물류 3, 각다귀류 1, 등에모기류 1행이다. 원문의 ‘지렁이류’와 ‘실지렁이류’를 임의 통합하지 않았다. 이 수는 각 분류군의 총 개체수나 총 검출 빈도가 아니라 **우점 기록 행수**다.

## 4. 두 파일의 공통점·차이점·불일치

| 항목 | 실제 비교 결과 | 해석·처리 |
|---|---|---|
| 조사 규모 | PDF 계획 80지점×4회, Excel 80코드×4회=320행 | 행 구조는 부합하나 eDNA 지수 79행 누락 |
| 생물군 | 실지렁이·깔따구 중심의 분류군이 양쪽에 존재 | Excel은 우점종만, PDF 표 37은 지표분류군 목록. 범위가 다름 |
| 지수 | PDF는 일반 군집 H′·J·R1·DI 정의와 e-KBSI를 구분, Excel은 네 일반명 지수만 있음 | 지수 산식·측정 기반 동일성을 확인할 수 없음 |
| PC1 | 양쪽 모두 PC1 사용 | Excel 점수 산식 및 환경원자료가 없어 PDF PCA와 수치 재현·일치 검증 불가 |
| 하천 유형 | PDF 계획: 하천 56·호소 8·산단 8·도시 8지점. Excel: River 53·Lake 9·Industry 7·Urban 6·Reservoir 5지점 | 계획과 실제 분류 및 Reservoir 추가를 구분. 일괄 재코딩하지 않음 |
| 지점별 유형 | PDF 97쪽(84쪽)에서는 풍영정천을 도시관류로 서술. Excel E245·E265·E285·E305는 River | 동일 지점의 유형 분류 불일치 |
| 표 19 제목/내용 | PDF 63쪽(50쪽) 표 19 제목은 2023 낙동강이나 내용은 영월1·달천5 등 한강 목록 | 페이지 영상으로 확인한 PDF 내부 편집 불일치 |
| 표 20 제목/내용 | 같은 쪽 표 20 제목은 2024 영산강·섬진강이나 내용은 내성천5·다사D 등 낙동강 목록 | Excel의 실제 영산강·섬진강 명단과 바로 대조하면 안 됨 |
| 일정 표 배치 | PDF 66쪽(53쪽) 표 24 제목 직후에 금강 지점·4~10월 일정이 나타나고, 실제 2024 지점·3~6월 일정은 67쪽에 나타남 | 제목만으로 연도·수계를 배정하지 않음 |
| PC1 부호 | PDF 89쪽 그림 42는 오른쪽 PC1 양의 방향으로 오염변수 화살표·Impaired를 표시. 같은 쪽 표 29는 5변수의 Axis 1 상관을 모두 음수로 표시 | PCA 축 부호를 바꿀 수 있다는 일반적 성질만으로 이 내부 불일치를 해결할 수 없음. 산출물 확인 필요 |
| e-KBSI 그림명 | 그림 78 y축 KBSI/캡션 e-KBSI, 그림 79 본문·회귀식 KBSI/축 e-KBSI | 원문 차이를 유지하고 어느 명칭이 맞는지 확정하지 않음 |
| 상관 vs 설명력 | 그림 80 r=0.75, 본문 ‘설명력 75%’ | r²는 0.5625. 그림 79의 R²=0.82와도 별개 |
| 그림 참조·캡션 | PDF 143쪽 본문 ‘그림 31’, 실제 도판 80. 캡션은 변동계수 비교, 실제는 KBSI vs e-KBSI | 잘못된 캡션을 결과 해석에 사용하지 않음 |
| 분류 일치율 | PDF 78쪽 ‘≤ identity per 97%’ | 원문 보존. 올바른 기준 방향은 확인 불가 |
| PDF 표 번호 | 빈모류 분류목록과 환경변수 상관표가 모두 표 28 | 페이지를 병기해 구별 |
| 277 vs 71 | PDF 표 37 277항목, Excel 우점종 71명칭 | 목록 목적이 달라 206항목이 단순 누락되었다고 할 수 없음 |

**[재계산]** Excel 71개 우점종 명칭 중 PDF 표 37과 **문자열이 정확히 같은 것은 61개**, 정확 일치하지 않는 것은 아래 10개이다. 두 목록을 강제 동의어 처리하지 않았다.

- Chironomidae sp. — PDF 표 37에는 Chironomidae sp.1, Chironominae sp.2가 있어 해상도·명칭 차이 가능성은 있으나 동일시하지 않음.
- Craspedacusta sowerbii, Fridericia peregrinabunda, Hippeutis cantori, Hippeutis sp., Hydra oligactis, Radix plicatula, Scapharca, Semisulcospira gottschei, Tipula sp.

각 명칭의 정확한 O열·Sheet2 주소 및 PDF 대응은 부록 B에 있다. ‘표 37과 불일치’는 PDF 전체에 그 이름이 전혀 없다는 뜻이 아니다. 표 37에는 Limnodrilus claparedeanus와 Limnodrilus claparedianus가 별도 행으로 실려 있어 원문 명칭을 그대로 유지했다.

## 5. 요청 항목별 확인 여부와 남은 데이터 공백

| 요청 항목 | 확인 결과 |
|---|---|
| eDNA·metabarcoding | PDF의 COI amplicon 실험방법·MiSeq·QIIME2·NCBI nt 확인. metabarcoding 명칭은 성과 논문 제목에도 등장 |
| 퇴적물 DNA·하상기질 | eDNA 채취 깊이·입경·용기·반복, 일반 입도 분석·세립질 환경 통계 확인 |
| 하천 유형 | PDF 계획·유역/고도 유형, Excel 5개 유형 확인. 같은 분류체계는 아님 |
| 수서곤충·생물군집 | PDF 현장 군집과 277개 eDNA 지표분류군, Excel 71개 우점종 확인 |
| Shannon | PDF 일반 군집 방법에 명시. Excel 다양도지수의 명칭 대응·산식은 첨부 자료에서 확인되지 않음 |
| Simpson | 해당 지수의 계산 결과·정의는 첨부 자료에서 확인되지 않음. 우점도지수를 Simpson으로 대체하지 않음 |
| Pielou | PDF 일반 군집 방법의 원문 표기 `Pilou` 균등도 J 확인. Excel 산식은 확인되지 않음 |
| richness | PDF Margalef R1, Excel 풍부도지수 존재. eDNA 관찰 종수·전체 ASV richness 원자료는 확인되지 않음 |
| Faith PD | 첨부 자료에서 확인되지 않음 |
| Bray-Curtis | 첨부 자료에서 확인되지 않음 |
| UniFrac | weighted/unweighted 모두 첨부 자료에서 확인되지 않음 |
| DNA 추출·PCR·시퀀싱 | 개요 확인. 상세 조건·QC 및 시료별 성공 여부는 확인되지 않음 |
| 수질·통계 | PDF 수질측정 방법·퇴적환경 통계·PCA·CCA·회귀 확인. Excel에 환경원자료 및 e-KBSI 점수 없음 |
| 유형·시료 차이 | Excel의 기술통계와 전체 조사행 추출. 유형별 검정·반복측정 모형 결과는 첨부 자료에서 확인되지 않음 |

**[해석]** 이 Excel만으로 원래의 다양도 지수, Bray-Curtis, UniFrac, Faith PD 또는 e-KBSI를 재산출할 수 없다. 필요한 전체 시료×분류군/ASV abundance 행렬, 지수 정의, 계통수 및 e-KBSI 적용 절차가 없기 때문이다. 79개 누락 원인, 지점당 3시료와 320행의 관계, PCA 부호·그림 명칭 오류를 확인하면 두 파일의 정합성을 더 명확히 판단할 수 있다.

---

## 부록 A. PDF 표 37의 eDNA 지표분류군 277개 전체

학명 철자·내성치·가중치를 원문대로 추출했다. 페이지는 파일 쪽수(본문 쪽수)이다. 종 수준으로 확정되지 않은 항목도 원문대로 포함했다.

| 번호 | 학명(원문) | 내성치 t | 지표가중치 g | PDF(본문) |
| --- | --- | --- | --- | --- |
| 1 | Ablabesmyia longistyla | 5.0 | 4 | 137(124) |
| 2 | Ablabesmyia monilis | 7.5 | 3 | 137(124) |
| 3 | Ablabesmyia prorasha | 2.0 | 1 | 137(124) |
| 4 | Ablabesmyia sp. | 0.0 | 4 | 137(124) |
| 5 | Acentrella sibirica | 0.0 | 5 | 137(124) |
| 6 | Aeolosoma | 6.4 | 2 | 137(124) |
| 7 | Aeolosoma sp. | 3.2 | 1 | 137(124) |
| 8 | Alboglossiphonia aff. | 0.0 | 5 | 137(124) |
| 9 | Allonais pectinata | 10.0 | 5 | 137(124) |
| 10 | Amphichaeta | 0.0 | 5 | 137(124) |
| 11 | Amphichaeta raptisae | 4.8 | 1 | 137(124) |
| 12 | Amphitrite ornata | 3.1 | 5 | 137(124) |
| 13 | Anodonta arcaeformis | 0.0 | 5 | 137(124) |
| 14 | Anodonta nuttalliana | 4.4 | 4 | 137(124) |
| 15 | Arcidae sp. | 3.9 | 4 | 137(124) |
| 16 | Aulodrilus pluriseta | 5.4 | 1 | 137(124) |
| 17 | Aulodrilus sp. | 6.5 | 5 | 137(124) |
| 18 | Barbronia arcana | 3.6 | 3 | 137(124) |
| 19 | Barbronia sp. | 10.0 | 4 | 137(124) |
| 20 | Barbronia weberi | 4.6 | 4 | 137(124) |
| 21 | Batracobdella algira | 3.1 | 5 | 137(124) |
| 22 | Benthalia carbonaria | 8.0 | 3 | 137(124) |
| 23 | Bothrioneurum vejdovskyanum | 6.5 | 1 | 137(124) |
| 24 | Branchiodrilus sp. | 4.8 | 1 | 137(124) |
| 25 | Branchiura sowerbyi | 5.8 | 2 | 137(124) |
| 26 | Branchiura sp. | 10.0 | 5 | 137(124) |
| 27 | Bryodrilus diverticulatus | 0.0 | 5 | 137(124) |
| 28 | Candona sp. | 2.8 | 4 | 137(124) |
| 29 | Capitella capitata | 4.7 | 3 | 137(124) |
| 30 | Capitella sp. | 0.0 | 3 | 137(124) |
| 31 | Capitella teleta | 10.0 | 4 | 137(124) |
| 32 | Ceratopogonidae sp. | 4.8 | 4 | 137(124) |
| 33 | Chaetogaster aff. | 6.8 | 1 | 137(124) |
| 34 | Chaetogaster diaphanus | 3.5 | 1 | 137(124) |
| 35 | Chaetogaster diastrophus | 4.6 | 1 | 137(124) |
| 36 | Chaetogaster sp. | 6.3 | 2 | 137(124) |
| 37 | Chaetonotus aff. | 2.5 | 1 | 137(124) |
| 38 | Chaetonotus gelidus | 6.5 | 5 | 137(124) |
| 39 | Chaetonotus sp. | 3.7 | 1 | 137(124) |
| 40 | Chironomidae sp.1 | 4.5 | 1 | 137(124) |
| 41 | Chironominae sp.2 | 6.2 | 1 | 137(124) |
| 42 | Chironomus | 5.8 | 2 | 137(124) |
| 43 | Chironomus circumdatus | 3.7 | 2 | 138(125) |
| 44 | Chironomus dorsalis | 7.2 | 3 | 138(125) |
| 45 | Chironomus entis | 5.1 | 3 | 138(125) |
| 46 | Chironomus flaviplumus | 3.6 | 1 | 138(125) |
| 47 | Chironomus incertipenis | 4.2 | 3 | 138(125) |
| 48 | Chironomus kiiensis | 3.4 | 2 | 138(125) |
| 49 | Chironomus nipponensis | 4.4 | 1 | 138(125) |
| 50 | Chironomus ramosus | 4.4 | 5 | 138(125) |
| 51 | Chironomus riparius | 4.7 | 3 | 138(125) |
| 52 | Chironomus sp. | 6.7 | 3 | 138(125) |
| 53 | Chironomus striatipennis | 5.0 | 1 | 138(125) |
| 54 | Chironomus yoshimatsui | 4.3 | 1 | 138(125) |
| 55 | Cirriformia sp. | 6.4 | 2 | 138(125) |
| 56 | Cladopelma | 10.0 | 5 | 138(125) |
| 57 | Cladopelma edwardsi | 4.7 | 2 | 138(125) |
| 58 | Cladopelma virescens | 5.3 | 5 | 138(125) |
| 59 | Cladotanytarsus | 1.8 | 2 | 138(125) |
| 60 | Cladotanytarsus paratridorsum | 1.8 | 2 | 138(125) |
| 61 | Cladotanytarsus vanderwulpi | 2.2 | 1 | 138(125) |
| 62 | Clitellata sp. | 4.2 | 5 | 138(125) |
| 63 | Conchapelopia sp. | 8.3 | 4 | 138(125) |
| 64 | Conchoecetta acuminata | 5.3 | 5 | 138(125) |
| 65 | Corbicula | 0.0 | 5 | 138(125) |
| 66 | Corbicula fluminea | 3.5 | 1 | 138(125) |
| 67 | Corbicula japonica | 1.8 | 5 | 138(125) |
| 68 | Corbicula leana | 3.8 | 2 | 138(125) |
| 69 | Corbicula sp. | 3.1 | 1 | 138(125) |
| 70 | Corophiidae sp. | 6.5 | 5 | 138(125) |
| 71 | Corynoneura lobata | 0.0 | 5 | 138(125) |
| 72 | Crassostrea talonata | 10.0 | 5 | 138(125) |
| 73 | Cricotopus | 5.2 | 4 | 138(125) |
| 74 | Cricotopus bicinctus | 4.7 | 1 | 138(125) |
| 75 | Cricotopus bimaculatus | 0.0 | 3 | 138(125) |
| 76 | Cricotopus metatibialis | 6.5 | 5 | 138(125) |
| 77 | Cricotopus sp. | 1.9 | 4 | 138(125) |
| 78 | Cricotopus sylvestris | 4.6 | 2 | 138(125) |
| 79 | Cricotopus triannulatus | 2.2 | 2 | 138(125) |
| 80 | Cricotopus tricinctus | 4.1 | 4 | 138(125) |
| 81 | Cricotopus trifasciatus | 4.3 | 1 | 138(125) |
| 82 | Culicoides arakawai | 5.8 | 2 | 138(125) |
| 83 | Culicoides morisitai | 2.7 | 2 | 138(125) |
| 84 | Culicoides sp. | 10.0 | 5 | 138(125) |
| 85 | Cyprididae | 3.1 | 5 | 138(125) |
| 86 | Cyprididae sp. | 5.1 | 2 | 138(125) |
| 87 | Cypridopsis | 5.7 | 3 | 138(125) |
| 88 | Cypridopsis sp. | 6.3 | 1 | 138(125) |
| 89 | Cypridopsis vidua | 5.2 | 1 | 138(125) |
| 90 | Dero borellii | 5.2 | 4 | 138(125) |
| 91 | Dero digitata | 5.3 | 2 | 138(125) |
| 92 | Dero dorsalis | 2.6 | 4 | 138(125) |
| 93 | Dero furcata | 5.7 | 1 | 138(125) |
| 94 | Dero obtusa | 5.4 | 1 | 138(125) |
| 95 | Dero sp. | 5.6 | 1 | 138(125) |
| 96 | Dicrotendipes | 0.8 | 3 | 139(126) |
| 97 | Dicrotendipes flexus | 0.0 | 5 | 139(126) |
| 98 | Dicrotendipes inouei | 10.0 | 5 | 139(126) |
| 99 | Dicrotendipes nervosus | 3.3 | 1 | 139(126) |
| 100 | Dicrotendipes pelochloris | 3.8 | 1 | 139(126) |
| 101 | Dicrotendipes septemmaculatus | 0.0 | 4 | 139(126) |
| 102 | Ecnomus tenellus | 4.4 | 1 | 139(126) |
| 103 | Einfeldia dissidens | 5.5 | 1 | 139(126) |
| 104 | Eisenia fetida | 0.0 | 5 | 139(126) |
| 105 | Eisenia sp. | 10.0 | 5 | 139(126) |
| 106 | Eiseniella neapolitana | 8.8 | 4 | 139(126) |
| 107 | Ephemera | 7.5 | 4 | 139(126) |
| 108 | Ephemera orientalis | 3.2 | 1 | 139(126) |
| 109 | Ephemera sachalinensis | 5.3 | 3 | 139(126) |
| 110 | Ephemera sp. | 0.0 | 5 | 139(126) |
| 111 | Ephoron shigae | 2.6 | 3 | 139(126) |
| 112 | Ephoron sp. | 1.8 | 5 | 139(126) |
| 113 | Erpobdella lineata | 6.5 | 5 | 139(126) |
| 114 | Erpobdella sp. | 4.2 | 5 | 139(126) |
| 115 | Eukiefferiella sp. | 4.9 | 3 | 139(126) |
| 116 | Eunice cariboea | 6.5 | 5 | 139(126) |
| 117 | Gammarus | 0.0 | 5 | 139(126) |
| 118 | Gammarus duebeni | 10.0 | 5 | 139(126) |
| 119 | Gammarus fossarum | 0.0 | 5 | 139(126) |
| 120 | Gammarus lacustris | 7.8 | 5 | 139(126) |
| 121 | Gammarus nekkensis | 3.8 | 3 | 139(126) |
| 122 | Gammarus qiani | 6.5 | 5 | 139(126) |
| 123 | Glyptotendipes | 7.8 | 5 | 139(126) |
| 124 | Glyptotendipes signatus | 4.2 | 5 | 139(126) |
| 125 | Glyptotendipes tokunagai | 6.2 | 2 | 139(126) |
| 126 | Grandidierella japonica | 2.4 | 4 | 139(126) |
| 127 | Haemonais waldvogeli | 5.3 | 5 | 139(126) |
| 128 | Harnischia japonica | 5.3 | 5 | 139(126) |
| 129 | Harnischia sp. | 0.0 | 3 | 139(126) |
| 130 | Hayesomyia tripunctata | 4.5 | 4 | 139(126) |
| 131 | Hediste atoka | 3.3 | 3 | 139(126) |
| 132 | Helobdella | 6.0 | 4 | 139(126) |
| 133 | Helobdella adiastola | 1.4 | 3 | 139(126) |
| 134 | Helobdella octatestisaca | 2.9 | 3 | 139(126) |
| 135 | Hemiclepsis kasmiana | 0.0 | 5 | 139(126) |
| 136 | Heterocypris incongruens | 5.3 | 5 | 139(126) |
| 137 | Heteromastus koreanus | 5.5 | 2 | 139(126) |
| 138 | Heteromastus sp. | 6.7 | 2 | 139(126) |
| 139 | Hydrobaenus conformis | 3.1 | 5 | 139(126) |
| 140 | Hydrobaenus kondoi | 4.7 | 1 | 139(126) |
| 141 | Ilyodrilus sp. | 7.8 | 5 | 139(126) |
| 142 | Ilyodrilus templetoni | 4.5 | 1 | 139(126) |
| 143 | Labiobaetis atrebatinus | 7.5 | 4 | 139(126) |
| 144 | Labiobaetis tricolor | 3.1 | 5 | 139(126) |
| 145 | Lanceolaria kihirai | 10.0 | 4 | 139(126) |
| 146 | Lanceolaria triformis | 7.8 | 5 | 139(126) |
| 147 | Limnodrilus claparedeanus | 5.0 | 1 | 139(126) |
| 148 | Limnodrilus claparedianus | 4.9 | 1 | 139(126) |
| 149 | Limnodrilus hoffmeisteri | 4.8 | 1 | 140(127) |
| 150 | Limnodrilus paraclaparedianus | 8.5 | 3 | 140(127) |
| 151 | Limnodrilus sp. | 4.9 | 1 | 140(127) |
| 152 | Limnoperna fortunei | 3.6 | 1 | 140(127) |
| 153 | Limnophyes | 0.0 | 5 | 140(127) |
| 154 | Limnophyes tamakitanaides | 10.0 | 5 | 140(127) |
| 155 | Lineidae sp. | 3.1 | 5 | 140(127) |
| 156 | Lipiniella fujiprimus | 4.2 | 5 | 140(127) |
| 157 | Lipiniella moderata | 4.6 | 2 | 140(127) |
| 158 | Lumbriculus variegatus | 6.0 | 1 | 140(127) |
| 159 | Marionina seminuda | 6.5 | 5 | 140(127) |
| 160 | Marionina sp. | 1.2 | 4 | 140(127) |
| 161 | Metaphire hilgendorfi | 6.5 | 5 | 140(127) |
| 162 | Metaphire sp. | 10.0 | 5 | 140(127) |
| 163 | Microchironomus | 4.6 | 4 | 140(127) |
| 164 | Microchironomus tener | 3.3 | 2 | 140(127) |
| 165 | Moerella iridescens | 8.3 | 4 | 140(127) |
| 166 | Monodiamesa bathyphila | 2.0 | 4 | 140(127) |
| 167 | Monopylephorus | 7.8 | 5 | 140(127) |
| 168 | Monopylephorus rubroniveus | 8.0 | 3 | 140(127) |
| 169 | Mytilus galloprovincialis | 3.6 | 2 | 140(127) |
| 170 | Mytilus sp. | 2.0 | 4 | 140(127) |
| 171 | Nais bretscheri | 3.9 | 1 | 140(127) |
| 172 | Nais christinae | 5.6 | 2 | 140(127) |
| 173 | Nais communis | 6.4 | 2 | 140(127) |
| 174 | Nais elinguis | 6.2 | 1 | 140(127) |
| 175 | Nais simplex | 6.1 | 1 | 140(127) |
| 176 | Nais sp. | 4.9 | 1 | 140(127) |
| 177 | Nais stolci | 5.4 | 1 | 140(127) |
| 178 | Nais variabilis | 5.7 | 3 | 140(127) |
| 179 | Nanocladius | 1.6 | 3 | 140(127) |
| 180 | Nanocladius tamabicolor | 4.4 | 2 | 140(127) |
| 181 | Neanthes japonica | 10.0 | 5 | 140(127) |
| 182 | Odontosyllis detecta | 0.0 | 5 | 140(127) |
| 183 | Ophidonais serpentina | 7.8 | 5 | 140(127) |
| 184 | Ormosia meigenii | 0.0 | 5 | 140(127) |
| 185 | Orthocladius glabripennis | 7.1 | 2 | 140(127) |
| 186 | Orthocladius sp. | 5.8 | 2 | 140(127) |
| 187 | Parachironomus arcuatus | 3.9 | 2 | 140(127) |
| 188 | Paracladopelma camptolabis | 7.8 | 5 | 140(127) |
| 189 | Parakiefferiella bathophila | 3.7 | 3 | 140(127) |
| 190 | Paraleptophlebia | 1.5 | 3 | 140(127) |
| 191 | Paraleptophlebia japonica | 0.9 | 2 | 140(127) |
| 192 | Parametriocnemus stylatus | 5.8 | 4 | 140(127) |
| 193 | Paranais frici | 5.3 | 1 | 140(127) |
| 194 | Paranais litoralis | 10.0 | 4 | 140(127) |
| 195 | Paratanytarsus grimmii | 4.2 | 1 | 140(127) |
| 196 | Paratanytarsus inopertus | 5.4 | 3 | 140(127) |
| 197 | Paratendipes albimanus | 3.2 | 1 | 140(127) |
| 198 | Paratrichocladius rufiventris | 3.1 | 5 | 140(127) |
| 199 | Paratrichocladius tamaater | 1.4 | 2 | 140(127) |
| 200 | Phaenopsectra flavipes | 2.7 | 3 | 140(127) |
| 201 | Pisidium subtruncatum | 5.3 | 5 | 140(127) |
| 202 | Polypedilum asakawaense | 4.1 | 1 | 141(128) |
| 203 | Polypedilum bingoparadoxum | 0.0 | 5 | 141(128) |
| 204 | Polypedilum cf. | 0.0 | 3 | 141(128) |
| 205 | Polypedilum crassistyla | 8.8 | 4 | 141(128) |
| 206 | Polypedilum cultellatum | 2.5 | 1 | 141(128) |
| 207 | Polypedilum genpeiense | 3.5 | 2 | 141(128) |
| 208 | Polypedilum japonicum | 2.5 | 1 | 141(128) |
| 209 | Polypedilum masudai | 5.0 | 1 | 141(128) |
| 210 | Polypedilum nubeculosum | 4.1 | 1 | 141(128) |
| 211 | Polypedilum nubifer | 4.1 | 2 | 141(128) |
| 212 | Polypedilum prominens | 0.0 | 5 | 141(128) |
| 213 | Polypedilum scalaenum | 5.4 | 1 | 141(128) |
| 214 | Polypedilum sordens | 2.8 | 3 | 141(128) |
| 215 | Polypedilum sp. | 6.8 | 2 | 141(128) |
| 216 | Polypedilum surugense | 2.2 | 3 | 141(128) |
| 217 | Polypedilum unifascium | 0.0 | 5 | 141(128) |
| 218 | Polypedilum yongsanensis | 6.5 | 5 | 141(128) |
| 219 | Potamanthus luteus | 0.0 | 5 | 141(128) |
| 220 | Pristina aequiseta | 4.2 | 1 | 141(128) |
| 221 | Pristina leidyi | 6.6 | 2 | 141(128) |
| 222 | Pristina longiseta | 0.0 | 4 | 141(128) |
| 223 | Pristina osborni | 3.8 | 1 | 141(128) |
| 224 | Pristina sp. | 5.2 | 2 | 141(128) |
| 225 | Procladius choreus | 1.7 | 2 | 141(128) |
| 226 | Procladius culiciformis | 6.1 | 2 | 141(128) |
| 227 | Procladius sp. | 3.9 | 1 | 141(128) |
| 228 | Procloeon pennulatum | 3.3 | 4 | 141(128) |
| 229 | Procloeon sp. | 5.3 | 2 | 141(128) |
| 230 | Prostoma cf. | 7.8 | 5 | 141(128) |
| 231 | Psectrocladius aquatronus | 7.8 | 2 | 141(128) |
| 232 | Rheopelopia joganflava | 0.7 | 3 | 141(128) |
| 233 | Rheotanytarsus aestuarius | 0.5 | 3 | 141(128) |
| 234 | Rheotanytarsus sp. | 6.3 | 3 | 141(128) |
| 235 | Rhoenanthus coreanus | 0.0 | 5 | 141(128) |
| 236 | Scatella sp. | 1.2 | 4 | 141(128) |
| 237 | Scatella tenuicosta | 4.5 | 2 | 141(128) |
| 238 | Sigambra sp. | 5.9 | 3 | 141(128) |
| 239 | Sphaerium striatinum | 4.2 | 5 | 141(128) |
| 240 | Stempellinella | 2.8 | 4 | 141(128) |
| 241 | Stempellinella coronata | 2.7 | 3 | 141(128) |
| 242 | Stenocypris | 0.0 | 5 | 141(128) |
| 243 | Stenocypris hislopi | 0.0 | 5 | 141(128) |
| 244 | Stenocypris sp. | 7.5 | 4 | 141(128) |
| 245 | Sternaspis sp. | 4.2 | 5 | 141(128) |
| 246 | Stictochironomus sinsauensis | 3.2 | 1 | 141(128) |
| 247 | Stylaria fossularis | 3.2 | 3 | 141(128) |
| 248 | Tanypus chinensis | 6.9 | 2 | 141(128) |
| 249 | Tanypus kraatzi | 4.6 | 4 | 141(128) |
| 250 | Tanypus punctipennis | 0.9 | 3 | 141(128) |
| 251 | Tanypus sp. | 0.0 | 5 | 141(128) |
| 252 | Tanytarsus ahyoni | 3.9 | 1 | 141(128) |
| 253 | Tanytarsus dibranchius | 6.5 | 5 | 141(128) |
| 254 | Tanytarsus formosanus | 4.2 | 1 | 141(128) |
| 255 | Tanytarsus kiseogi | 6.1 | 2 | 142(129) |
| 256 | Tanytarsus okuboi | 4.7 | 1 | 142(129) |
| 257 | Tanytarsus oscillans | 2.6 | 1 | 142(129) |
| 258 | Tanytarsus oyamai | 4.2 | 5 | 142(129) |
| 259 | Tanytarsus simantoteuus | 0.0 | 5 | 142(129) |
| 260 | Tanytarsus sp. | 3.7 | 1 | 142(129) |
| 261 | Tanytarsus takahashii | 5.8 | 2 | 142(129) |
| 262 | Tanytarsus tamagotoi | 5.6 | 1 | 142(129) |
| 263 | Tanytarsus tamakutibasi | 3.7 | 2 | 142(129) |
| 264 | Tanytarsus tamaoctavus | 3.7 | 2 | 142(129) |
| 265 | Tanytarsus tamaundecimus | 4.6 | 1 | 142(129) |
| 266 | Tanytarsus tongmuensis | 0.0 | 5 | 142(129) |
| 267 | Tanytarsus unagiseptimus | 4.6 | 1 | 142(129) |
| 268 | Tanytarsus yunosecundus | 4.1 | 1 | 142(129) |
| 269 | Thienemanniella | 4.2 | 5 | 142(129) |
| 270 | Thienemanniella flaviscutella | 0.0 | 5 | 142(129) |
| 271 | Thienemanniella majuscula | 4.2 | 5 | 142(129) |
| 272 | Tubifex montanus | 7.8 | 5 | 142(129) |
| 273 | Tubifex sp. | 6.7 | 3 | 142(129) |
| 274 | Tubifex tubifex | 5.6 | 1 | 142(129) |
| 275 | Tubificinae sp. | 5.5 | 2 | 142(129) |
| 276 | Tvetenia sp. | 4.2 | 5 | 142(129) |
| 277 | Tvetenia tamaflava | 0.0 | 5 | 142(129) |

## 부록 B. Excel 우점종 71개, PC1 평균 및 PDF 표 37 대응

Sheet2의 A5:A75는 Sheet1 O2:O72와 같은 순서의 71개 명칭이다. ‘우점 행수’는 K2:K321에서 같은 명칭이 우점종인 행수다. PC1 평균은 Q열에 저장된 계산값이며 소수 15자리 유효숫자로 표시했다. 표 37 대응은 정확 문자열 일치 기준이다.

| 우점종 | 피벗 셀 | 명칭 / 평균 셀 | 우점 행수 | 평균 PC1 | PDF 표 37 |
| --- | --- | --- | --- | --- | --- |
| Amphichaeta | 'Sheet2'!A5 | 'Sheet1'!O2 / Q2 | 1 | -2.89466 | 번호 10, t=0.0, g=5, PDF 137쪽 |
| Amphichaeta raptisae | 'Sheet2'!A6 | 'Sheet1'!O3 / Q3 | 4 | -0.753335 | 번호 11, t=4.8, g=1, PDF 137쪽 |
| Aulodrilus pluriseta | 'Sheet2'!A7 | 'Sheet1'!O4 / Q4 | 3 | 0.658933333333333 | 번호 16, t=5.4, g=1, PDF 137쪽 |
| Bothrioneurum vejdovskyanum | 'Sheet2'!A8 | 'Sheet1'!O5 / Q5 | 8 | 1.28667875 | 번호 23, t=6.5, g=1, PDF 137쪽 |
| Branchiodrilus sp. | 'Sheet2'!A9 | 'Sheet1'!O6 / Q6 | 1 | 2.90417 | 번호 24, t=4.8, g=1, PDF 137쪽 |
| Branchiura sowerbyi | 'Sheet2'!A10 | 'Sheet1'!O7 / Q7 | 2 | 0.04077 | 번호 25, t=5.8, g=2, PDF 137쪽 |
| Chaetogaster aff. | 'Sheet2'!A11 | 'Sheet1'!O8 / Q8 | 3 | 2.32819 | 번호 33, t=6.8, g=1, PDF 137쪽 |
| Chaetogaster diaphanus | 'Sheet2'!A12 | 'Sheet1'!O9 / Q9 | 1 | -0.30236 | 번호 34, t=3.5, g=1, PDF 137쪽 |
| Chaetogaster sp. | 'Sheet2'!A13 | 'Sheet1'!O10 / Q10 | 1 | 2.47455 | 번호 36, t=6.3, g=2, PDF 137쪽 |
| Chironomidae sp. | 'Sheet2'!A14 | 'Sheet1'!O11 / Q11 | 5 | -1.215318 | 표 37 정확 일치 없음 |
| Chironomus circumdatus | 'Sheet2'!A15 | 'Sheet1'!O12 / Q12 | 1 | 0.07605 | 번호 43, t=3.7, g=2, PDF 138쪽 |
| Chironomus flaviplumus | 'Sheet2'!A16 | 'Sheet1'!O13 / Q13 | 2 | -1.102555 | 번호 46, t=3.6, g=1, PDF 138쪽 |
| Cladopelma edwardsi | 'Sheet2'!A17 | 'Sheet1'!O14 / Q14 | 1 | 1.89837 | 번호 57, t=4.7, g=2, PDF 138쪽 |
| Cladotanytarsus | 'Sheet2'!A18 | 'Sheet1'!O15 / Q15 | 2 | -2.351 | 번호 59, t=1.8, g=2, PDF 138쪽 |
| Cladotanytarsus vanderwulpi | 'Sheet2'!A19 | 'Sheet1'!O16 / Q16 | 11 | -1.83365909090909 | 번호 61, t=2.2, g=1, PDF 138쪽 |
| Corbicula fluminea | 'Sheet2'!A20 | 'Sheet1'!O17 / Q17 | 1 | -2.09713 | 번호 66, t=3.5, g=1, PDF 138쪽 |
| Corbicula leana | 'Sheet2'!A21 | 'Sheet1'!O18 / Q18 | 1 | -3.43287 | 번호 68, t=3.8, g=2, PDF 138쪽 |
| Corbicula sp. | 'Sheet2'!A22 | 'Sheet1'!O19 / Q19 | 5 | -0.715936 | 번호 69, t=3.1, g=1, PDF 138쪽 |
| Craspedacusta sowerbii | 'Sheet2'!A23 | 'Sheet1'!O20 / Q20 | 2 | 0.265685 | 표 37 정확 일치 없음 |
| Culicoides arakawai | 'Sheet2'!A24 | 'Sheet1'!O21 / Q21 | 1 | 1.3703 | 번호 82, t=5.8, g=2, PDF 138쪽 |
| Dero furcata | 'Sheet2'!A25 | 'Sheet1'!O22 / Q22 | 4 | -1.683005 | 번호 93, t=5.7, g=1, PDF 138쪽 |
| Dero sp. | 'Sheet2'!A26 | 'Sheet1'!O23 / Q23 | 1 | 3.69974 | 번호 95, t=5.6, g=1, PDF 138쪽 |
| Dicrotendipes nervosus | 'Sheet2'!A27 | 'Sheet1'!O24 / Q24 | 11 | -0.104594545454545 | 번호 99, t=3.3, g=1, PDF 139쪽 |
| Dicrotendipes pelochloris | 'Sheet2'!A28 | 'Sheet1'!O25 / Q25 | 1 | -1.50209 | 번호 100, t=3.8, g=1, PDF 139쪽 |
| Einfeldia dissidens | 'Sheet2'!A29 | 'Sheet1'!O26 / Q26 | 4 | 0.92223 | 번호 103, t=5.5, g=1, PDF 139쪽 |
| Ephoron shigae | 'Sheet2'!A30 | 'Sheet1'!O27 / Q27 | 2 | -0.377525 | 번호 111, t=2.6, g=3, PDF 139쪽 |
| Fridericia peregrinabunda | 'Sheet2'!A31 | 'Sheet1'!O28 / Q28 | 1 | -1.62368 | 표 37 정확 일치 없음 |
| Glyptotendipes tokunagai | 'Sheet2'!A32 | 'Sheet1'!O29 / Q29 | 3 | 0.914093333333333 | 번호 125, t=6.2, g=2, PDF 139쪽 |
| Heteromastus koreanus | 'Sheet2'!A33 | 'Sheet1'!O30 / Q30 | 2 | 0.18198 | 번호 137, t=5.5, g=2, PDF 139쪽 |
| Heteromastus sp. | 'Sheet2'!A34 | 'Sheet1'!O31 / Q31 | 2 | 0.911295 | 번호 138, t=6.7, g=2, PDF 139쪽 |
| Hippeutis cantori | 'Sheet2'!A35 | 'Sheet1'!O32 / Q32 | 1 | 1.06943 | 표 37 정확 일치 없음 |
| Hippeutis sp. | 'Sheet2'!A36 | 'Sheet1'!O33 / Q33 | 1 | -2.0919 | 표 37 정확 일치 없음 |
| Hydra oligactis | 'Sheet2'!A37 | 'Sheet1'!O34 / Q34 | 1 | -0.99598 | 표 37 정확 일치 없음 |
| Ilyodrilus sp. | 'Sheet2'!A38 | 'Sheet1'!O35 / Q35 | 1 | 1.5517 | 번호 141, t=7.8, g=5, PDF 139쪽 |
| Ilyodrilus templetoni | 'Sheet2'!A39 | 'Sheet1'!O36 / Q36 | 1 | -1.89918 | 번호 142, t=4.5, g=1, PDF 139쪽 |
| Limnodrilus claparedeanus | 'Sheet2'!A40 | 'Sheet1'!O37 / Q37 | 2 | 0.150305 | 번호 147, t=5.0, g=1, PDF 139쪽 |
| Limnodrilus hoffmeisteri | 'Sheet2'!A41 | 'Sheet1'!O38 / Q38 | 44 | -0.1566125 | 번호 149, t=4.8, g=1, PDF 140쪽 |
| Limnodrilus sp. | 'Sheet2'!A42 | 'Sheet1'!O39 / Q39 | 9 | 0.784881111111111 | 번호 151, t=4.9, g=1, PDF 140쪽 |
| Limnoperna fortunei | 'Sheet2'!A43 | 'Sheet1'!O40 / Q40 | 1 | -1.2137 | 번호 152, t=3.6, g=1, PDF 140쪽 |
| Lumbriculus variegatus | 'Sheet2'!A44 | 'Sheet1'!O41 / Q41 | 2 | 1.03546 | 번호 158, t=6.0, g=1, PDF 140쪽 |
| Monopylephorus rubroniveus | 'Sheet2'!A45 | 'Sheet1'!O42 / Q42 | 1 | -0.72289 | 번호 168, t=8.0, g=3, PDF 140쪽 |
| Nais christinae | 'Sheet2'!A46 | 'Sheet1'!O43 / Q43 | 1 | -1.89455 | 번호 172, t=5.6, g=2, PDF 140쪽 |
| Nais elinguis | 'Sheet2'!A47 | 'Sheet1'!O44 / Q44 | 1 | 0.94029 | 번호 174, t=6.2, g=1, PDF 140쪽 |
| Nais simplex | 'Sheet2'!A48 | 'Sheet1'!O45 / Q45 | 1 | 1.83441 | 번호 175, t=6.1, g=1, PDF 140쪽 |
| Nais sp. | 'Sheet2'!A49 | 'Sheet1'!O46 / Q46 | 3 | -1.40518666666667 | 번호 176, t=4.9, g=1, PDF 140쪽 |
| Nais stolci | 'Sheet2'!A50 | 'Sheet1'!O47 / Q47 | 2 | -0.88985 | 번호 177, t=5.4, g=1, PDF 140쪽 |
| Paraleptophlebia japonica | 'Sheet2'!A51 | 'Sheet1'!O48 / Q48 | 1 | -3.46193 | 번호 191, t=0.9, g=2, PDF 140쪽 |
| Paranais frici | 'Sheet2'!A52 | 'Sheet1'!O49 / Q49 | 5 | 0.314094 | 번호 193, t=5.3, g=1, PDF 140쪽 |
| Paranais litoralis | 'Sheet2'!A53 | 'Sheet1'!O50 / Q50 | 1 | 4.99447 | 번호 194, t=10.0, g=4, PDF 140쪽 |
| Paratanytarsus grimmii | 'Sheet2'!A54 | 'Sheet1'!O51 / Q51 | 1 | -0.15429 | 번호 195, t=4.2, g=1, PDF 140쪽 |
| Polypedilum nubeculosum | 'Sheet2'!A55 | 'Sheet1'!O52 / Q52 | 1 | -0.13879 | 번호 210, t=4.1, g=1, PDF 141쪽 |
| Polypedilum scalaenum | 'Sheet2'!A56 | 'Sheet1'!O53 / Q53 | 3 | 0.118106666666667 | 번호 213, t=5.4, g=1, PDF 141쪽 |
| Pristina aequiseta | 'Sheet2'!A57 | 'Sheet1'!O54 / Q54 | 5 | -0.383164 | 번호 220, t=4.2, g=1, PDF 141쪽 |
| Pristina leidyi | 'Sheet2'!A58 | 'Sheet1'!O55 / Q55 | 1 | -0.18154 | 번호 221, t=6.6, g=2, PDF 141쪽 |
| Pristina osborni | 'Sheet2'!A59 | 'Sheet1'!O56 / Q56 | 2 | -0.429655 | 번호 223, t=3.8, g=1, PDF 141쪽 |
| Pristina sp. | 'Sheet2'!A60 | 'Sheet1'!O57 / Q57 | 3 | -0.688633333333333 | 번호 224, t=5.2, g=2, PDF 141쪽 |
| Procladius culiciformis | 'Sheet2'!A61 | 'Sheet1'!O58 / Q58 | 1 | 1.86775 | 번호 226, t=6.1, g=2, PDF 141쪽 |
| Psectrocladius aquatronus | 'Sheet2'!A62 | 'Sheet1'!O59 / Q59 | 2 | 1.38315 | 번호 231, t=7.8, g=2, PDF 141쪽 |
| Radix plicatula | 'Sheet2'!A63 | 'Sheet1'!O60 / Q60 | 1 | -0.29118 | 표 37 정확 일치 없음 |
| Scapharca | 'Sheet2'!A64 | 'Sheet1'!O61 / Q61 | 1 | -2.73172 | 표 37 정확 일치 없음 |
| Semisulcospira gottschei | 'Sheet2'!A65 | 'Sheet1'!O62 / Q62 | 1 | -0.25128 | 표 37 정확 일치 없음 |
| Stictochironomus sinsauensis | 'Sheet2'!A66 | 'Sheet1'!O63 / Q63 | 4 | -0.034535 | 번호 246, t=3.2, g=1, PDF 141쪽 |
| Tanytarsus formosanus | 'Sheet2'!A67 | 'Sheet1'!O64 / Q64 | 26 | 0.190044615384615 | 번호 254, t=4.2, g=1, PDF 141쪽 |
| Tanytarsus kiseogi | 'Sheet2'!A68 | 'Sheet1'!O65 / Q65 | 1 | 1.61328 | 번호 255, t=6.1, g=2, PDF 142쪽 |
| Tanytarsus sp. | 'Sheet2'!A69 | 'Sheet1'!O66 / Q66 | 9 | -0.877195555555556 | 번호 260, t=3.7, g=1, PDF 142쪽 |
| Tanytarsus tamagotoi | 'Sheet2'!A70 | 'Sheet1'!O67 / Q67 | 3 | 1.02229 | 번호 262, t=5.6, g=1, PDF 142쪽 |
| Tanytarsus unagiseptimus | 'Sheet2'!A71 | 'Sheet1'!O68 / Q68 | 1 | 1.15825 | 번호 267, t=4.6, g=1, PDF 142쪽 |
| Tanytarsus yunosecundus | 'Sheet2'!A72 | 'Sheet1'!O69 / Q69 | 1 | -1.66634 | 번호 268, t=4.1, g=1, PDF 142쪽 |
| Tipula sp. | 'Sheet2'!A73 | 'Sheet1'!O70 / Q70 | 1 | -2.26115 | 표 37 정확 일치 없음 |
| Tubifex tubifex | 'Sheet2'!A74 | 'Sheet1'!O71 / Q71 | 5 | 1.135342 | 번호 274, t=5.6, g=1, PDF 142쪽 |
| Tubificinae sp. | 'Sheet2'!A75 | 'Sheet1'!O72 / Q72 | 2 | 0.71006 | 번호 275, t=5.5, g=2, PDF 142쪽 |

**[검증]** 71개 수식 전부를 원자료와 독립적으로 비교한 결과 절대 오차 1×10⁻¹² 이내로 일치했다(최대 차이 4.44e-16). 두 시트의 저장 셀에 Excel 오류 형식 값은 0개다. 이는 저장 계산값 검증이며 원본을 다시 계산한 결과는 아니다.

## 부록 C. 누락 주소와 320개 조사행 전체

### C.1 79개 누락 조사행

아래 각 행의 G:J는 빈 셀, K:M은 빈 문자열이다. A:F는 기록되어 있다. 빈칸은 미검출 또는 0으로 해석하지 않는다.

| 누락 범위 | 차수(A) | 코드(B) | 지점(C) | 유형(E) |
| --- | --- | --- | --- | --- |
| 'Sheet1'!G58:M58 | 2022_3차 | 1201F10 | 공촌천 | Urban |
| 'Sheet1'!G59:M59 | 2022_3차 | 1201F50 | 장만수천 | Urban |
| 'Sheet1'!G60:M60 | 2022_3차 | 1202E52 | C옥구천 | Industry |
| 'Sheet1'!G66:M66 | 2022_4차 | 1007R18 | 강천U | River |
| 'Sheet1'!G68:M68 | 2022_4차 | 1007R75 | 강상 | River |
| 'Sheet1'!G69:M69 | 2022_4차 | 1013R60 | 춘성교 | River |
| 'Sheet1'!G71:M71 | 2022_4차 | 1015R60 | 삼봉리 | River |
| 'Sheet1'!G72:M72 | 2022_4차 | 1016R80 | 경안천6 | River |
| 'Sheet1'!G77:M77 | 2022_4차 | 1101B40 | 서호2 | Lake |
| 'Sheet1'!G88:M88 | 2023_1차 | 3302A60 | 원평천2 | River |
| 'Sheet1'!G97:M97 | 2023_1차 | 3101B40 | 삽교호3 | Lake |
| 'Sheet1'!G102:M102 | 2023_1차 | 2004R90 | 내성천5 | River |
| 'Sheet1'!G103:M103 | 2023_1차 | 2011R57 | 다사D | River |
| 'Sheet1'!G108:M108 | 2023_1차 | 2016R30 | 황강6 | River |
| 'Sheet1'!G111:M111 | 2023_1차 | 2009A30 | 선산 | River |
| 'Sheet1'!G112:M112 | 2023_1차 | 2011R24 | 칠곡U | River |
| 'Sheet1'!G113:M113 | 2023_1차 | 2019R80 | 남강7 | River |
| 'Sheet1'!G115:M115 | 2023_1차 | 2001A30 | 황지2 | River |
| 'Sheet1'!G116:M116 | 2023_1차 | 2004B20 | 영주댐3 | Lake |
| 'Sheet1'!G118:M118 | 2023_1차 | 2301E21 | C상남리수로-1 | Industry |
| 'Sheet1'!G119:M119 | 2023_1차 | 2302E11 | C장림유수지 | Industry |
| 'Sheet1'!G121:M121 | 2023_1차 | 2302F28 | 죽성천 | Urban |
| 'Sheet1'!G125:M125 | 2023_2차 | 3302A50 | 고부천2 | River |
| 'Sheet1'!G127:M127 | 2023_2차 | 3203A40 | 웅천천2 | River |
| 'Sheet1'!G128:M128 | 2023_2차 | 3302A60 | 원평천2 | River |
| 'Sheet1'!G134:M134 | 2023_2차 | 3006A20 | 우산 | River |
| 'Sheet1'!G136:M136 | 2023_2차 | 3301B50 | 경천지1 | Lake |
| 'Sheet1'!G141:M141 | 2023_2차 | 3301F30 | 전주천6 | Urban |
| 'Sheet1'!G145:M145 | 2023_2차 | 2020R33 | 함안D | River |
| 'Sheet1'!G149:M149 | 2023_2차 | 2009A05 | 낙단 | River |
| 'Sheet1'!G166:M166 | 2023_3차 | 3004A50 | 영동 | River |
| 'Sheet1'!G172:M172 | 2023_3차 | 3012R41 | 부여U | River |
| 'Sheet1'!G173:M173 | 2023_3차 | 3302R40 | 동진강3 | River |
| 'Sheet1'!G175:M175 | 2023_3차 | 3005R30 | 초강2 | River |
| 'Sheet1'!G181:M181 | 2023_3차 | 3301F30 | 전주천6 | Urban |
| 'Sheet1'!G184:M184 | 2023_3차 | 2014R80 | 덕곡D | River |
| 'Sheet1'!G192:M192 | 2023_3차 | 2011R24 | 칠곡U | River |
| 'Sheet1'!G194:M194 | 2023_3차 | 2201A45 | 태화 | River |
| 'Sheet1'!G199:M199 | 2023_3차 | 2302E11 | C장림유수지 | Industry |
| 'Sheet1'!G200:M200 | 2023_3차 | 2022F10 | 덕천천 | Urban |
| 'Sheet1'!G201:M201 | 2023_3차 | 2302F28 | 죽성천 | Urban |
| 'Sheet1'!G205:M205 | 2023_4차 | 3302A50 | 고부천2 | River |
| 'Sheet1'!G206:M206 | 2023_4차 | 3004A50 | 영동 | River |
| 'Sheet1'!G208:M208 | 2023_4차 | 3302A60 | 원평천2 | River |
| 'Sheet1'!G209:M209 | 2023_4차 | 3012A32 | 금강 | River |
| 'Sheet1'!G213:M213 | 2023_4차 | 3302R40 | 동진강3 | River |
| 'Sheet1'!G216:M216 | 2023_4차 | 3301B50 | 경천지1 | Lake |
| 'Sheet1'!G219:M219 | 2023_4차 | 3302E11 | C정읍천 | Industry |
| 'Sheet1'!G221:M221 | 2023_4차 | 3301F30 | 전주천6 | Urban |
| 'Sheet1'!G224:M224 | 2023_4차 | 2014R80 | 덕곡D | River |
| 'Sheet1'!G227:M227 | 2023_4차 | 2401A10 | 왕피천 | River |
| 'Sheet1'!G230:M230 | 2023_4차 | 2007R23 | 도남U | River |
| 'Sheet1'!G232:M232 | 2023_4차 | 2011R24 | 칠곡U | River |
| 'Sheet1'!G236:M236 | 2023_4차 | 2004B20 | 영주댐3 | Lake |
| 'Sheet1'!G238:M238 | 2023_4차 | 2301E21 | C상남리수로-1 | Industry |
| 'Sheet1'!G244:M244 | 2024_1차 | 4001A03 | 광주천 | River |
| 'Sheet1'!G247:M247 | 2024_1차 | 4001A06 | 예전저수지 | Reservoir |
| 'Sheet1'!G249:M249 | 2024_1차 | 4001A08 | 수양저수지 | Reservoir |
| 'Sheet1'!G258:M258 | 2024_1차 | 4001A17 | 영산호2 | Lake |
| 'Sheet1'!G259:M259 | 2024_1차 | 4001A18 | 쌍봉천 | River |
| 'Sheet1'!G260:M260 | 2024_1차 | 4001A19 | C남수천 | Industry |
| 'Sheet1'!G263:M263 | 2024_2차 | 4001A02 | 평동천 | River |
| 'Sheet1'!G266:M266 | 2024_2차 | 4001A05 | 와탄천 | River |
| 'Sheet1'!G269:M269 | 2024_2차 | 4001A08 | 수양저수지 | Reservoir |
| 'Sheet1'!G272:M272 | 2024_2차 | 4001A11 | 삼포천2 | River |
| 'Sheet1'!G274:M274 | 2024_2차 | 4001A13 | 고막원천 | River |
| 'Sheet1'!G277:M277 | 2024_2차 | 4001A16 | 영암호3 | Lake |
| 'Sheet1'!G278:M278 | 2024_2차 | 4001A17 | 영산호2 | Lake |
| 'Sheet1'!G281:M281 | 2024_2차 | 4001A20 | 금사천 | River |
| 'Sheet1'!G290:M290 | 2024_3차 | 4001A09 | 화원2저수지 | Reservoir |
| 'Sheet1'!G292:M292 | 2024_3차 | 4001A11 | 삼포천2 | River |
| 'Sheet1'!G293:M293 | 2024_3차 | 4001A12 | 함평천 | River |
| 'Sheet1'!G294:M294 | 2024_3차 | 4001A13 | 고막원천 | River |
| 'Sheet1'!G298:M298 | 2024_3차 | 4001A17 | 영산호2 | Lake |
| 'Sheet1'!G300:M300 | 2024_3차 | 4001A19 | C남수천 | Industry |
| 'Sheet1'!G312:M312 | 2024_4차 | 4001A11 | 삼포천2 | River |
| 'Sheet1'!G314:M314 | 2024_4차 | 4001A13 | 고막원천 | River |
| 'Sheet1'!G317:M317 | 2024_4차 | 4001A16 | 영암호3 | Lake |
| 'Sheet1'!G318:M318 | 2024_4차 | 4001A17 | 영산호2 | Lake |

### C.2 전체 원자료

행마다 A:M을 순서대로 추출했다. 열 머리글의 알파벳과 행 주소를 결합해 단일 셀을 찾는다. 숫자는 소수 15자리 유효숫자로 표시하며, 이는 원본 Excel 정밀도를 읽기 쉽게 표현한 것이다.

| Sheet1 범위 | A 차수 | B 코드 | C 지점 | D 수계 | E 유형 | F PC1 | G 다양도 | H 균등도 | I 풍부도 | J 우점도 | K 우점종 | L 우점 분류군 | M 우점종 ASV count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A2:M2 | 2022_1차 | 1001R85 | 영월1 | Han | River | 1.24603 | 0.177925921415639 | 0.0641732111179855 | 1.44459913324523 | 0.981251160200483 | Tubifex tubifex | 실지렁이류 | 31383 |
| A3:M3 | 2022_1차 | 1004R70 | 달천5 | Han | River | -2.09713 | 0.389254058998014 | 0.147497386521255 | 1.14436076080046 | 0.99529269202088 | Corbicula fluminea | 이매패류 | 75834 |
| A4:M4 | 2022_1차 | 1005R60 | 원주 | Han | River | -2.89121 | 0.91274877518801 | 0.830819739231727 | 0.203318979623461 | 0.894542733443797 | Cladotanytarsus vanderwulpi | 깔따구류 | 10977 |
| A5:M5 | 2022_1차 | 1006R80 | 섬강4-1 | Han | River | -3.0834 | 0.302424095985157 | 0.117906458895726 | 1.50356160672556 | 0.972991452991453 | Limnodrilus hoffmeisteri | 실지렁이류 | 2772 |
| A6:M6 | 2022_1차 | 1007R18 | 강천U | Han | River | -2.3411 | 1.36531612352913 | 0.656578266887073 | 0.724708462363732 | 0.71308178509864 | Limnodrilus hoffmeisteri | 실지렁이류 | 8249 |
| A7:M7 | 2022_1차 | 1007R30 | 대신D | Han | River | -0.89577 | 0.46556423583276 | 0.202191978593672 | 0.928918714184874 | 0.950167348456675 | Limnodrilus hoffmeisteri | 실지렁이류 | 14519 |
| A8:M8 | 2022_1차 | 1007R75 | 강상 | Han | River | 1.40026 | 1.74353504695229 | 0.564060530795362 | 2.40718521273759 | 0.648178269355888 | Limnodrilus hoffmeisteri | 실지렁이류 | 3133 |
| A9:M9 | 2022_1차 | 1013R60 | 춘성교 | Han | River | 0.25248 | 1.07552658177961 | 0.338423022136743 | 2.19646838284379 | 0.905412298101445 | Limnodrilus hoffmeisteri | 실지렁이류 | 22037 |
| A10:M10 | 2022_1차 | 1014R70 | 홍천강6 | Han | River | -0.68804 | 1.7383982189023 | 0.724968366476476 | 1.45736238436684 | 0.598952879581152 | Limnodrilus hoffmeisteri | 실지렁이류 | 430 |
| A11:M11 | 2022_1차 | 1015R60 | 삼봉리 | Han | River | 1.15825 | 1.13339825814159 | 0.582451486103725 | 0.669944622465193 | 0.767474851689451 | Tanytarsus unagiseptimus | 깔따구류 | 4924 |
| A12:M12 | 2022_1차 | 1016R80 | 경안천6 | Han | River | 1.4731 | 2.41858660241258 | 0.807344041977183 | 2.48453415659242 | 0.419570405727924 | Limnodrilus claparedeanus | 실지렁이류 | 440 |
| A13:M13 | 2022_1차 | 1018R22 | 탄천 | Han | River | -1.89455 | 0.857806110773247 | 0.780808770866015 | 0.26572008099113 | 0.947226709746904 | Nais christinae | 지렁이류 | 973 |
| A14:M14 | 2022_1차 | 1019R25 | 행주 | Han | River | -1.2137 | 0.884258534417621 | 0.804886804506476 | 0.374368189198277 | 0.904306220095694 | Limnoperna fortunei | 이매패류 | 128 |
| A15:M15 | 2022_1차 | 1022E30 | C신천-1 | Han | Industry | 1.15247 | 2.04714275037509 | 0.635980653419246 | 2.77950834075463 | 0.60163613729326 | Limnodrilus sp. | 실지렁이류 | 1851 |
| A16:M16 | 2022_1차 | 1101B20 | 원천지2 | Han | Lake | 0.41724 | 0.957531668261816 | 0.43579144259467 | 0.981018809946024 | 0.906034482758621 | Limnodrilus hoffmeisteri | 실지렁이류 | 2462 |
| A17:M17 | 2022_1차 | 1101B40 | 서호2 | Han | Lake | 0.79675 | 1.51113129801152 | 0.522815549205144 | 1.57620274215556 | 0.652708492889818 | Glyptotendipes tokunagai | 깔따구류 | 17677 |
| A18:M18 | 2022_1차 | 1201F10 | 공촌천 | Han | Urban | 2.90417 | 0.874622493518318 | 0.297042152921749 | 1.80857063638426 | 0.88970343218927 | Branchiodrilus sp. | 지렁이류 | 16522 |
| A19:M19 | 2022_1차 | 1201F50 | 장만수천 | Han | Urban | 3.37002 | 2.06855456395484 | 0.783823276873038 | 1.60192783930657 | 0.509715994020927 | Tubifex tubifex | 실지렁이류 | 1042 |
| A20:M20 | 2022_1차 | 1202E52 | C옥구천 | Han | Industry | 4.99447 | 0.922962083235653 | 0.474308684644934 | 0.718872387949065 | 0.93570581257414 | Paranais litoralis | 실지렁이류 | 2633 |
| A21:M21 | 2022_1차 | 1202R10 | 반월천 | Han | River | -1.50209 | 0.644476381072982 | 0.222973525572393 | 1.61346545139268 | 0.928330545155209 | Dicrotendipes pelochloris | 깔따구류 | 32036 |
| A22:M22 | 2022_2차 | 1001R85 | 영월1 | Han | River | 0.87299 | 2.17508919574283 | 0.622074786771109 | 3.2851736117181 | 0.498940927277006 | Tanytarsus formosanus | 깔따구류 | 6795 |
| A23:M23 | 2022_2차 | 1004R70 | 달천5 | Han | River | 0.8958 | 0.148818749389485 | 0.0646311616635961 | 0.792751618899173 | 0.995434754544708 | Corbicula sp. | 이매패류 | 82717 |
| A24:M24 | 2022_2차 | 1005R60 | 원주 | Han | River | -3.14454 | 2.20579399232388 | 0.859975650555104 | 1.1495143485605 | 0.448921663301437 | Cladotanytarsus vanderwulpi | 깔따구류 | 8965 |
| A25:M25 | 2022_2차 | 1006R80 | 섬강4-1 | Han | River | -3.43287 | 1.75990039535941 | 0.73393547054521 | 1.2216532331211 | 0.580941766508777 | Corbicula leana | 이매패류 | 1383 |
| A26:M26 | 2022_2차 | 1007R18 | 강천U | Han | River | 0.98911 | 0.578255394087498 | 0.278082063139109 | 0.806895772246911 | 0.943135245901639 | Tanytarsus formosanus | 깔따구류 | 5025 |
| A27:M27 | 2022_2차 | 1007R30 | 대신D | Han | River | -0.58383 | 1.22099397962576 | 0.476030443281012 | 1.48012583026462 | 0.798433263031033 | Tanytarsus formosanus | 깔따구류 | 2355 |
| A28:M28 | 2022_2차 | 1007R75 | 강상 | Han | River | -0.03743 | 1.88680129144952 | 0.786857254715548 | 1.47869288424886 | 0.535260115606936 | Tanytarsus formosanus | 깔따구류 | 358 |
| A29:M29 | 2022_2차 | 1013R60 | 춘성교 | Han | River | 0.42624 | 1.48561100049275 | 0.473804414291518 | 2.10806440102267 | 0.768551133028062 | Limnodrilus hoffmeisteri | 실지렁이류 | 15557 |
| A30:M30 | 2022_2차 | 1014R70 | 홍천강6 | Han | River | -0.67755 | 1.42944109935124 | 0.687415861758968 | 0.894130534415135 | 0.757563694267516 | Cladotanytarsus vanderwulpi | 깔따구류 | 1179 |
| A31:M31 | 2022_2차 | 1015R60 | 삼봉리 | Han | River | 0.60048 | 1.09852940278675 | 0.61310093327428 | 0.642890550904136 | 0.793378038558257 | Limnodrilus hoffmeisteri | 실지렁이류 | 1568 |
| A32:M32 | 2022_2차 | 1016R80 | 경안천6 | Han | River | 1.6976 | 1.1435909127117 | 0.395655302674317 | 1.79102851727617 | 0.808301886792453 | Limnodrilus hoffmeisteri | 실지렁이류 | 9112 |
| A33:M33 | 2022_2차 | 1018R22 | 탄천 | Han | River | -1.94041 | 1.28411392970992 | 0.463146199582235 | 1.52758837246758 | 0.811551639745472 | Dero furcata | 지렁이류 | 8002 |
| A34:M34 | 2022_2차 | 1019R25 | 행주 | Han | River | -3.03789 | 1.38956906311794 | 0.668241465444325 | 1.30002904977577 | 0.788990825688073 | Limnodrilus hoffmeisteri | 실지렁이류 | 112 |
| A35:M35 | 2022_2차 | 1022E30 | C신천-1 | Han | Industry | -2.24694 | 2.08023834990236 | 0.694400620598339 | 2.31800251809251 | 0.539267015706806 | Pristina aequiseta | 지렁이류 | 979 |
| A36:M36 | 2022_2차 | 1101B20 | 원천지2 | Han | Lake | -0.82246 | 0.531547386260967 | 0.24191764089285 | 0.738019895220004 | 0.929055908413707 | Corbicula sp. | 이매패류 | 45331 |
| A37:M37 | 2022_2차 | 1101B40 | 서호2 | Han | Lake | 0.01386 | 0.983851616733739 | 0.383575454958468 | 1.25828867877897 | 0.865584415584416 | Tanytarsus formosanus | 깔따구류 | 10348 |
| A38:M38 | 2022_2차 | 1201F10 | 공촌천 | Han | Urban | 1.24295 | 0.0798901323444697 | 0.0281977114473468 | 1.3237391209919 | 0.992548326048754 | Tanytarsus formosanus | 깔따구류 | 175643 |
| A39:M39 | 2022_2차 | 1201F50 | 장만수천 | Han | Urban | -0.11396 | 1.64378489457636 | 0.685511545572233 | 0.917417776784261 | 0.65710067361816 | Chironomus flaviplumus | 깔따구류 | 20558 |
| A40:M40 | 2022_2차 | 1202E52 | C옥구천 | Han | Industry | 4.86106 | 0.607962584452555 | 0.276695696345073 | 0.997146059587502 | 0.908196721311475 | Tanytarsus formosanus | 깔따구류 | 2647 |
| A41:M41 | 2022_2차 | 1202R10 | 반월천 | Han | River | -2.47615 | 0.303123483480591 | 0.118179129969484 | 1.11443698895569 | 0.980112080225846 | Tanytarsus formosanus | 깔따구류 | 44534 |
| A42:M42 | 2022_3차 | 1001R85 | 영월1 | Han | River | 0.06292 | 0.546419488564661 | 0.19707917159933 | 1.76089562077818 | 0.936476228525769 | Limnodrilus hoffmeisteri | 실지렁이류 | 4472 |
| A43:M43 | 2022_3차 | 1004R70 | 달천5 | Han | River | -1.22867 | 1.8196532212766 | 0.629556809190899 | 1.72499783837921 | 0.619050118079244 | Tubifex tubifex | 실지렁이류 | 7636 |
| A44:M44 | 2022_3차 | 1005R60 | 원주 | Han | River | -0.68334 | 1.76922750728683 | 0.638113937741764 | 1.64428749702303 | 0.618844852058085 | Limnodrilus hoffmeisteri | 실지렁이류 | 3824 |
| A45:M45 | 2022_3차 | 1006R80 | 섬강4-1 | Han | River | -3.46193 | 0.466457535660571 | 0.260334907487072 | 0.633277249743165 | 0.946741154562384 | Paraleptophlebia japonica | 하루살이류 | 2406 |
| A46:M46 | 2022_3차 | 1007R18 | 강천U | Han | River | 0.65603 | 0.606050445016464 | 0.291448657184601 | 0.809925707643475 | 0.93579114482272 | Tanytarsus formosanus | 깔따구류 | 4835 |
| A47:M47 | 2022_3차 | 1007R30 | 대신D | Han | River | 1.90855 | 1.18882898868329 | 0.463490238208774 | 1.45628924210147 | 0.811609498680739 | Tanytarsus formosanus | 깔따구류 | 2735 |
| A48:M48 | 2022_3차 | 1007R75 | 강상 | Han | River | -0.07143 | 1.79387719712777 | 0.748104897439617 | 1.47668268806497 | 0.580756013745705 | Tanytarsus formosanus | 깔따구류 | 378 |
| A49:M49 | 2022_3차 | 1013R60 | 춘성교 | Han | River | -1.39338 | 1.44340158913145 | 0.626861345330175 | 1.10213994540395 | 0.729468599033816 | Limnodrilus hoffmeisteri | 실지렁이류 | 1863 |
| A50:M50 | 2022_3차 | 1014R70 | 홍천강6 | Han | River | -1.65218 | 1.42902297921767 | 0.687214788477904 | 0.889348572357426 | 0.754961832061069 | Cladotanytarsus vanderwulpi | 깔따구류 | 1230 |
| A51:M51 | 2022_3차 | 1015R60 | 삼봉리 | Han | River | 0.84675 | 1.07222894229646 | 0.666213299694693 | 0.541258701000519 | 0.811728395061728 | Limnodrilus hoffmeisteri | 실지렁이류 | 1068 |
| A52:M52 | 2022_3차 | 1016R80 | 경안천6 | Han | River | 2.2039 | 1.12928577096846 | 0.390706063288704 | 1.79600592820371 | 0.81365256469859 | Limnodrilus hoffmeisteri | 실지렁이류 | 8869 |
| A53:M53 | 2022_3차 | 1018R22 | 탄천 | Han | River | -1.47484 | 1.30260035607691 | 0.459760772625763 | 1.61560879276922 | 0.813081308130813 | Dero furcata | 지렁이류 | 8493 |
| A54:M54 | 2022_3차 | 1019R25 | 행주 | Han | River | -2.05129 | 1.61283916258905 | 0.734034736014266 | 1.5015363996002 | 0.70873786407767 | Chironomidae sp. | 깔따구류 | 85 |
| A55:M55 | 2022_3차 | 1022E30 | C신천-1 | Han | Industry | -2.34544 | 2.0962793406781 | 0.699755234866556 | 2.3087641204124 | 0.5416 | Pristina aequiseta | 지렁이류 | 1070 |
| A56:M56 | 2022_3차 | 1101B20 | 원천지2 | Han | Lake | -0.25546 | 1.21587072974725 | 0.448983822106539 | 1.45345764518144 | 0.804302203567681 | Branchiura sowerbyi | 실지렁이류 | 9720 |
| A57:M57 | 2022_3차 | 1101B40 | 서호2 | Han | Lake | 0.10278 | 0.983240192260844 | 0.39568496158386 | 1.16698294098472 | 0.866849359232691 | Tanytarsus formosanus | 깔따구류 | 9212 |
| A58:M58 | 2022_3차 | 1201F10 | 공촌천 | Han | Urban | -0.981 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A59:M59 | 2022_3차 | 1201F50 | 장만수천 | Han | Urban | 0.43608 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A60:M60 | 2022_3차 | 1202E52 | C옥구천 | Han | Industry | 3.6115 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A61:M61 | 2022_3차 | 1202R10 | 반월천 | Han | River | -3.52064 | 0.312028836840873 | 0.11254061388117 | 1.40634437199345 | 0.978446968813417 | Tanytarsus formosanus | 깔따구류 | 40167 |
| A62:M62 | 2022_4차 | 1001R85 | 영월1 | Han | River | 0.91231 | 0.435991658597542 | 0.175455950683193 | 1.06745565716148 | 0.971115871209586 | Tubifex tubifex | 실지렁이류 | 26819 |
| A63:M63 | 2022_4차 | 1004R70 | 달천5 | Han | River | 1.89837 | 1.78622671735808 | 0.617992032505269 | 1.94579016402824 | 0.659922928709056 | Cladopelma edwardsi | 깔따구류 | 2199 |
| A64:M64 | 2022_4차 | 1005R60 | 원주 | Han | River | -0.1336 | 1.99319473664023 | 0.718893040519211 | 1.64927061460432 | 0.5665544332211 | Ephoron shigae | 하루살이류 | 2961 |
| A65:M65 | 2022_4차 | 1006R80 | 섬강4-1 | Han | River | -4.00635 | 1.71555164626644 | 0.715440605654298 | 1.14287138557697 | 0.637559429477021 | Cladotanytarsus vanderwulpi | 깔따구류 | 2496 |
| A66:M66 | 2022_4차 | 1007R18 | 강천U | Han | River | 1.16661 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A67:M67 | 2022_4차 | 1007R30 | 대신D | Han | River | 0.16106 | 1.84523355140254 | 0.6992017682585 | 1.42873443241294 | 0.565951263134362 | Limnodrilus sp. | 실지렁이류 | 3205 |
| A68:M68 | 2022_4차 | 1007R75 | 강상 | Han | River | 1.12198 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A69:M69 | 2022_4차 | 1013R60 | 춘성교 | Han | River | -1.21945 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A70:M70 | 2022_4차 | 1014R70 | 홍천강6 | Han | River | 0.87472 | 0.132459349011247 | 0.120569695403492 | 0.230392411142335 | 0.996264221429784 | Paranais frici | 실지렁이류 | 5734 |
| A71:M71 | 2022_4차 | 1015R60 | 삼봉리 | Han | River | 1.92327 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A72:M72 | 2022_4차 | 1016R80 | 경안천6 | Han | River | 1.65408 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A73:M73 | 2022_4차 | 1018R22 | 탄천 | Han | River | -1.64772 | 0.953085573912459 | 0.531927186813238 | 0.500798613514184 | 0.873281668050558 | Dero furcata | 지렁이류 | 14034 |
| A74:M74 | 2022_4차 | 1019R25 | 행주 | Han | River | 1.42812 | 1.08611608438151 | 0.471694222153255 | 0.864450472401027 | 0.897896542385122 | Tanytarsus formosanus | 깔따구류 | 15915 |
| A75:M75 | 2022_4차 | 1022E30 | C신천-1 | Han | Industry | -0.97141 | 1.65387452140442 | 0.610725207653564 | 1.61948817823108 | 0.697359154929577 | Aulodrilus pluriseta | 실지렁이류 | 3176 |
| A76:M76 | 2022_4차 | 1101B20 | 원천지2 | Han | Lake | 0.13237 | 1.60035889968157 | 0.695027039196465 | 1.06058173668823 | 0.615146512587701 | Limnodrilus hoffmeisteri | 실지렁이류 | 1787 |
| A77:M77 | 2022_4차 | 1101B40 | 서호2 | Han | Lake | -0.2079 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A78:M78 | 2022_4차 | 1201F10 | 공촌천 | Han | Urban | -0.16954 | 0.901294682645831 | 0.306100649061841 | 1.67155739970229 | 0.926435910392454 | Tanytarsus formosanus | 깔따구류 | 34427 |
| A79:M79 | 2022_4차 | 1201F50 | 장만수천 | Han | Urban | 3.37999 | 1.07273924970395 | 0.551278922217829 | 0.668204230654621 | 0.89252866322288 | Limnodrilus hoffmeisteri | 실지렁이류 | 3935 |
| A80:M80 | 2022_4차 | 1202E52 | C옥구천 | Han | Industry | 2.1668 | 0.169842215725535 | 0.154597047090599 | 0.230847856375011 | 0.996199689065469 | Paranais frici | 실지렁이류 | 5576 |
| A81:M81 | 2022_4차 | 1202R10 | 반월천 | Han | River | -0.66055 | 0.338330828876825 | 0.210216763419681 | 0.625954515393386 | 0.964765100671141 | Tanytarsus formosanus | 깔따구류 | 554 |
| A82:M82 | 2023_1차 | 3009A80 | 갑천6 | Geum | River | -2.21899 | 0.943154196118212 | 0.429247973032249 | 0.762471862027215 | 0.878999805733633 | Limnodrilus hoffmeisteri | 실지렁이류 | 25149 |
| A83:M83 | 2023_1차 | 3010R20 | 부강 | Geum | River | 0.75797 | 1.80686822584227 | 0.651689957240622 | 1.45684266081172 | 0.656628743121434 | Limnodrilus hoffmeisteri | 실지렁이류 | 11029 |
| A84:M84 | 2023_1차 | 3008A60 | 현도 | Geum | River | 0.48597 | 1.16852840775606 | 0.72604752176416 | 0.507005603838117 | 0.697264893218434 | Pristina osborni | 지렁이류 | 1016 |
| A85:M85 | 2023_1차 | 3302A50 | 고부천2 | Geum | River | 0.44382 | 2.64116122528228 | 0.784356753500001 | 2.80696031280134 | 0.258295713687346 | Tanytarsus tamagotoi | 깔따구류 | 2825 |
| A86:M86 | 2023_1차 | 3004A50 | 영동 | Geum | River | -0.25128 | 1.09956466268162 | 0.56506445748044 | 0.660651896746961 | 0.81466742467311 | Semisulcospira gottschei | 복족류 | 5779 |
| A87:M87 | 2023_1차 | 3203A40 | 웅천천2 | Geum | River | 2.74992 | 1.27754445066879 | 0.581435536379083 | 0.951292856733087 | 0.784632516703786 | Psectrocladius aquatronus | 깔따구류 | 1921 |
| A88:M88 | 2023_1차 | 3302A60 | 원평천2 | Geum | River | -0.33474 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A89:M89 | 2023_1차 | 3012A32 | 금강 | Geum | River | -0.72185 | 1.17803047103785 | 0.424884679645601 | 1.53843605050773 | 0.838200151541645 | Paranais frici | 실지렁이류 | 12009 |
| A90:M90 | 2023_1차 | 3003A20 | 무주남대천2 | Geum | River | -0.58657 | 1.16135165276919 | 0.558492090059439 | 0.914728285344716 | 0.867996201329535 | Stictochironomus sinsauensis | 깔따구류 | 1170 |
| A91:M91 | 2023_1차 | 3011R97 | 미호천10 | Geum | River | -1.52432 | 1.42755262917538 | 0.476528774542929 | 1.71938522852839 | 0.742746891524939 | Cladotanytarsus vanderwulpi | 깔따구류 | 32578 |
| A92:M92 | 2023_1차 | 3012R41 | 부여U | Geum | River | -0.56269 | 1.91072020197753 | 0.573410244222095 | 2.85036416615137 | 0.607140109255982 | Amphichaeta raptisae | 지렁이류 | 6720 |
| A93:M93 | 2023_1차 | 3302R40 | 동진강3 | Geum | River | 0.94808 | 1.54218952632702 | 0.601255351042596 | 1.28967773464344 | 0.64018564018564 | Limnodrilus sp. | 실지렁이류 | 3771 |
| A94:M94 | 2023_1차 | 3006A20 | 우산 | Geum | River | -0.62145 | 1.78264867205904 | 0.7741944814474 | 1.42266635307802 | 0.590339892665474 | Ephoron shigae | 하루살이류 | 203 |
| A95:M95 | 2023_1차 | 3005R30 | 초강2 | Geum | River | -2.07046 | 1.1071669034427 | 0.43165253934621 | 1.13515813757705 | 0.833829110678018 | Cladotanytarsus vanderwulpi | 깔따구류 | 25722 |
| A96:M96 | 2023_1차 | 3301B50 | 경천지1 | Geum | Lake | -0.15429 | 1.04282441060789 | 0.376119401425489 | 1.46323073295955 | 0.813517426462799 | Paratanytarsus grimmii | 깔따구류 | 21879 |
| A97:M97 | 2023_1차 | 3101B40 | 삽교호3 | Geum | Lake | -1.0966 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A98:M98 | 2023_1차 | 3101E10 | C천안천 | Geum | Industry | 0.19893 | 1.38492867998388 | 0.524781581833157 | 1.28730166155507 | 0.72772521596051 | Chironomidae sp. | 깔따구류 | 13798 |
| A99:M99 | 2023_1차 | 3302E11 | C정읍천 | Geum | Industry | -0.30022 | 1.16289438473434 | 0.381962822912848 | 1.94512237021219 | 0.839142641922893 | Limnodrilus hoffmeisteri | 실지렁이류 | 21313 |
| A100:M100 | 2023_1차 | 3009F20 | 유등천5 | Geum | Urban | -0.30236 | 1.4162833035094 | 0.644578309435449 | 0.902178230998948 | 0.648724813301395 | Chaetogaster diaphanus | 지렁이류 | 2946 |
| A101:M101 | 2023_1차 | 3301F30 | 전주천6 | Geum | Urban | -0.79986 | 1.48769468745919 | 0.50525573733586 | 1.98357584896934 | 0.719931271477663 | Cladotanytarsus vanderwulpi | 깔따구류 | 5483 |
| A102:M102 | 2023_1차 | 2004R90 | 내성천5 | Nakdong | River | 1.252 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A103:M103 | 2023_1차 | 2011R57 | 다사D | Nakdong | River | 1.34339 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A104:M104 | 2023_1차 | 2014R80 | 덕곡D | Nakdong | River | -0.13879 | 1.43130969953687 | 0.735547682009745 | 0.79457707847037 | 0.718864950078823 | Polypedilum nubeculosum | 깔따구류 | 793 |
| A105:M105 | 2023_1차 | 2020R33 | 함안D | Nakdong | River | 0.12002 | 0.785827657774815 | 0.341280615498559 | 0.846295716052889 | 0.923002864226057 | Glyptotendipes tokunagai | 깔따구류 | 31993 |
| A106:M106 | 2023_1차 | 2006R20 | 병성천 | Nakdong | River | 1.08362 | 1.57064673954381 | 0.612350000195809 | 1.3024739377079 | 0.74095124139994 | Cladotanytarsus vanderwulpi | 깔따구류 | 4430 |
| A107:M107 | 2023_1차 | 2401A10 | 왕피천 | Nakdong | River | 1.98786 | 1.53608918072621 | 0.699104313947038 | 1.01060144969217 | 0.743524261218533 | Tanytarsus tamagotoi | 깔따구류 | 1052 |
| A108:M108 | 2023_1차 | 2016R30 | 황강6 | Nakdong | River | -0.33232 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A109:M109 | 2023_1차 | 2009A05 | 낙단 | Nakdong | River | -1.62368 | 0.43782888629947 | 0.224999538910892 | 0.6427461863726 | 0.974044318884082 | Fridericia peregrinabunda | 지렁이류 | 10096 |
| A110:M110 | 2023_1차 | 2007R23 | 도남U | Nakdong | River | -1.7285 | 1.5435050331664 | 0.499347730242083 | 2.3949161311183 | 0.717218852076528 | Limnodrilus hoffmeisteri | 실지렁이류 | 4034 |
| A111:M111 | 2023_1차 | 2009A30 | 선산 | Nakdong | River | -0.8171 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A112:M112 | 2023_1차 | 2011R24 | 칠곡U | Nakdong | River | -1.55211 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A113:M113 | 2023_1차 | 2019R80 | 남강7 | Nakdong | River | 0.03522 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A114:M114 | 2023_1차 | 2201A45 | 태화 | Nakdong | River | -1.11966 | 1.15445067212042 | 0.717300532814244 | 0.452340636740728 | 0.83971119133574 | Corbicula sp. | 이매패류 | 2938 |
| A115:M115 | 2023_1차 | 2001A30 | 황지2 | Nakdong | River | -2.44651 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A116:M116 | 2023_1차 | 2004B20 | 영주댐3 | Nakdong | Lake | -0.18879 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A117:M117 | 2023_1차 | 2018B10 | 낙동강하구3 | Nakdong | Lake | -1.43086 | 0.724856131191297 | 0.348582115275882 | 0.777501920636564 | 0.910813138147374 | Limnodrilus hoffmeisteri | 실지렁이류 | 6475 |
| A118:M118 | 2023_1차 | 2301E21 | C상남리수로-1 | Nakdong | Industry | 0.23728 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A119:M119 | 2023_1차 | 2302E11 | C장림유수지 | Nakdong | Industry | -0.66283 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A120:M120 | 2023_1차 | 2022F10 | 덕천천 | Nakdong | Urban | -1.99161 | 1.4266115079388 | 0.796207042540946 | 0.630243755065609 | 0.62782359268555 | Limnodrilus hoffmeisteri | 실지렁이류 | 1022 |
| A121:M121 | 2023_1차 | 2302F28 | 죽성천 | Nakdong | Urban | 0.24358 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A122:M122 | 2023_2차 | 3009A80 | 갑천6 | Geum | River | -1.29441 | 1.54449345408561 | 0.670764984445073 | 0.836881148489031 | 0.674888419074466 | Dicrotendipes nervosus | 깔따구류 | 20401 |
| A123:M123 | 2023_2차 | 3010R20 | 부강 | Geum | River | 2.63079 | 1.79553379579407 | 0.621212060659282 | 1.53980953780241 | 0.580929769963746 | Dicrotendipes nervosus | 깔따구류 | 27737 |
| A124:M124 | 2023_2차 | 3008A60 | 현도 | Geum | River | -1.45215 | 1.51844420437837 | 0.659451939039499 | 0.851809935928342 | 0.669700642033881 | Dicrotendipes nervosus | 깔따구류 | 16758 |
| A125:M125 | 2023_2차 | 3302A50 | 고부천2 | Geum | River | 0.0468 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A126:M126 | 2023_2차 | 3004A50 | 영동 | Geum | River | 3.18692 | 1.70252853357023 | 0.645127528858359 | 1.18646015372145 | 0.61881015483331 | Dicrotendipes nervosus | 깔따구류 | 24424 |
| A127:M127 | 2023_2차 | 3203A40 | 웅천천2 | Geum | River | 1.1015 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A128:M128 | 2023_2차 | 3302A60 | 원평천2 | Geum | River | 0.18351 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A129:M129 | 2023_2차 | 3012A32 | 금강 | Geum | River | -1.1372 | 1.74443818338851 | 0.661008066711015 | 1.34856905509153 | 0.610348193947283 | Dicrotendipes nervosus | 깔따구류 | 7061 |
| A130:M130 | 2023_2차 | 3003A20 | 무주남대천2 | Geum | River | -2.0831 | 1.57382267224187 | 0.581164511500305 | 1.33286059028947 | 0.679679569833475 | Stictochironomus sinsauensis | 깔따구류 | 13688 |
| A131:M131 | 2023_2차 | 3011R97 | 미호천10 | Geum | River | -1.48164 | 1.0624734460812 | 0.414227845470096 | 1.14438794838866 | 0.798542265910805 | Tanytarsus sp. | 깔따구류 | 26219 |
| A132:M132 | 2023_2차 | 3012R41 | 부여U | Geum | River | -1.58558 | 1.63442785740201 | 0.589495241141163 | 1.39309258070743 | 0.637189403359396 | Dicrotendipes nervosus | 깔따구류 | 22505 |
| A133:M133 | 2023_2차 | 3302R40 | 동진강3 | Geum | River | 0.92859 | 1.41421633395469 | 0.522226779023183 | 1.24088960369097 | 0.666968941283156 | Dicrotendipes nervosus | 깔따구류 | 40324 |
| A134:M134 | 2023_2차 | 3006A20 | 우산 | Geum | River | -1.05167 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A135:M135 | 2023_2차 | 3005R30 | 초강2 | Geum | River | -2.58126 | 1.55879708754625 | 0.52033925104294 | 1.75727916194726 | 0.69786985348945 | Dicrotendipes nervosus | 깔따구류 | 24720 |
| A136:M136 | 2023_2차 | 3301B50 | 경천지1 | Geum | Lake | 0.80814 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A137:M137 | 2023_2차 | 3101B40 | 삽교호3 | Geum | Lake | 1.82551 | 0.291953743043804 | 0.121754167646818 | 0.89664605689394 | 0.993634408602151 | Glyptotendipes tokunagai | 깔따구류 | 64720 |
| A138:M138 | 2023_2차 | 3101E10 | C천안천 | Geum | Industry | -0.53227 | 1.93918071733283 | 0.588372785478236 | 2.45142752652349 | 0.55746799078729 | Limnodrilus hoffmeisteri | 실지렁이류 | 17676 |
| A139:M139 | 2023_2차 | 3302E11 | C정읍천 | Geum | Industry | 1.62829 | 0.503537241004288 | 0.258766953473542 | 0.611170899039186 | 0.948056903035919 | Limnodrilus hoffmeisteri | 실지렁이류 | 15995 |
| A140:M140 | 2023_2차 | 3009F20 | 유등천5 | Geum | Urban | 1.20052 | 1.43438110730713 | 0.577237421546402 | 1.26494814974839 | 0.713162736243519 | Chironomidae sp. | 깔따구류 | 2588 |
| A141:M141 | 2023_2차 | 3301F30 | 전주천6 | Geum | Urban | -0.52138 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A142:M142 | 2023_2차 | 2004R90 | 내성천5 | Nakdong | River | -1.6434 | 1.35950784747652 | 0.399714481378359 | 2.61506472857761 | 0.797086400146596 | Cladotanytarsus vanderwulpi | 깔따구류 | 41837 |
| A143:M143 | 2023_2차 | 2011R57 | 다사D | Nakdong | River | 2.58015 | 1.43773481950386 | 0.560531464421095 | 1.10002789442823 | 0.664007611241218 | Dicrotendipes nervosus | 깔따구류 | 28618 |
| A144:M144 | 2023_2차 | 2014R80 | 덕곡D | Nakdong | River | 1.59318 | 1.14878310142419 | 0.462304329026686 | 1.10729015067292 | 0.829559229985938 | Amphichaeta raptisae | 지렁이류 | 13797 |
| A145:M145 | 2023_2차 | 2020R33 | 함안D | Nakdong | River | 1.43994 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A146:M146 | 2023_2차 | 2006R20 | 병성천 | Nakdong | River | 3.68093 | 1.63064557541005 | 0.520060144625985 | 1.96651452637068 | 0.655647573676047 | Stictochironomus sinsauensis | 깔따구류 | 33976 |
| A147:M147 | 2023_2차 | 2401A10 | 왕피천 | Nakdong | River | -0.68719 | 1.45699447969499 | 0.525499677614641 | 1.37193033734648 | 0.682553282638963 | Dicrotendipes nervosus | 깔따구류 | 29712 |
| A148:M148 | 2023_2차 | 2016R30 | 황강6 | Nakdong | River | 0.01638 | 2.9917695068877 | 0.822460108302351 | 3.76378086310063 | 0.302963480879901 | Psectrocladius aquatronus | 깔따구류 | 3492 |
| A149:M149 | 2023_2차 | 2009A05 | 낙단 | Nakdong | River | 0.72563 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A150:M150 | 2023_2차 | 2007R23 | 도남U | Nakdong | River | -2.30628 | 1.58283607690852 | 0.570887439674016 | 1.59058044959203 | 0.654497312043649 | Limnodrilus hoffmeisteri | 실지렁이류 | 7026 |
| A151:M151 | 2023_2차 | 2009A30 | 선산 | Nakdong | River | -1.7392 | 1.24050745732209 | 0.564579274288842 | 0.744419636545406 | 0.745142340713963 | Dicrotendipes nervosus | 깔따구류 | 28983 |
| A152:M152 | 2023_2차 | 2011R24 | 칠곡U | Nakdong | River | -1.66634 | 0.0233881901540447 | 0.0337420259506084 | 0.129377894459861 | 1 | Tanytarsus yunosecundus | 깔따구류 | 2266 |
| A153:M153 | 2023_2차 | 2019R80 | 남강7 | Nakdong | River | -1.17249 | 0.99132422362485 | 0.615944371613304 | 0.534487349411691 | 0.816750983698707 | Limnodrilus claparedeanus | 실지렁이류 | 1200 |
| A154:M154 | 2023_2차 | 2201A45 | 태화 | Nakdong | River | -0.72289 | 1.99126933889049 | 0.702830707425533 | 2.3044386985622 | 0.562741312741313 | Monopylephorus rubroniveus | 지렁이류 | 439 |
| A155:M155 | 2023_2차 | 2001A30 | 황지2 | Nakdong | River | -1.66463 | 1.35719921491121 | 0.460936437981619 | 1.63030368368555 | 0.783431933689257 | Nais sp. | 지렁이류 | 27543 |
| A156:M156 | 2023_2차 | 2004B20 | 영주댐3 | Nakdong | Lake | 1.13158 | 0.276197177050938 | 0.104657513101924 | 1.29908005532262 | 0.985484379930577 | Limnodrilus hoffmeisteri | 실지렁이류 | 20943 |
| A157:M157 | 2023_2차 | 2018B10 | 낙동강하구3 | Nakdong | Lake | 1.62634 | 1.20388708014741 | 0.54791262238971 | 0.779283802312794 | 0.763833785759031 | Paranais frici | 실지렁이류 | 16197 |
| A158:M158 | 2023_2차 | 2301E21 | C상남리수로-1 | Nakdong | Industry | -2.00509 | 0.586835896253883 | 0.301573994327938 | 0.56748554105876 | 0.917315175097276 | Limnodrilus hoffmeisteri | 실지렁이류 | 33668 |
| A159:M159 | 2023_2차 | 2302E11 | C장림유수지 | Nakdong | Industry | -2.04837 | 0.20760679554072 | 0.149756647190723 | 0.268813418611769 | 0.992330022483422 | Limnodrilus hoffmeisteri | 실지렁이류 | 67093 |
| A160:M160 | 2023_2차 | 2022F10 | 덕천천 | Nakdong | Urban | -1.12654 | 1.30248163269251 | 0.626361264111482 | 0.864083226188592 | 0.826561552456034 | Limnodrilus hoffmeisteri | 실지렁이류 | 1379 |
| A161:M161 | 2023_2차 | 2302F28 | 죽성천 | Nakdong | Urban | -2.09115 | 1.49578082595358 | 0.459096533358682 | 2.10582903303699 | 0.69620668701501 | Chironomus flaviplumus | 깔따구류 | 77757 |
| A162:M162 | 2023_3차 | 3009A80 | 갑천6 | Geum | River | -2.37554 | 1.83047989252311 | 0.713651475105413 | 1.34083834107248 | 0.502271252433485 | Paranais frici | 실지렁이류 | 2136 |
| A163:M163 | 2023_3차 | 3010R20 | 부강 | Geum | River | 0.47416 | 1.79391566263247 | 0.598823759542524 | 1.66368730023597 | 0.661456276600412 | Tanytarsus formosanus | 깔따구류 | 42362 |
| A164:M164 | 2023_3차 | 3008A60 | 현도 | Geum | River | -1.66905 | 1.94424449340078 | 0.660310676212819 | 1.97423464868628 | 0.525403270053769 | Dero furcata | 지렁이류 | 2747 |
| A165:M165 | 2023_3차 | 3302A50 | 고부천2 | Geum | River | -2.53043 | 0.724772901122295 | 0.267636434814725 | 1.25762387450296 | 0.984223620664423 | Limnodrilus hoffmeisteri | 실지렁이류 | 44788 |
| A166:M166 | 2023_3차 | 3004A50 | 영동 | Geum | River | -3.24692 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A167:M167 | 2023_3차 | 3203A40 | 웅천천2 | Geum | River | -0.96466 | 1.26305613655654 | 0.466407947697004 | 1.40742201538485 | 0.76367552045944 | Tanytarsus formosanus | 깔따구류 | 13098 |
| A168:M168 | 2023_3차 | 3302A60 | 원평천2 | Geum | River | -1.89918 | 1.20702012661369 | 0.379798515395675 | 1.9753187300161 | 0.807177327366851 | Ilyodrilus templetoni | 실지렁이류 | 50753 |
| A169:M169 | 2023_3차 | 3012A32 | 금강 | Geum | River | -1.19803 | 0.467452952431357 | 0.1822464646608 | 1.302403478545 | 0.940302969902332 | Tanytarsus formosanus | 깔따구류 | 9190 |
| A170:M170 | 2023_3차 | 3003A20 | 무주남대천2 | Geum | River | -1.34528 | 0.633543494564291 | 0.353587356698743 | 0.543730373301792 | 0.910603754439371 | Pristina osborni | 지렁이류 | 8130 |
| A171:M171 | 2023_3차 | 3011R97 | 미호천10 | Geum | River | -3.13628 | 1.15171193376886 | 0.500182137577941 | 0.93733337378996 | 0.838201487491548 | Tanytarsus formosanus | 깔따구류 | 8545 |
| A172:M172 | 2023_3차 | 3012R41 | 부여U | Geum | River | 0.37986 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A173:M173 | 2023_3차 | 3302R40 | 동진강3 | Geum | River | -0.83102 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A174:M174 | 2023_3차 | 3006A20 | 우산 | Geum | River | 0.5769 | 0.655386310828813 | 0.365778064569779 | 0.481512962744185 | 0.940437902028699 | Tanytarsus formosanus | 깔따구류 | 26043 |
| A175:M175 | 2023_3차 | 3005R30 | 초강2 | Geum | River | -0.31004 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A176:M176 | 2023_3차 | 3301B50 | 경천지1 | Geum | Lake | 0.50234 | 1.98820195345899 | 0.62560361139047 | 2.17491412925349 | 0.537868144780199 | Pristina aequiseta | 지렁이류 | 11883 |
| A177:M177 | 2023_3차 | 3101B40 | 삽교호3 | Geum | Lake | 0.6 | 1.42763112833712 | 0.503891149366545 | 1.54450159888942 | 0.749223454833597 | Tanytarsus formosanus | 깔따구류 | 19019 |
| A178:M178 | 2023_3차 | 3101E10 | C천안천 | Geum | Industry | -0.18154 | 2.2531139176969 | 0.59904122311807 | 4.31111382692313 | 0.549465397720597 | Pristina leidyi | 지렁이류 | 6868 |
| A179:M179 | 2023_3차 | 3302E11 | C정읍천 | Geum | Industry | 1.09193 | 1.36108898337822 | 0.480404691808205 | 1.59487334585775 | 0.743559307130924 | Tanytarsus formosanus | 깔따구류 | 13985 |
| A180:M180 | 2023_3차 | 3009F20 | 유등천5 | Geum | Urban | 1.37702 | 0.720858363755505 | 0.370447918217325 | 0.586296714698692 | 0.963595198734996 | Tubifex tubifex | 실지렁이류 | 20382 |
| A181:M181 | 2023_3차 | 3301F30 | 전주천6 | Geum | Urban | 1.3331 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A182:M182 | 2023_3차 | 2004R90 | 내성천5 | Nakdong | River | -2.00729 | 1.03101374675523 | 0.447763580982195 | 1.27133289632248 | 0.909856781802864 | Amphichaeta raptisae | 지렁이류 | 745 |
| A183:M183 | 2023_3차 | 2011R57 | 다사D | Nakdong | River | 0.07605 | 1.23888663448183 | 0.516655855881493 | 0.980485766216458 | 0.789597053242549 | Chironomus circumdatus | 깔따구류 | 12446 |
| A184:M184 | 2023_3차 | 2014R80 | 덕곡D | Nakdong | River | -0.36375 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A185:M185 | 2023_3차 | 2020R33 | 함안D | Nakdong | River | -2.03654 | 1.00335578035031 | 0.435751878791871 | 1.31182643997765 | 0.815513626834382 | Amphichaeta raptisae | 지렁이류 | 730 |
| A186:M186 | 2023_3차 | 2006R20 | 병성천 | Nakdong | River | -2.844 | 0.223610408012947 | 0.114913018014477 | 0.551849856906407 | 0.984878955756242 | Cladotanytarsus vanderwulpi | 깔따구류 | 50393 |
| A187:M187 | 2023_3차 | 2401A10 | 왕피천 | Nakdong | River | -1.1494 | 0.26861242377377 | 0.149915448131828 | 0.565481225748303 | 0.975140916317387 | Stictochironomus sinsauensis | 깔따구류 | 6526 |
| A188:M188 | 2023_3차 | 2016R30 | 황강6 | Nakdong | River | -2.3034 | 1.12257392547044 | 0.358021367020057 | 2.16404238810819 | 0.907759151030452 | Limnodrilus hoffmeisteri | 실지렁이류 | 13006 |
| A189:M189 | 2023_3차 | 2009A05 | 낙단 | Nakdong | River | -1.77103 | 1.51683792332812 | 0.560121788994439 | 1.23981804992403 | 0.71557573338655 | Limnodrilus sp. | 실지렁이류 | 29197 |
| A190:M190 | 2023_3차 | 2007R23 | 도남U | Nakdong | River | -2.17435 | 1.37071950843269 | 0.431307832278793 | 2.23981917929918 | 0.745315102720711 | Tanytarsus formosanus | 깔따구류 | 19981 |
| A191:M191 | 2023_3차 | 2009A30 | 선산 | Nakdong | River | -3.26537 | 1.1794338302026 | 0.366411720853162 | 2.24712593313938 | 0.835759122577085 | Chironomidae sp. | 깔따구류 | 30850 |
| A192:M192 | 2023_3차 | 2011R24 | 칠곡U | Nakdong | River | -0.88763 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A193:M193 | 2023_3차 | 2019R80 | 남강7 | Nakdong | River | 0.91744 | 2.30128689593119 | 0.670150107992677 | 3.11082473359041 | 0.436045380875203 | Limnodrilus hoffmeisteri | 실지렁이류 | 3753 |
| A194:M194 | 2023_3차 | 2201A45 | 태화 | Nakdong | River | -0.12809 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A195:M195 | 2023_3차 | 2001A30 | 황지2 | Nakdong | River | -1.91043 | 1.47220690383308 | 0.463241651156015 | 2.28716379660552 | 0.779208515752425 | Tanytarsus sp. | 깔따구류 | 10185 |
| A196:M196 | 2023_3차 | 2004B20 | 영주댐3 | Nakdong | Lake | -2.15938 | 0.752540732922152 | 0.31383386149468 | 1.09059460041714 | 0.887268180871015 | Chironomidae sp. | 깔따구류 | 7979 |
| A197:M197 | 2023_3차 | 2018B10 | 낙동강하구3 | Nakdong | Lake | 1.81429 | 0.760152908507598 | 0.296361761021239 | 1.13694070090985 | 0.876652326945639 | Limnodrilus hoffmeisteri | 실지렁이류 | 31868 |
| A198:M198 | 2023_3차 | 2301E21 | C상남리수로-1 | Nakdong | Industry | 1.06943 | 1.75135269993116 | 0.631666963759546 | 1.73783802016037 | 0.605530776092774 | Hippeutis cantori | 복족류 | 2195 |
| A199:M199 | 2023_3차 | 2302E11 | C장림유수지 | Nakdong | Industry | 1.97877 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A200:M200 | 2023_3차 | 2022F10 | 덕천천 | Nakdong | Urban | 2.05348 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A201:M201 | 2023_3차 | 2302F28 | 죽성천 | Nakdong | Urban | 0.68101 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A202:M202 | 2023_4차 | 3009A80 | 갑천6 | Geum | River | -2.0919 | 1.56537697510955 | 0.610295470573643 | 1.35404389149059 | 0.728650332814049 | Hippeutis sp. | 복족류 | 2920 |
| A203:M203 | 2023_4차 | 3010R20 | 부강 | Geum | River | -0.19897 | 0.867896008071248 | 0.361940747753509 | 0.975279094982668 | 0.96349670554244 | Limnodrilus sp. | 실지렁이류 | 14892 |
| A204:M204 | 2023_4차 | 3008A60 | 현도 | Geum | River | -2.73172 | 0 | 0 | 0 | 1 | Scapharca | 이매패류 | 334 |
| A205:M205 | 2023_4차 | 3302A50 | 고부천2 | Geum | River | -1.18411 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A206:M206 | 2023_4차 | 3004A50 | 영동 | Geum | River | -3.22274 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A207:M207 | 2023_4차 | 3203A40 | 웅천천2 | Geum | River | -2.09239 | 1.30302758260973 | 0.524376874568266 | 1.14100448758586 | 0.743057813617741 | Tanytarsus sp. | 깔따구류 | 8497 |
| A208:M208 | 2023_4차 | 3302A60 | 원평천2 | Geum | River | -2.99778 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A209:M209 | 2023_4차 | 3012A32 | 금강 | Geum | River | -0.96793 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A210:M210 | 2023_4차 | 3003A20 | 무주남대천2 | Geum | River | -2.51094 | 0.908627906406704 | 0.564562260766247 | 0.468635076784291 | 0.934996072270228 | Pristina sp. | 지렁이류 | 2865 |
| A211:M211 | 2023_4차 | 3011R97 | 미호천10 | Geum | River | -2.40332 | 1.15781837948851 | 0.595000945984374 | 0.689984989771877 | 0.825526932084309 | Tanytarsus sp. | 깔따구류 | 3521 |
| A212:M212 | 2023_4차 | 3012R41 | 부여U | Geum | River | -1.40421 | 0.568510365682891 | 0.517480435588536 | 0.245532848046998 | 0.922273781902552 | Tanytarsus sp. | 깔따구류 | 2869 |
| A213:M213 | 2023_4차 | 3302R40 | 동진강3 | Geum | River | 1.04516 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A214:M214 | 2023_4차 | 3006A20 | 우산 | Geum | River | -1.25589 | 1.02194038774899 | 0.634967263945846 | 0.476626816166453 | 0.841377747564015 | Cladotanytarsus | 깔따구류 | 2664 |
| A215:M215 | 2023_4차 | 3005R30 | 초강2 | Geum | River | -0.69462 | 0.551100687967897 | 0.214858311476881 | 1.13997054908375 | 0.937684346007401 | Pristina sp. | 지렁이류 | 32695 |
| A216:M216 | 2023_4차 | 3301B50 | 경천지1 | Geum | Lake | 1.06726 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A217:M217 | 2023_4차 | 3101B40 | 삽교호3 | Geum | Lake | 2.11909 | 1.0995661137902 | 0.442497956164272 | 1.1226635415726 | 0.848055555555556 | Tanytarsus sp. | 깔따구류 | 12254 |
| A218:M218 | 2023_4차 | 3101E10 | C천안천 | Geum | Industry | 1.13966 | 1.56154250574625 | 0.563207407294361 | 1.6575346465563 | 0.716030534351145 | Pristina sp. | 지렁이류 | 4255 |
| A219:M219 | 2023_4차 | 3302E11 | C정읍천 | Geum | Industry | 3.89437 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A220:M220 | 2023_4차 | 3009F20 | 유등천5 | Geum | Urban | 3.69974 | 1.78016171303284 | 0.657359199732816 | 1.49712891673603 | 0.614435855120299 | Dero sp. | 지렁이류 | 3666 |
| A221:M221 | 2023_4차 | 3301F30 | 전주천6 | Geum | Urban | 1.61163 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A222:M222 | 2023_4차 | 2004R90 | 내성천5 | Nakdong | River | -3.11656 | 0.797474281300397 | 0.383504063622858 | 0.696060656473473 | 0.979535801621691 | Tanytarsus sp. | 깔따구류 | 11759 |
| A223:M223 | 2023_4차 | 2011R57 | 다사D | Nakdong | River | -1.89099 | 0.78680548937017 | 0.488869737248958 | 0.543894877663821 | 0.971849008317338 | Corbicula sp. | 이매패류 | 989 |
| A224:M224 | 2023_4차 | 2014R80 | 덕곡D | Nakdong | River | -1.6606 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A225:M225 | 2023_4차 | 2020R33 | 함안D | Nakdong | River | -2.89466 | 1.11795580803721 | 0.449898513544799 | 1.56315998775435 | 0.818980667838313 | Amphichaeta | 지렁이류 | 832 |
| A226:M226 | 2023_4차 | 2006R20 | 병성천 | Nakdong | River | -3.44611 | 0.560283925231671 | 0.348123976018623 | 0.655944781075882 | 0.925842696629213 | Cladotanytarsus | 깔따구류 | 385 |
| A227:M227 | 2023_4차 | 2401A10 | 왕피천 | Nakdong | River | -2.83651 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A228:M228 | 2023_4차 | 2016R30 | 황강6 | Nakdong | River | -2.45683 | 0.255322660821188 | 0.368352736593302 | 0.191756916380211 | 1 | Nais sp. | 지렁이류 | 171 |
| A229:M229 | 2023_4차 | 2009A05 | 낙단 | Nakdong | River | -1.15574 | 0.652713234724234 | 0.335428249367582 | 0.572044879422369 | 0.993650263179881 | Limnodrilus sp. | 실지렁이류 | 24939 |
| A230:M230 | 2023_4차 | 2007R23 | 도남U | Nakdong | River | -0.87178 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A231:M231 | 2023_4차 | 2009A30 | 선산 | Nakdong | River | -2.26115 | 1.23222350029322 | 0.466918049284235 | 1.41571166343613 | 0.841883417292074 | Tipula sp. | 각다귀류 | 5724 |
| A232:M232 | 2023_4차 | 2011R24 | 칠곡U | Nakdong | River | -2.47393 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A233:M233 | 2023_4차 | 2019R80 | 남강7 | Nakdong | River | 2.23083 | 0.416588427159958 | 0.232502428096243 | 0.504039731946232 | 0.992867683226758 | Tanytarsus sp. | 깔따구류 | 17741 |
| A234:M234 | 2023_4차 | 2201A45 | 태화 | Nakdong | River | -0.64237 | 0.593317817403545 | 0.540061151257326 | 0.417032391424246 | 0.933884297520661 | Corbicula sp. | 이매패류 | 99 |
| A235:M235 | 2023_4차 | 2001A30 | 황지2 | Nakdong | River | 0.16387 | 1.11657222014154 | 0.508173917067324 | 0.865131012357342 | 0.827759036144578 | Tanytarsus sp. | 깔따구류 | 6834 |
| A236:M236 | 2023_4차 | 2004B20 | 영주댐3 | Nakdong | Lake | 0.23398 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A237:M237 | 2023_4차 | 2018B10 | 낙동강하구3 | Nakdong | Lake | 1.23531 | 0.223231037754989 | 0.13870124223517 | 0.368084749705844 | 0.991987943762996 | Limnodrilus sp. | 실지렁이류 | 49856 |
| A238:M238 | 2023_4차 | 2301E21 | C상남리수로-1 | Nakdong | Industry | 3.43847 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A239:M239 | 2023_4차 | 2302E11 | C장림유수지 | Nakdong | Industry | 5.14109 | 0.572581240645901 | 0.413030058192945 | 0.255049159944904 | 0.998768895122331 | Limnodrilus sp. | 실지렁이류 | 96027 |
| A240:M240 | 2023_4차 | 2022F10 | 덕천천 | Nakdong | Urban | 1.5517 | 0.914389435315651 | 0.416156566218734 | 0.711238635914798 | 0.869286412512219 | Ilyodrilus sp. | 실지렁이류 | 48167 |
| A241:M241 | 2023_4차 | 2302F28 | 죽성천 | Nakdong | Urban | 1.55166 | 0.659380390409969 | 0.317094939767963 | 0.662957192258853 | 0.902682211201413 | Limnodrilus sp. | 실지렁이류 | 31692 |
| A242:M242 | 2024_1차 | 4001A01 | 지석천 지류 | Yeongsan-Seomjin | River | 1.71668 | 1.39519212871831 | 0.528670640482718 | 1.3126622616089 | 0.764861756912154 | Einfeldia dissidens | 깔따구류 | 12511 |
| A243:M243 | 2024_1차 | 4001A02 | 평동천 | Yeongsan-Seomjin | River | -0.0941 | 1.78581758015332 | 0.541840404351788 | 2.82044369534326 | 0.721555401249876 | Nais sp. | 지렁이류 | 5088 |
| A244:M244 | 2024_1차 | 4001A03 | 광주천 | Yeongsan-Seomjin | River | -0.75539 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A245:M245 | 2024_1차 | 4001A04 | 풍영정천 | Yeongsan-Seomjin | River | 1.83441 | 1.25266339001997 | 0.544024797967895 | 0.867997080862569 | 0.762960404433699 | Nais simplex | 지렁이류 | 17796 |
| A246:M246 | 2024_1차 | 4001A05 | 와탄천 | Yeongsan-Seomjin | River | 0.56956 | 1.68219734082048 | 0.676966010358577 | 1.26318534757544 | 0.635327164573695 | Craspedacusta sowerbii | 자포동물류 | 2028 |
| A247:M247 | 2024_1차 | 4001A06 | 예전저수지 | Yeongsan-Seomjin | Reservoir | 1.48422 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A248:M248 | 2024_1차 | 4001A07 | 덕림저수지 | Yeongsan-Seomjin | Reservoir | 0.94029 | 2.49862376215147 | 0.766896785590274 | 2.72423535471974 | 0.405025333471203 | Nais elinguis | 지렁이류 | 2675 |
| A249:M249 | 2024_1차 | 4001A08 | 수양저수지 | Yeongsan-Seomjin | Reservoir | 0.99747 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A250:M250 | 2024_1차 | 4001A09 | 화원2저수지 | Yeongsan-Seomjin | Reservoir | 0.91047 | 0.937914525780117 | 0.676562317560349 | 0.478682623408026 | 0.874762808349146 | Bothrioneurum vejdovskyanum | 실지렁이류 | 338 |
| A251:M251 | 2024_1차 | 4001A10 | 금호호1 | Yeongsan-Seomjin | Lake | 1.64948 | 0.798995943931183 | 0.333207189235894 | 0.944763159549155 | 0.883589717639915 | Bothrioneurum vejdovskyanum | 실지렁이류 | 31558 |
| A252:M252 | 2024_1차 | 4001A11 | 삼포천2 | Yeongsan-Seomjin | River | 1.61328 | 1.30649007371019 | 0.594609257144802 | 0.878994685335879 | 0.823909891825583 | Tanytarsus kiseogi | 깔따구류 | 3759 |
| A253:M253 | 2024_1차 | 4001A12 | 함평천 | Yeongsan-Seomjin | River | 1.02236 | 3.10871846522297 | 0.831726391764593 | 4.39284734624057 | 0.211424529136086 | Tubificinae sp. | 실지렁이류 | 1235 |
| A254:M254 | 2024_1차 | 4001A13 | 고막원천 | Yeongsan-Seomjin | River | 1.14996 | 0.371775319534259 | 0.19105472044264 | 0.689245948894751 | 0.953927742790852 | Pristina aequiseta | 지렁이류 | 5562 |
| A255:M255 | 2024_1차 | 4001A14 | 영산천 | Yeongsan-Seomjin | River | 0.37778 | 1.98752105609534 | 0.584359222081973 | 2.89630852055457 | 0.533013581962437 | Bothrioneurum vejdovskyanum | 실지렁이류 | 8227 |
| A256:M256 | 2024_1차 | 4001A15 | 오호저수지 | Yeongsan-Seomjin | Reservoir | 0.4534 | 1.06420242196347 | 0.33485978487877 | 2.17804168520013 | 0.858372883114189 | Einfeldia dissidens | 깔따구류 | 29591 |
| A257:M257 | 2024_1차 | 4001A16 | 영암호3 | Yeongsan-Seomjin | Lake | 0.63519 | 1.02115473937463 | 0.736607439238017 | 0.392639124886547 | 0.841902931283037 | Tanytarsus tamagotoi | 깔따구류 | 1225 |
| A258:M258 | 2024_1차 | 4001A17 | 영산호2 | Yeongsan-Seomjin | Lake | 0.94948 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A259:M259 | 2024_1차 | 4001A18 | 쌍봉천 | Yeongsan-Seomjin | River | 0.4089 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A260:M260 | 2024_1차 | 4001A19 | C남수천 | Yeongsan-Seomjin | Industry | 1.73814 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A261:M261 | 2024_1차 | 4001A20 | 금사천 | Yeongsan-Seomjin | River | 1.73503 | 1.59644489821036 | 0.820410386874947 | 0.816197912653726 | 0.635430038510911 | Lumbriculus variegatus | 지렁이류 | 527 |
| A262:M262 | 2024_2차 | 4001A01 | 지석천 지류 | Yeongsan-Seomjin | River | 1.43766 | 0.690912820857858 | 0.314447975862111 | 0.715743597138702 | 0.963892502902869 | Limnodrilus hoffmeisteri | 실지렁이류 | 53983 |
| A263:M263 | 2024_2차 | 4001A02 | 평동천 | Yeongsan-Seomjin | River | 2.34123 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A264:M264 | 2024_2차 | 4001A03 | 광주천 | Yeongsan-Seomjin | River | -0.15768 | 0.914808573296415 | 0.368146052236796 | 1.03993798196594 | 0.836204260523902 | Polypedilum scalaenum | 깔따구류 | 31106 |
| A265:M265 | 2024_2차 | 4001A04 | 풍영정천 | Yeongsan-Seomjin | River | 3.99686 | 1.08850166892981 | 0.438045295996401 | 0.987268961149837 | 0.818432151190597 | Tanytarsus formosanus | 깔따구류 | 48320 |
| A266:M266 | 2024_2차 | 4001A05 | 와탄천 | Yeongsan-Seomjin | River | 0.37864 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A267:M267 | 2024_2차 | 4001A06 | 예전저수지 | Yeongsan-Seomjin | Reservoir | 0.82215 | 2.33325855165875 | 0.754845197652896 | 2.18272710186427 | 0.484679665738162 | Limnodrilus hoffmeisteri | 실지렁이류 | 4983 |
| A268:M268 | 2024_2차 | 4001A07 | 덕림저수지 | Yeongsan-Seomjin | Reservoir | 1.75899 | 1.5406121071889 | 0.440614550406619 | 3.04668176170535 | 0.762138720390854 | Heteromastus sp. | 다모류 | 21315 |
| A269:M269 | 2024_2차 | 4001A08 | 수양저수지 | Yeongsan-Seomjin | Reservoir | -2.57525 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A270:M270 | 2024_2차 | 4001A09 | 화원2저수지 | Yeongsan-Seomjin | Reservoir | 0.31993 | 1.43946116170835 | 0.472803597658725 | 1.87381123235959 | 0.753501724816521 | Limnodrilus hoffmeisteri | 실지렁이류 | 17511 |
| A271:M271 | 2024_2차 | 4001A10 | 금호호1 | Yeongsan-Seomjin | Lake | 1.60618 | 1.83630649812705 | 0.58565137476514 | 2.25490824958379 | 0.60274527974053 | Einfeldia dissidens | 깔따구류 | 5979 |
| A272:M272 | 2024_2차 | 4001A11 | 삼포천2 | Yeongsan-Seomjin | River | 1.11361 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A273:M273 | 2024_2차 | 4001A12 | 함평천 | Yeongsan-Seomjin | River | 0.44617 | 3.08819657873197 | 0.80209823056143 | 5.3103483251285 | 0.239750908147379 | Bothrioneurum vejdovskyanum | 실지렁이류 | 734 |
| A274:M274 | 2024_2차 | 4001A13 | 고막원천 | Yeongsan-Seomjin | River | 0.94656 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A275:M275 | 2024_2차 | 4001A14 | 영산천 | Yeongsan-Seomjin | River | 0.59606 | 1.94454839265643 | 0.551432100910355 | 3.71295869530832 | 0.632472732293249 | Heteromastus koreanus | 다모류 | 4184 |
| A276:M276 | 2024_2차 | 4001A15 | 오호저수지 | Yeongsan-Seomjin | Reservoir | -0.99598 | 1.75267982775189 | 0.478408717266571 | 3.73765115952489 | 0.60983669548511 | Hydra oligactis | 자포동물류 | 9958 |
| A277:M277 | 2024_2차 | 4001A16 | 영암호3 | Yeongsan-Seomjin | Lake | 0.82558 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A278:M278 | 2024_2차 | 4001A17 | 영산호2 | Yeongsan-Seomjin | Lake | 1.30443 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A279:M279 | 2024_2차 | 4001A18 | 쌍봉천 | Yeongsan-Seomjin | River | 2.47455 | 3.01791151183993 | 0.829646743561101 | 4.0130179573666 | 0.240962662176884 | Chaetogaster sp. | 지렁이류 | 1221 |
| A280:M280 | 2024_2차 | 4001A19 | C남수천 | Yeongsan-Seomjin | Industry | 1.91485 | 1.40390429530051 | 0.564972650147757 | 1.28057580249081 | 0.726427375860145 | Bothrioneurum vejdovskyanum | 실지렁이류 | 3309 |
| A281:M281 | 2024_2차 | 4001A20 | 금사천 | Yeongsan-Seomjin | River | 1.65459 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A282:M282 | 2024_3차 | 4001A01 | 지석천 지류 | Yeongsan-Seomjin | River | 1.33844 | 0.668829520107738 | 0.415567146107678 | 0.369361099041653 | 0.998989878983541 | Limnodrilus hoffmeisteri | 실지렁이류 | 31618 |
| A283:M283 | 2024_3차 | 4001A02 | 평동천 | Yeongsan-Seomjin | River | -0.29118 | 1.61356333067927 | 0.581969953832815 | 1.66537147988839 | 0.661151960784314 | Radix plicatula | 복족류 | 3800 |
| A284:M284 | 2024_3차 | 4001A03 | 광주천 | Yeongsan-Seomjin | River | 1.01484 | 1.36907389327898 | 0.415394920604418 | 2.41549424684091 | 0.761992385786802 | Polypedilum scalaenum | 깔따구류 | 29691 |
| A285:M285 | 2024_3차 | 4001A04 | 풍영정천 | Yeongsan-Seomjin | River | 1.11875 | 0.0402194378856928 | 0.0156804023318016 | 1.10195158179337 | 0.996289044289044 | Tanytarsus formosanus | 깔따구류 | 53373 |
| A286:M286 | 2024_3차 | 4001A05 | 와탄천 | Yeongsan-Seomjin | River | -0.03819 | 3.22331706832125 | 0.846756726393081 | 4.77739493400122 | 0.261978593578073 | Craspedacusta sowerbii | 자포동물류 | 1681 |
| A287:M287 | 2024_3차 | 4001A06 | 예전저수지 | Yeongsan-Seomjin | Reservoir | 0.33589 | 0.715889340225401 | 0.238969732557611 | 1.75674957344346 | 0.895687282807384 | Lumbriculus variegatus | 지렁이류 | 42551 |
| A288:M288 | 2024_3차 | 4001A07 | 덕림저수지 | Yeongsan-Seomjin | Reservoir | 0.0636 | 0.949983812967272 | 0.382301610021576 | 0.968903622801756 | 0.933070496573735 | Heteromastus sp. | 다모류 | 45686 |
| A289:M289 | 2024_3차 | 4001A08 | 수양저수지 | Yeongsan-Seomjin | Reservoir | 0.53748 | 1.79641887065739 | 0.466584416103814 | 4.51776405925884 | 0.72782319103845 | Bothrioneurum vejdovskyanum | 실지렁이류 | 12802 |
| A290:M290 | 2024_3차 | 4001A09 | 화원2저수지 | Yeongsan-Seomjin | Reservoir | 1.5536 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A291:M291 | 2024_3차 | 4001A10 | 금호호1 | Yeongsan-Seomjin | Lake | 1.46096 | 1.22077937045505 | 0.509104540262255 | 1.00520476088371 | 0.82213722208941 | Bothrioneurum vejdovskyanum | 실지렁이류 | 8883 |
| A292:M292 | 2024_3차 | 4001A11 | 삼포천2 | Yeongsan-Seomjin | River | 0.86742 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A293:M293 | 2024_3차 | 4001A12 | 함평천 | Yeongsan-Seomjin | River | -0.00438 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A294:M294 | 2024_3차 | 4001A13 | 고막원천 | Yeongsan-Seomjin | River | 0.91201 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A295:M295 | 2024_3차 | 4001A14 | 영산천 | Yeongsan-Seomjin | River | -0.2321 | 1.21610517512261 | 0.321364755144002 | 4.33321880276268 | 0.807754521837165 | Heteromastus koreanus | 다모류 | 15973 |
| A296:M296 | 2024_3차 | 4001A15 | 오호저수지 | Yeongsan-Seomjin | Reservoir | 0.80891 | 0.912114769927718 | 0.279953266971522 | 2.67237912673261 | 0.862841813776393 | Limnodrilus hoffmeisteri | 실지렁이류 | 9379 |
| A297:M297 | 2024_3차 | 4001A16 | 영암호3 | Yeongsan-Seomjin | Lake | 1.3703 | 0.951419542827915 | 0.530997357160789 | 0.74152284017301 | 0.824292452830189 | Culicoides arakawai | 등에모기류 | 598 |
| A298:M298 | 2024_3차 | 4001A17 | 영산호2 | Yeongsan-Seomjin | Lake | -0.09836 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A299:M299 | 2024_3차 | 4001A18 | 쌍봉천 | Yeongsan-Seomjin | River | 0.32462 | 0.53194630352725 | 0.330516821691332 | 0.348595703173476 | 0.973566359451793 | Limnodrilus hoffmeisteri | 실지렁이류 | 79952 |
| A300:M300 | 2024_3차 | 4001A19 | C남수천 | Yeongsan-Seomjin | Industry | 0.82659 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A301:M301 | 2024_3차 | 4001A20 | 금사천 | Yeongsan-Seomjin | River | 2.05226 | 2.66565167506143 | 0.708723703357084 | 4.76360429892005 | 0.409070698088039 | Chaetogaster aff. | 지렁이류 | 1758 |
| A302:M302 | 2024_4차 | 4001A01 | 지석천 지류 | Yeongsan-Seomjin | River | 2.99624 | 1.0400701172516 | 0.451696712714836 | 0.884375071598252 | 0.895902294258646 | Bothrioneurum vejdovskyanum | 실지렁이류 | 16947 |
| A303:M303 | 2024_4차 | 4001A02 | 평동천 | Yeongsan-Seomjin | River | -1.56473 | 0.86440741750422 | 0.247220233993052 | 2.84198518187797 | 0.884532151690025 | Nais stolci | 지렁이류 | 64920 |
| A304:M304 | 2024_4차 | 4001A03 | 광주천 | Yeongsan-Seomjin | River | -0.50284 | 1.24499812164892 | 0.439429711236111 | 1.46299169340314 | 0.824168001423741 | Polypedilum scalaenum | 깔따구류 | 32328 |
| A305:M305 | 2024_4차 | 4001A04 | 풍영정천 | Yeongsan-Seomjin | River | 1.99544 | 2.28003877699096 | 0.7488986609985 | 2.25913373462218 | 0.428877769835597 | Chaetogaster aff. | 지렁이류 | 1968 |
| A306:M306 | 2024_4차 | 4001A05 | 와탄천 | Yeongsan-Seomjin | River | -0.08734 | 2.47696159409034 | 0.702413033721205 | 3.58881852008977 | 0.470659898477157 | Einfeldia dissidens | 깔따구류 | 3118 |
| A307:M307 | 2024_4차 | 4001A06 | 예전저수지 | Yeongsan-Seomjin | Reservoir | 2.93687 | 2.28944162545624 | 0.666700686148741 | 3.11906432003439 | 0.575181219658176 | Chaetogaster aff. | 지렁이류 | 5008 |
| A308:M308 | 2024_4차 | 4001A07 | 덕림저수지 | Yeongsan-Seomjin | Reservoir | -0.21497 | 0.597757394200255 | 0.259602737818038 | 0.808251811670119 | 0.986401704164113 | Nais stolci | 지렁이류 | 53643 |
| A309:M309 | 2024_4차 | 4001A08 | 수양저수지 | Yeongsan-Seomjin | Reservoir | 0.337 | 1.43380826210955 | 0.517137017332769 | 1.72252547396651 | 0.766688697951091 | Branchiura sowerbyi | 실지렁이류 | 3806 |
| A310:M310 | 2024_4차 | 4001A09 | 화원2저수지 | Yeongsan-Seomjin | Reservoir | 2.15383 | 3.12339460807606 | 0.830425000532074 | 4.57047188213423 | 0.234555294598182 | Aulodrilus pluriseta | 실지렁이류 | 1210 |
| A311:M311 | 2024_4차 | 4001A10 | 금호호1 | Yeongsan-Seomjin | Lake | 1.75389 | 1.51631438837187 | 0.483596614743726 | 2.19829467868191 | 0.66132083971529 | Limnodrilus hoffmeisteri | 실지렁이류 | 9231 |
| A312:M312 | 2024_4차 | 4001A11 | 삼포천2 | Yeongsan-Seomjin | River | 1.66922 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A313:M313 | 2024_4차 | 4001A12 | 함평천 | Yeongsan-Seomjin | River | 0.53394 | 2.77591579972708 | 0.780771882729306 | 4.06660949810416 | 0.336295603367633 | Limnodrilus hoffmeisteri | 실지렁이류 | 828 |
| A314:M314 | 2024_4차 | 4001A13 | 고막원천 | Yeongsan-Seomjin | River | 0.97731 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A315:M315 | 2024_4차 | 4001A14 | 영산천 | Yeongsan-Seomjin | River | 0.79438 | 1.47919685174976 | 0.409645660060591 | 3.58397009728525 | 0.817747677346531 | Aulodrilus pluriseta | 실지렁이류 | 12828 |
| A316:M316 | 2024_4차 | 4001A15 | 오호저수지 | Yeongsan-Seomjin | Reservoir | 0.39776 | 2.10654664478191 | 0.613440446729255 | 3.34962665565811 | 0.549381124290872 | Tubificinae sp. | 실지렁이류 | 2323 |
| A317:M317 | 2024_4차 | 4001A16 | 영암호3 | Yeongsan-Seomjin | Lake | 1.44844 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A318:M318 | 2024_4차 | 4001A17 | 영산호2 | Yeongsan-Seomjin | Lake | 0.16784 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 | 빈칸 |
| A319:M319 | 2024_4차 | 4001A18 | 쌍봉천 | Yeongsan-Seomjin | River | 0.74519 | 0.0240290078069822 | 0.0149300619932837 | 0.350022194241055 | 0.999814903532076 | Limnodrilus hoffmeisteri | 실지렁이류 | 91525 |
| A320:M320 | 2024_4차 | 4001A19 | C남수천 | Yeongsan-Seomjin | Industry | 1.02426 | 1.992843461285 | 0.665227490079006 | 2.22699198647865 | 0.571456731716933 | Pristina aequiseta | 지렁이류 | 2224 |
| A321:M321 | 2024_4차 | 4001A20 | 금사천 | Yeongsan-Seomjin | River | 1.86775 | 2.38059839668704 | 0.730671534408458 | 3.13647149157467 | 0.414507772020725 | Procladius culiciformis | 깔따구류 | 743 |

## 부록 D. Excel 기술통계 및 시료별 극값

**[재계산]** 빈값을 제외한 산술평균. 지수 0은 포함. 같은 지점의 조사차수도 각각 한 행으로 집계했으며 독립 표본이라고 가정한 가설검정은 하지 않았다.

### D.1 유형별

근거: 'Sheet1'!E2:E321의 그룹과 F2:J321. 개별 소속 행은 부록 C 참조.

| 구분 | PC1 행수 | 지점수 | 지수 유효행 | 누락행 | 누락률 | PC1 평균 | 다양도 평균 | 균등도 평균 | 풍부도 평균 | 우점도 평균 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| River | 212 | 53 | 165 | 47 | 22.17% | -0.3942 | 1.2743 | 0.5013 | 1.4558 | 0.7636 |
| Industry | 28 | 7 | 20 | 8 | 28.57% | 1.1005 | 1.3130 | 0.4835 | 1.5584 | 0.7557 |
| Lake | 36 | 9 | 24 | 12 | 33.33% | 0.5885 | 1.0383 | 0.4218 | 1.1844 | 0.8181 |
| Urban | 24 | 6 | 16 | 8 | 33.33% | 0.7725 | 1.2049 | 0.5014 | 1.2000 | 0.7782 |
| Reservoir | 20 | 5 | 16 | 4 | 20.00% | 0.6513 | 1.5933 | 0.5113 | 2.4817 | 0.7050 |

### D.2 조사차수별

근거: 'Sheet1'!A2:A321의 그룹과 F2:J321. 개별 소속 행은 부록 C 참조.

| 구분 | PC1 행수 | 지점수 | 지수 유효행 | 누락행 | 누락률 | PC1 평균 | 다양도 평균 | 균등도 평균 | 풍부도 평균 | 우점도 평균 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2022_1차 | 20 | 20 | 20 | 0 | 0.00% | 0.1279 | 1.1246 | 0.4997 | 1.3442 | 0.8061 |
| 2022_2차 | 20 | 20 | 20 | 0 | 0.00% | -0.3457 | 1.2018 | 0.4776 | 1.3573 | 0.7701 |
| 2022_3차 | 20 | 20 | 17 | 3 | 15.00% | -0.4646 | 1.2228 | 0.4971 | 1.3699 | 0.7807 |
| 2022_4차 | 20 | 20 | 14 | 6 | 30.00% | 0.3902 | 1.1203 | 0.4699 | 1.0505 | 0.8044 |
| 2023_1차 | 40 | 40 | 27 | 13 | 32.50% | -0.3423 | 1.3390 | 0.5550 | 1.2759 | 0.7465 |
| 2023_2차 | 40 | 40 | 32 | 8 | 20.00% | -0.1565 | 1.3126 | 0.4956 | 1.3312 | 0.7351 |
| 2023_3차 | 40 | 40 | 29 | 11 | 27.50% | -0.6941 | 1.2212 | 0.4422 | 1.5528 | 0.7821 |
| 2023_4차 | 40 | 40 | 26 | 14 | 35.00% | -0.4835 | 0.8571 | 0.4267 | 0.7766 | 0.8894 |
| 2024_1차 | 20 | 20 | 14 | 6 | 30.00% | 0.9668 | 1.4863 | 0.5830 | 1.6183 | 0.7076 |
| 2024_2차 | 20 | 20 | 12 | 8 | 40.00% | 1.0105 | 1.7543 | 0.5501 | 2.5130 | 0.6393 |
| 2024_3차 | 20 | 20 | 14 | 6 | 30.00% | 0.6961 | 1.2768 | 0.4317 | 2.2455 | 0.7812 |
| 2024_4차 | 20 | 20 | 16 | 4 | 20.00% | 0.9715 | 1.7266 | 0.5351 | 2.5106 | 0.6511 |

### D.3 수계별

근거: 'Sheet1'!D2:D321의 그룹과 F2:J321. 개별 소속 행은 부록 C 참조.

| 구분 | PC1 행수 | 지점수 | 지수 유효행 | 누락행 | 누락률 | PC1 평균 | 다양도 평균 | 균등도 평균 | 풍부도 평균 | 우점도 평균 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Han | 80 | 20 | 71 | 9 | 11.25% | -0.0730 | 1.1690 | 0.4870 | 1.2961 | 0.7895 |
| Geum | 80 | 20 | 59 | 21 | 26.25% | -0.3584 | 1.3062 | 0.5118 | 1.3105 | 0.7509 |
| Nakdong | 80 | 20 | 55 | 25 | 31.25% | -0.4797 | 1.0689 | 0.4467 | 1.1809 | 0.8215 |
| Yeongsan-Seomjin | 80 | 20 | 56 | 24 | 30.00% | 0.9112 | 1.5600 | 0.5244 | 2.2218 | 0.6952 |

### D.4 전체 평균과 최솟값·최댓값

| 항목 | 유효행 | 평균 | 최소 | Sheet1 최소 셀(차수·지점) | 최대 | Sheet1 최대 셀(차수·지점) |
| --- | --- | --- | --- | --- | --- | --- |
| PC1 | 320 | -9.37500000033301e-08 | -4.00635 | F65 (2022_4차, 섬강4-1) | 5.14109 | F239 (2023_4차, C장림유수지) |
| 다양도지수 | 241 | 1.27060087698001 | 0 | G204 (2023_4차, 현도) | 3.22331706832125 | G286 (2024_3차, 와탄천) |
| 균등도지수 | 241 | 0.492559528376615 | 0 | H204 (2023_4차, 현도) | 0.859975650555104 | H24 (2022_2차, 원주) |
| 풍부도지수 | 241 | 1.48843416522445 | 0 | I204 (2023_4차, 현도) | 5.3103483251285 | I273 (2024_2차, 함평천) |
| 우점도지수 | 241 | 0.76544935872534 | 0.211424529136086 | J253 (2024_1차, 함평천) | 1 | J152 (2023_2차, 칠곡U), J204 (2023_4차, 현도), J228 (2023_4차, 황강6) |
| 우점종 ASV count | 241 | 15744.8340248963 | 85 | M54 (2022_3차, 행주) | 175643 | M38 (2022_2차, 공촌천) |

### D.5 지점별 기록 범위 및 지수 평균

80개 지점 각각의 유효행 수와 평균을 제시한다. 유효 차수가 다르므로 완전한 연평균으로 간주하지 않았다. 행이 비연속이므로 실제 행번호를 모두 표시했다.

| 코드 | 지점 | 유형 | Sheet1 행번호(A:M) | 유효차수 | 다양도 평균 | 균등도 평균 | 풍부도 평균 | 우점도 평균 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1001R85 | 영월1 | River | 2, 22, 42, 62 | 4 | 0.8339 | 0.2647 | 1.8895 | 0.8469 |
| 1004R70 | 달천5 | River | 3, 23, 43, 63 | 4 | 1.0360 | 0.3649 | 1.4020 | 0.8174 |
| 1005R60 | 원주 | River | 4, 24, 44, 64 | 4 | 1.7202 | 0.7620 | 1.1616 | 0.6322 |
| 1006R80 | 섬강4-1 | River | 5, 25, 45, 65 | 4 | 1.0611 | 0.4569 | 1.1253 | 0.7846 |
| 1007R18 | 강천U | River | 6, 26, 46, 66 | 3 | 0.8499 | 0.4087 | 0.7805 | 0.8640 |
| 1007R30 | 대신D | River | 7, 27, 47, 67 | 4 | 1.1802 | 0.4602 | 1.3235 | 0.7815 |
| 1007R75 | 강상 | River | 8, 28, 48, 68 | 3 | 1.8081 | 0.6997 | 1.7875 | 0.5881 |
| 1013R60 | 춘성교 | River | 9, 29, 49, 69 | 3 | 1.3348 | 0.4797 | 1.8022 | 0.8011 |
| 1014R70 | 홍천강6 | River | 10, 30, 50, 70 | 4 | 1.1823 | 0.5550 | 0.8678 | 0.7769 |
| 1015R60 | 삼봉리 | River | 11, 31, 51, 71 | 3 | 1.1014 | 0.6206 | 0.6180 | 0.7909 |
| 1016R80 | 경안천6 | River | 12, 32, 52, 72 | 3 | 1.5638 | 0.5312 | 2.0239 | 0.6805 |
| 1018R22 | 탄천 | River | 13, 33, 53, 73 | 4 | 1.0994 | 0.5589 | 0.9774 | 0.8613 |
| 1019R25 | 행주 | River | 14, 34, 54, 74 | 4 | 1.2432 | 0.6697 | 1.0101 | 0.8250 |
| 1022E30 | C신천-1 | Industry | 15, 35, 55, 75 | 4 | 1.9694 | 0.6602 | 2.2564 | 0.5950 |
| 1101B20 | 원천지2 | Lake | 16, 36, 56, 76 | 4 | 1.0763 | 0.4554 | 1.0583 | 0.8136 |
| 1101B40 | 서호2 | Lake | 17, 37, 57, 77 | 3 | 1.1594 | 0.4340 | 1.3338 | 0.7950 |
| 1201F10 | 공촌천 | Urban | 18, 38, 58, 78 | 3 | 0.6186 | 0.2104 | 1.6013 | 0.9362 |
| 1201F50 | 장만수천 | Urban | 19, 39, 59, 79 | 3 | 1.5950 | 0.6735 | 1.0625 | 0.6864 |
| 1202E52 | C옥구천 | Industry | 20, 40, 60, 80 | 3 | 0.5669 | 0.3019 | 0.6490 | 0.9467 |
| 1202R10 | 반월천 | River | 21, 41, 61, 81 | 4 | 0.3995 | 0.1660 | 1.1901 | 0.9629 |
| 3009A80 | 갑천6 | River | 82, 122, 162, 202 | 4 | 1.4709 | 0.6060 | 1.0736 | 0.6962 |
| 3010R20 | 부강 | River | 83, 123, 163, 203 | 4 | 1.5661 | 0.5584 | 1.4089 | 0.7156 |
| 3008A60 | 현도 | River | 84, 124, 164, 204 | 4 | 1.1578 | 0.5115 | 0.8333 | 0.7231 |
| 3302A50 | 고부천2 | River | 85, 125, 165, 205 | 2 | 1.6830 | 0.5260 | 2.0323 | 0.6213 |
| 3004A50 | 영동 | River | 86, 126, 166, 206 | 2 | 1.4010 | 0.6051 | 0.9236 | 0.7167 |
| 3203A40 | 웅천천2 | River | 87, 127, 167, 207 | 3 | 1.2812 | 0.5241 | 1.1666 | 0.7638 |
| 3302A60 | 원평천2 | River | 88, 128, 168, 208 | 1 | 1.2070 | 0.3798 | 1.9753 | 0.8072 |
| 3012A32 | 금강 | River | 89, 129, 169, 209 | 3 | 1.1300 | 0.4227 | 1.3965 | 0.7963 |
| 3003A20 | 무주남대천2 | River | 90, 130, 170, 210 | 4 | 1.0693 | 0.5145 | 0.8150 | 0.8483 |
| 3011R97 | 미호천10 | River | 91, 131, 171, 211 | 4 | 1.1999 | 0.4965 | 1.1228 | 0.8013 |
| 3012R41 | 부여U | River | 92, 132, 172, 212 | 3 | 1.3712 | 0.5601 | 1.4963 | 0.7222 |
| 3302R40 | 동진강3 | River | 93, 133, 173, 213 | 2 | 1.4782 | 0.5617 | 1.2653 | 0.6536 |
| 3006A20 | 우산 | River | 94, 134, 174, 214 | 3 | 1.1533 | 0.5916 | 0.7936 | 0.7907 |
| 3005R30 | 초강2 | River | 95, 135, 175, 215 | 3 | 1.0724 | 0.3890 | 1.3441 | 0.8231 |
| 3301B50 | 경천지1 | Lake | 96, 136, 176, 216 | 2 | 1.5155 | 0.5009 | 1.8191 | 0.6757 |
| 3101B40 | 삽교호3 | Lake | 97, 137, 177, 217 | 3 | 0.9397 | 0.3560 | 1.1879 | 0.8636 |
| 3101E10 | C천안천 | Industry | 98, 138, 178, 218 | 4 | 1.7847 | 0.5689 | 2.4268 | 0.6377 |
| 3302E11 | C정읍천 | Industry | 99, 139, 179, 219 | 3 | 1.0092 | 0.3737 | 1.3837 | 0.8436 |
| 3009F20 | 유등천5 | Urban | 100, 140, 180, 220 | 4 | 1.3379 | 0.5624 | 1.0626 | 0.7350 |
| 3301F30 | 전주천6 | Urban | 101, 141, 181, 221 | 1 | 1.4877 | 0.5053 | 1.9836 | 0.7199 |
| 2004R90 | 내성천5 | River | 102, 142, 182, 222 | 3 | 1.0627 | 0.4103 | 1.5275 | 0.8955 |
| 2011R57 | 다사D | River | 103, 143, 183, 223 | 3 | 1.1545 | 0.5220 | 0.8748 | 0.8085 |
| 2014R80 | 덕곡D | River | 104, 144, 184, 224 | 2 | 1.2900 | 0.5989 | 0.9509 | 0.7742 |
| 2020R33 | 함안D | River | 105, 145, 185, 225 | 3 | 0.9690 | 0.4090 | 1.2404 | 0.8525 |
| 2006R20 | 병성천 | River | 106, 146, 186, 226 | 4 | 0.9963 | 0.3989 | 1.1192 | 0.8268 |
| 2401A10 | 왕피천 | River | 107, 147, 187, 227 | 3 | 1.0872 | 0.4582 | 0.9827 | 0.8004 |
| 2016R30 | 황강6 | River | 108, 148, 188, 228 | 3 | 1.4566 | 0.5163 | 2.0399 | 0.7369 |
| 2009A05 | 낙단 | River | 109, 149, 189, 229 | 3 | 0.8691 | 0.3735 | 0.8182 | 0.8944 |
| 2007R23 | 도남U | River | 110, 150, 190, 230 | 3 | 1.4990 | 0.5005 | 2.0751 | 0.7057 |
| 2009A30 | 선산 | River | 111, 151, 191, 231 | 3 | 1.2174 | 0.4660 | 1.4691 | 0.8076 |
| 2011R24 | 칠곡U | River | 112, 152, 192, 232 | 1 | 0.0234 | 0.0337 | 0.1294 | 1.0000 |
| 2019R80 | 남강7 | River | 113, 153, 193, 233 | 3 | 1.2364 | 0.5062 | 1.3831 | 0.7486 |
| 2201A45 | 태화 | River | 114, 154, 194, 234 | 3 | 1.2463 | 0.6534 | 1.0579 | 0.7788 |
| 2001A30 | 황지2 | River | 115, 155, 195, 235 | 3 | 1.3153 | 0.4775 | 1.5942 | 0.7968 |
| 2004B20 | 영주댐3 | Lake | 116, 156, 196, 236 | 2 | 0.5144 | 0.2092 | 1.1948 | 0.9364 |
| 2018B10 | 낙동강하구3 | Lake | 117, 157, 197, 237 | 4 | 0.7280 | 0.3329 | 0.7655 | 0.8858 |
| 2301E21 | C상남리수로-1 | Industry | 118, 158, 198, 238 | 2 | 1.1691 | 0.4666 | 1.1527 | 0.7614 |
| 2302E11 | C장림유수지 | Industry | 119, 159, 199, 239 | 2 | 0.3901 | 0.2814 | 0.2619 | 0.9955 |
| 2022F10 | 덕천천 | Urban | 120, 160, 200, 240 | 3 | 1.2145 | 0.6129 | 0.7352 | 0.7746 |
| 2302F28 | 죽성천 | Urban | 121, 161, 201, 241 | 2 | 1.0776 | 0.3881 | 1.3844 | 0.7994 |
| 4001A01 | 지석천 지류 | River | 242, 262, 282, 302 | 4 | 0.9488 | 0.4276 | 0.8205 | 0.9059 |
| 4001A02 | 평동천 | River | 243, 263, 283, 303 | 3 | 1.4213 | 0.4570 | 2.4426 | 0.7557 |
| 4001A03 | 광주천 | River | 244, 264, 284, 304 | 3 | 1.1763 | 0.4077 | 1.6395 | 0.8075 |
| 4001A04 | 풍영정천 | River | 245, 265, 285, 305 | 4 | 1.1654 | 0.4367 | 1.3041 | 0.7516 |
| 4001A05 | 와탄천 | River | 246, 266, 286, 306 | 3 | 2.4608 | 0.7420 | 3.2098 | 0.4560 |
| 4001A06 | 예전저수지 | Reservoir | 247, 267, 287, 307 | 3 | 1.7795 | 0.5535 | 2.3528 | 0.6518 |
| 4001A07 | 덕림저수지 | Reservoir | 248, 268, 288, 308 | 4 | 1.3967 | 0.4624 | 1.8870 | 0.7717 |
| 4001A08 | 수양저수지 | Reservoir | 249, 269, 289, 309 | 2 | 1.6151 | 0.4919 | 3.1201 | 0.7473 |
| 4001A09 | 화원2저수지 | Reservoir | 250, 270, 290, 310 | 3 | 1.8336 | 0.6599 | 2.3077 | 0.6209 |
| 4001A10 | 금호호1 | Lake | 251, 271, 291, 311 | 4 | 1.3431 | 0.4779 | 1.6008 | 0.7424 |
| 4001A11 | 삼포천2 | River | 252, 272, 292, 312 | 1 | 1.3065 | 0.5946 | 0.8790 | 0.8239 |
| 4001A12 | 함평천 | River | 253, 273, 293, 313 | 3 | 2.9909 | 0.8049 | 4.5899 | 0.2625 |
| 4001A13 | 고막원천 | River | 254, 274, 294, 314 | 1 | 0.3718 | 0.1911 | 0.6892 | 0.9539 |
| 4001A14 | 영산천 | River | 255, 275, 295, 315 | 4 | 1.6568 | 0.4667 | 3.6316 | 0.6977 |
| 4001A15 | 오호저수지 | Reservoir | 256, 276, 296, 316 | 4 | 1.4589 | 0.4267 | 2.9844 | 0.7201 |
| 4001A16 | 영암호3 | Lake | 257, 277, 297, 317 | 2 | 0.9863 | 0.6338 | 0.5671 | 0.8331 |
| 4001A17 | 영산호2 | Lake | 258, 278, 298, 318 | 0 | 첨부 자료에서 확인되지 않음 | 첨부 자료에서 확인되지 않음 | 첨부 자료에서 확인되지 않음 | 첨부 자료에서 확인되지 않음 |
| 4001A18 | 쌍봉천 | River | 259, 279, 299, 319 | 3 | 1.1913 | 0.3917 | 1.5705 | 0.7381 |
| 4001A19 | C남수천 | Industry | 260, 280, 300, 320 | 2 | 1.6984 | 0.6151 | 1.7538 | 0.6489 |
| 4001A20 | 금사천 | River | 261, 281, 301, 321 | 3 | 2.2142 | 0.7533 | 2.9054 | 0.4863 |

## 부록 E. PDF 직접 관련 위치 색인

핵심 방법·결과 외에 eDNA/DNA가 등장하는 요약·계획·성과 문단도 포함한 위치 색인이다. 참고문헌의 richness와 성과논문의 metabarcoding을 퇴적물 eDNA 지수 결과로 혼동하지 않았다.

| PDF 파일 쪽 | 내용 |
| --- | --- |
| 6~7 | 연구목표·DNA 종다양성 스크리닝·eDNA 핵심어 |
| 14, 16~19 | 과제 개요·최종/연차별 목표와 DNA 분류기술 |
| 44~45 | 깔따구 동정 및 eDNA 접목의 필요성 |
| 47~50 | eDNA 종다양성 조사 역할·연차별 추진방법·일정 |
| 58~67 | 하천유형·지점선정·조사시기·수중 환경인자 |
| 77~79 | eDNA 시료채취·실험·분석방법·그림 32 |
| 80 | 일반 저서동물 군집지수 정의 |
| 86~89 | 환경변수 변환·상관분석·PCA |
| 100~113 | 현장 군집지수·환경 상관·CCA 비교 자료 |
| 129~136 | 출현개체 기반 KBSI 비교 자료 |
| 137~143 | eDNA 표 37 및 e-KBSI 그림 78~80 |
| 144, 146 | 목표 달성·eDNA 277지표분류군 성과 |
| 148~149 | 3종 DB 구축 및 eDNA metabarcoding 논문 성과 |
| 152~154 | 목표 달성·DB 후속 활용·KBSI/e-KBSI 병행 평가 |
| 10~11 | 목차에 eDNA 표·그림 위치 안내 |
| 29, 218 | 참고문헌 제목의 expected richness: eDNA 지수값이 아님 |

