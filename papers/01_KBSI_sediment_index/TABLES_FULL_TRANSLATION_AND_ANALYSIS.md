# KBSI 논문 표 전체 번역 및 분석

## 표 1. PCA 적재량과 설명된 분산

| 변수 | PC1 | PC2 | PC3 |
|---|---:|---:|---:|
| TAN | 0.66 | 0.03 | 0.00 |
| AVS | 0.69 | -0.01 | -0.06 |
| TOC | 0.86 | 0.08 | -0.02 |
| Metals Tier II Index | 0.82 | -0.01 | -0.03 |
| 머드 함량 | 0.76 | -0.03 | 0.01 |
| 설명된 분산(%) | 58.0 | 17.2 | 10.8 |
| 누적 설명 분산(%) | 58.0 | 75.2 | 86.0 |
| 고유값 | 2.9 | 0.9 | 0.5 |

TAN은 총 암모니아성 질소, AVS는 산휘발성 황화물, TOC는 총유기탄소다. 머드 함량은 실트-점토 분획이며 화학 오염물질이 아니라 물리적 퇴적 변수로 취급했다.

**해석:** PC1이 전체 변동의 58.0%를 설명하며 주요 환경 구배가 된다. TOC와 Metals Tier II Index의 기여가 특히 크고, 머드 함량도 0.76으로 높다. 따라서 PC1은 단일 오염물질 축이 아니라 유기물, 금속, 미세 입자 및 환원 상태가 함께 변하는 복합 구배다.

## 표 2. PC1 구간과 대표 클래스 값

| 구간 번호 | 누적확률 | PC1 구간 | 대표 클래스 값 |
|---:|---:|---|---:|
| 1 | 1/9 | < -2.277 | -3.142 |
| 2 | 2/9 | -2.277 ~ < -1.367 | -1.822 |
| 3 | 3/9 | -1.367 ~ < -0.730 | -1.049 |
| 4 | 4/9 | -0.730 ~ < -0.199 | -0.465 |
| 5 | 5/9 | -0.199 ~ < 0.288 | 0.045 |
| 6 | 6/9 | 0.288 ~ < 0.773 | 0.531 |
| 7 | 7/9 | 0.773 ~ < 1.301 | 1.037 |
| 8 | 8/9 | 1.301 ~ < 1.976 | 1.639 |
| 9 | 1 | ≥ 1.976 | 3.559 |

**해석:** 구간은 동일한 수치 폭이 아니라 동일한 누적확률을 기준으로 나누었다. 따라서 구간 폭은 PC1 분포의 비대칭성을 반영한다. 대표값은 분류군 내성값 계산을 위한 내부 척도이며 규제 또는 독성 기준이 아니다.

## 표 3. 분류군별 내성값과 지시자 가중치 전체

| 번호 | 분류군 | 내성값(t) | 지시자 가중치(g) |
|---:|---|---:|---:|
| 1 | Anodonta woodiana | 3.0 | 4 |
| 2 | Corbicula fluminea | 3.1 | 2 |
| 3 | Musculium lacustre | 3.9 | 4 |
| 4 | Hediste sp. | 6.5 | 2 |
| 5 | Branchiura sowerbyi | 5.1 | 1 |
| 6 | Bothrioneurum vejdoskynum | 3.7 | 1 |
| 7 | Rhyacodrilus coccineus | 0.0 | 5 |
| 8 | Tubifex tubifex | 4.6 | 1 |
| 9 | Limnodrilus claparedeianus | 0.7 | 4 |
| 10 | Limnodrilus hoffmeisteri | 4.9 | 1 |
| 11 | Limnodrilus udekimineanus | 7.3 | 5 |
| 12 | Haplotaxis gordioides | 3.8 | 1 |
| 13 | Chaetogaster diaphanus | 1.9 | 4 |
| 14 | Chaetogaster limnaei | 0.0 | 5 |
| 15 | Branchiodrilus hortensis | 7.1 | 3 |
| 16 | Opidonais sp. | 0.0 | 4 |
| 17 | Amphichaeta asiatica | 3.8 | 2 |
| 18 | Haemonais waldvogeli | 4.8 | 2 |
| 19 | Nais variabilis | 5.6 | 3 |
| 20 | Nais communis | 7.3 | 5 |
| 21 | Slavina appendiculata | 7.3 | 5 |
| 22 | Stylaria fossularis | 3.1 | 3 |
| 23 | Pristina biserrata | 0.0 | 5 |
| 24 | Pristina longiseta | 1.8 | 3 |
| 25 | Henlea sp. | 5.7 | 3 |
| 26 | Mesenchytreanus sp. | 6.9 | 2 |
| 27 | Lumbriculus variegatus | 3.3 | 1 |
| 28 | Lamprotus orientalis | 0.9 | 3 |
| 29 | Eisenia koreana | 4.2 | 1 |
| 30 | Helobdella stagnalis | 5.6 | 1 |
| 31 | Erpobdella lineata | 4.3 | 1 |
| 32 | Erpobdella sp. | 7.9 | 2 |
| 33 | Cyprididae sp. | 7.3 | 5 |
| 34 | Gnorimosphaeroma sp. | 4.6 | 5 |
| 35 | Cyathura higoensis | 7.9 | 4 |
| 36 | Asellus sp. | 6.4 | 2 |
| 37 | Gammarus sp. | 4.9 | 2 |
| 38 | Jesogammarus sp. | 10.0 | 5 |
| 39 | Monocorophium sp. | 9.0 | 5 |
| 40 | Collembola sp. | 4.2 | 2 |
| 41 | Baetis fuscatus | 3.3 | 4 |
| 42 | Cloeon dipterum | 5.1 | 2 |
| 43 | Labiobaetis atrebatinus | 4.6 | 2 |
| 44 | Procloeon maritimum | 0.0 | 5 |
| 45 | Procloeon pennulatum | 3.3 | 2 |
| 46 | Choroterpes altioculus | 0.8 | 3 |
| 47 | Potamanthus formosus | 0.0 | 4 |
| 48 | Rhoenanthus coreanus | 0.2 | 3 |
| 49 | Ephoron shigae | 0.0 | 5 |
| 50 | Ephemera orientalis | 2.7 | 2 |
| 51 | Serratella setigera | 5.6 | 2 |
| 52 | Caenis sp. | 2.6 | 2 |
| 53 | Psychoda sp. | 4.0 | 4 |
| 54 | Dixidae sp. | 3.3 | 5 |
| 55 | Ceratopogonidae sp. | 4.3 | 2 |
| 56 | Benthalia sp. | 4.6 | 5 |
| 57 | Chironomus circumdatus | 0.0 | 5 |
| 58 | Chironomus flaviplumus | 5.0 | 1 |
| 59 | Chironomus kiiensis | 8.5 | 3 |
| 60 | Chironomus nipponensis | 4.5 | 2 |
| 61 | Chironomus edwardsi | 6.9 | 3 |
| 62 | Chironomus sp. | 6.0 | 2 |
| 63 | Cladotanytarsus vanderwulpi | 3.3 | 3 |
| 64 | Cryptochironomus sp. | 1.6 | 2 |
| 65 | Demicryptochironomus sp. | 1.7 | 3 |
| 66 | Dicrotendipes nervosus | 3.8 | 3 |
| 67 | Dicrotendipes pelochloris | 9.0 | 5 |
| 68 | Dicrotendipes septemmaculatus | 6.9 | 3 |
| 69 | Dicrotendipes sp. | 6.6 | 2 |
| 70 | Glyptotendipes tokunagai | 5.2 | 2 |
| 71 | Harnischia japonica | 4.9 | 3 |
| 72 | Harnischiagumsanea | 7.3 | 5 |
| 73 | Harnischia sp. | 6.2 | 2 |
| 74 | Lipiniella moderata | 4.5 | 2 |
| 75 | Microchironomus tener | 3.1 | 3 |
| 76 | Microchironomus sp. | 7.3 | 5 |
| 77 | Microtendipes sp. | 3.8 | 3 |
| 78 | Nilothauma sp. | 3.9 | 4 |
| 79 | Parachironomus gracilior | 1.7 | 5 |
| 80 | Parachironomus arcuatus | 7.4 | 3 |
| 81 | Paratanytarsus inopertus | 7.3 | 5 |
| 82 | Paratanytarsus grimmii | 7.9 | 4 |
| 83 | Paratanytarsus sp. | 4.6 | 5 |
| 84 | Paratendipes albimanus | 2.2 | 2 |
| 85 | Paratendipes sp. | 0.0 | 4 |
| 86 | Polypedilum asakawaense | 6.6 | 2 |
| 87 | Polypedilum pedestre | 0.0 | 5 |
| 88 | Polypedilum nubifer | 1.3 | 3 |
| 89 | Polypedilum decematoguttatum | 4.6 | 5 |
| 90 | Polypedilum masudai | 4.0 | 2 |
| 91 | Polypedilum cultellatum | 3.8 | 2 |
| 92 | Polypedilum nubeculosum | 5.5 | 2 |
| 93 | Polypedilum sp. | 4.7 | 1 |
| 94 | Stictochironomus sinsauensis | 3.0 | 1 |
| 95 | Stictochironomus sp. | 4.8 | 3 |
| 96 | Tanytarsus kiseogi | 0.8 | 4 |
| 97 | Tanytarsus takahashii | 1.7 | 5 |
| 98 | Tanytarsus tamagotoi | 3.3 | 5 |
| 99 | Tanytarsus tamakutibasi | 2.3 | 4 |
| 100 | Tanytarsus formosanus | 10.0 | 5 |
| 101 | Tanytarsus sp. | 4.3 | 1 |
| 102 | Potthastia sp. | 4.6 | 5 |
| 103 | Thienemanniella sp. | 1.2 | 4 |
| 104 | Brillia japonica | 4.6 | 5 |
| 105 | Corynoneura sp. | 1.7 | 3 |
| 106 | Cricotopus bicinctus | 2.7 | 3 |
| 107 | Cricotopus bimaculatus | 0.0 | 4 |
| 108 | Cricotopus sylvestris | 5.8 | 1 |
| 109 | Cricotopus triannulatus | 2.3 | 4 |
| 110 | Cricotopus sp. | 4.3 | 1 |
| 111 | Eukiefferiella sp. | 0.0 | 4 |
| 112 | Hydrobaenus kondoi | 3.9 | 1 |
| 113 | Hydrobaenus sp. | 3.3 | 5 |
| 114 | Limnophyes tamakitanaides | 6.0 | 5 |
| 115 | Orthocladius glabripennis | 5.6 | 4 |
| 116 | Orthocladius sp. | 1.8 | 2 |
| 117 | Paratrichocladius rufiventris | 6.1 | 2 |
| 118 | Propsilocerus akamusi | 2.3 | 4 |
| 119 | Rheocricotopus sp. | 0.0 | 5 |
| 120 | Ablabesmyia longistyla | 8.3 | 3 |
| 121 | Ablabesmyia monilis | 3.7 | 2 |
| 122 | Ablabesmyia prorasha | 0.8 | 3 |
| 123 | Ablabesmyia sp. | 4.5 | 1 |
| 124 | Conchapelopia sp. | 3.4 | 1 |
| 125 | Hayesomyia tripunctata | 9.0 | 5 |
| 126 | Procladius choreus | 2.9 | 2 |
| 127 | Procladius nigriventris | 10.0 | 5 |
| 128 | Procladius sp. | 5.1 | 1 |
| 129 | Rheopelopia sp. | 3.3 | 5 |
| 130 | Tanypus punctipennis | 9.3 | 3 |
| 131 | Saetheria tylus | 0.0 | 4 |
| 132 | Cladopelma edwardsi | 7.0 | 2 |
| 133 | Cladopelma virescens | 3.3 | 4 |
| 134 | Chironomidae sp. | 1.8 | 2 |
| 135 | Syrphidae sp. | 7.3 | 5 |
| 136 | Ephydridae sp. | 10.0 | 4 |
| 137 | Ecnomus sp. | 7.6 | 2 |

**주석 번역:** 내성값은 9개 PC1 구간에 따른 각 분류군의 가중평균 위치를 나타낸다. 지시자 가중치는 PC1 구배에서 각 분류군의 출현 분포가 집중되는 정도를 나타내며 민감도 값으로 해석해서는 안 된다.

**표 분석:** 내성값 범위는 0.0~10.0이다. 내성값 0.0 분류군은 낮은 PC1 구간에 집중되고, 10.0 분류군은 높은 PC1 구간에 집중된 것으로 해석된다. 그러나 이 값은 실험실 독성시험에서 얻은 생리적 내성이 아니라 본 연구의 현장 분포 위치다. 동일한 내성값이라도 가중치가 다를 수 있으며, 가중치가 높다는 것은 환경 위치가 좁은 범위에 특이적으로 나타났다는 뜻이다.

## 표 4. KBSI 분류 기준

| 등급 | 생태 상태 | KBSI 범위 |
|---|---|---:|
| A | 높음 | 70~100 |
| B | 양호 | 60~<70 |
| C | 보통 | 50~<60 |
| D | 나쁨 | 40~<50 |
| E | 매우 나쁨 | 0~<40 |

**주석 번역:** KBSI 등급은 퇴적물 연관 생태 상태를 위한 경험적 생물학적 평가 범주다. 독립적인 화학적 퇴적물 품질 기준 또는 독성 임계값으로 해석해서는 안 된다.

**표 분석:** 등급 경계는 실무적 해석을 쉽게 하지만, 독립적인 외부 자료로 검증된 생태 임계값인지 확인이 필요하다. 현재 논문에서 이 등급은 지수 개발 자료에 기반한 해석 범주다.

# 그림 전체 번역 및 분석

## Figure 1. 조사 지점 분포

**캡션 번역:** KBSI 개발에 사용한 한국 주요 하천 유역의 80개 담수 퇴적물 모니터링 지점 분포. 지점 범주는 기준지점 또는 손상지점이 아니라 수체 유형, 주변 토지 이용 환경 및 퇴적성 서식처 환경의 대략적인 차이를 나타낸다.

**그림 해석:** 이 그림은 연구가 단일 하천이나 단일 수체에 한정되지 않고 여러 하천 유역과 수체 유형을 포함했다는 점을 보여준다. 다만 지점이 한국 전체 담수 환경을 무작위로 대표한다고 단정할 수는 없다. 지점별 표본 수와 유역별 공간 의존성을 함께 확인해야 하며, 일반 하천을 자동으로 청정 기준지점으로 해석해서는 안 된다.

## Figure 2. 퇴적물 변수의 PCA 이중도표

**캡션 번역:** 퇴적물 물리·화학 변수의 PCA 이중도표. 왼쪽 패널은 PC1-PC2 배열을, 오른쪽 패널은 PC2-PC3 배열을 나타낸다. 환경 벡터는 공극수 TAN, AVS, TOC, Metals Tier II Index 및 머드 함량을 나타낸다. PC1은 전체 분산의 58.0%를 설명했으며, 분류군별 내성값과 지시자 가중치를 도출하기 위한 주요 현장 기반 퇴적물 상태 구배로 사용했다. 지점 기호는 기술적 수체 유형을 나타내며 기준지점 또는 손상지점으로 사용되지 않았다.

**그림 해석:** 환경 벡터가 PC1 방향으로 함께 향한다면 다섯 변수가 공통적인 퇴적물 상태 구배를 형성한다는 해석을 지지한다. TOC와 Metals Tier II Index의 벡터가 길고 PC1 방향성이 강하면 해당 변수들이 PC1에 크게 기여한다는 뜻이다. 그러나 PCA 도표는 공변 구조를 보여줄 뿐 특정 변수가 생물 반응을 직접 일으킨다는 인과관계를 보여주지는 않는다.

## Figure 3. PC1 점수의 확률분포

**캡션 번역:** 지시자 분류군이 포함된 309개 표본 단위의 PC1 점수 확률분포. PC1의 경험적 분포를 Weibull 누적분포함수로 적합했다. 세로 점선은 동일한 누적확률 구간으로부터 도출한 9개 구간 경계를 나타낸다. 이 PC1 구간은 분류군별 내성값과 지시자 가중치를 도출하기 위한 퇴적물 상태 구배의 경험적 구간으로 사용했다.

**그림 해석:** 세로 경계선은 동일한 수치 폭이 아니라 동일한 누적확률을 기준으로 정해졌다. 따라서 PC1 분포가 비대칭이면 각 구간의 수치 폭이 달라진다. 이 그림은 9개 구간이 규제 기준이나 독성 임계값이 아니라, 연구 자료 안에서 생물 출현 분포를 계산하기 위한 내부 구분임을 보여준다. Weibull 적합도와 매개변수의 불확실성이 함께 제시되어야 경계값의 안정성을 평가할 수 있다.

## Figure 4. KBSI와 퇴적물 환경 변수의 관계

**캡션 번역:** KBSI와 퇴적물 환경 변수의 관계. 산점도는 KBSI와 (a) 공극수 TAN, (b) AVS, (c) TOC, (d) Metals Tier II Index, (e) 머드 함량의 관계를 나타낸다. 회귀선은 현장 수준의 관계를 요약한다. KBSI는 다섯 퇴적물 변수 모두와 유의한 음의 관계를 보였다.

**그림 해석:** 모든 패널에서 회귀선이 하향하면 각 퇴적물 변수의 값이 증가할수록 KBSI가 감소하는 방향성이 나타난다. 이는 KBSI가 유기물 축적, 환원성 조건, 상대적 금속 오염 및 미세 입자 축적이 함께 강해지는 환경을 낮은 점수로 표현한다는 뜻이다. 다만 다섯 변수가 서로 상관되어 있을 가능성이 있으므로 각 회귀선은 독립적인 인과효과가 아니라 공통 환경 구배를 반영할 수 있다.

## Figure 5. PC1 점수와 KBSI의 관계

**캡션 번역:** PC1 점수와 KBSI의 관계. 산점도는 지점 수준 연간 평균 PC1 점수와 KBSI의 관계를 절삭 전(a)과 95% 예측구간 밖의 네 지점을 절삭한 후(b)로 나누어 보여준다. 높은 PC1 점수는 더 강한 퇴적물 연관 환경 스트레스를 나타낸다. KBSI는 PC1 점수와 유의한 음의 관계를 보였으며, 이는 KBSI가 PCA로 도출한 퇴적물 상태 구배와 내부적으로 일치함을 지지한다.

**그림 해석:** 네 지점을 제외한 뒤에도 음의 관계가 유지되면 관계가 소수의 극단값에만 의존하지 않을 가능성을 보여준다. 그러나 PC1은 KBSI의 내성값과 가중치를 만드는 과정에 이미 사용되었기 때문에, 이 그림은 독립적인 검증이 아니라 개발 자료 내부의 일관성 확인이다. 절삭 전후의 표본 수, 회귀계수, 신뢰구간 및 절삭 기준을 함께 보고해야 한다.

## Figure 6. 관찰 KBSI와 계산 KBSI

**캡션 번역:** 관찰 KBSI와 계산 KBSI의 관계. 산점도는 PC1-KBSI 분석에서 95% 예측구간 밖의 네 지점을 제외한 뒤 76개 지점의 관찰 KBSI와 계산 KBSI 사이의 관계를 보여준다. 이 관계는 지수 개발 틀 안에서의 내부 일치성을 나타내며 외부 검증으로 해석해서는 안 된다.

**그림 해석:** 관찰값과 계산값의 양의 관계는 퇴적물 변수 기반 계산식이 개발 자료 안에서 KBSI 변동을 재현한다는 의미다. 하지만 같은 개발 자료와 같은 환경 변수 체계에서 두 값이 산출되었으므로 새로운 지역 또는 새로운 시기의 예측 성능을 증명하지 않는다. 외부 검증에는 지수 개발에 사용하지 않은 지점·연도의 관찰 KBSI가 필요하다.

## 그림과 표의 종합 해석

Figure 1은 공간적 조사 범위를, Figure 2와 Figure 3은 PC1 환경 구배를 만드는 통계적 구조를, Table 1과 Table 2는 그 구배의 수치적 근거를 보여준다. Table 3은 137개 분류군의 출현 위치와 특이성을 KBSI 계산에 연결하는 핵심 자료이며, Figure 4와 Figure 5는 개발된 점수가 퇴적물 변수 및 PC1과 의도한 방향으로 변하는지 보여준다. Figure 6과 Table 4는 지수의 내부 계산 일치성과 실무적 등급 체계를 제시한다.

전체 그림과 표는 KBSI 개발 자료 내부의 논리적 일관성을 지지한다. 그러나 같은 PC1과 같은 개발 자료를 이용해 점수를 만들고 평가했다는 점에서, 그림과 표만으로 독립적인 공간·시간 검증이나 직접적인 독성 기준을 확립할 수는 없다.
