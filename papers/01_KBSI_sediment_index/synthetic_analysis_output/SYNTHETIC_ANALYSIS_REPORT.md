# Synthetic KBSI analysis

> WARNING: Every observation in this folder is simulated. It is not the paper's field data and must not be reported as an empirical result.

- random seed: 20260916
- synthetic sample units: 320
- indicator taxa used: 137
- samples with at least one detected synthetic taxon: 320

## PCA

- synthetic PC1 explained variance: 87.84%
- PC1 correlations:
  - TAN: 0.786
  - AVS: 0.806
  - TOC: 0.706
  - Metals_TierII: 0.646
  - mud_fraction: 0.906
  - PC1: 1.000

## KBSI summary

- mean KBSI: 78.10
- median KBSI: 78.25
- minimum KBSI: 27.33
- maximum KBSI: 100.00

## Files

- synthetic_environment.csv: simulated sediment variables and PC1
- synthetic_pca_loadings.csv: PCA loadings and reported loading references
- synthetic_taxon_frequencies.csv: simulated long-format taxon frequencies
- synthetic_biological_data.csv: simulated sample-by-taxon abundance matrix
- synthetic_kbsi_scores.csv: calculated KBSI and classes
- indicator_values_used.csv: 137 indicator values parsed from Table 3
