# Datasets

This directory contains external datasets used in the study of trace impurities and their effects on Coulombic efficiency (CE).

## Contents

### A. Severson et al. Battery Cycling Dataset (`severson2019_cycle_life/`)
- **Source:** https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation
- **Reference:** Severson et al., "Data-driven prediction of battery cycle life before capacity degradation," Nature Energy, 2019.
- **Contents:** Jupyter notebooks and MATLAB scripts for loading and processing battery cycling data from 124 LFP/graphite cells.

### B. F-GCN Electrolyte-to-CE Dataset (`fgcn_electrolyte_ce/`)
- **Source:** https://figshare.com/articles/dataset/24545935
- **Reference:** Sharma et al., "Formulation Graphs for Mapping Structure-Composition of Battery Electrolytes to Device Performance," J. Chem. Inf. Model., 2023.
- **Contents:** `ci3c01030_si_002.xlsx` - Supporting Information with electrolyte formulation data and CE measurements.

### C. Baakes et al. KITopen Data (`baakes_kitopen/`)
- **Source:** https://doi.org/10.35097/1804 (RADAR/KIT repository)
- **Reference:** Baakes et al., "Impact of electrolyte impurities and SEI composition on battery safety."
- **Contents:** `DataSources.xlsx` (~12.4 MB) containing experimental data on electrolyte impurities and SEI composition, plus metadata files.

### D. Open-Source Battery Data List (`open_battery_data_list/`)
- **Source:** https://github.com/lappemic/open-source-battery-data
- **Contents:** Curated list of open-source battery datasets with links and descriptions.

## Notes
- Large binary files are excluded from version control via `.gitignore`.
- To reproduce the full dataset directory, re-run the download commands documented in the project setup instructions.
