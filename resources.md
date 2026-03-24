# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project on trace impurities and their effects on Coulombic Efficiency (CE) in lithium batteries. Resources include papers, datasets, and code repositories.

---

## Papers
Total papers downloaded: 18

| # | Title | Authors | Year | File | Key Info |
|---|-------|---------|------|------|----------|
| 1 | Re-evaluation of battery-grade lithium purity toward sustainable batteries | Choe et al. | 2024 | papers/choe2024_lithium_purity_reevaluation.pdf | **CRITICAL**: 1% Mg impurity beneficial for NCM622 cathode |
| 2 | Impact of electrolyte impurities and SEI composition on battery safety | Baakes, Witt, Krewer | 2023 | papers/baakes2023_electrolyte_impurities_SEI_safety.pdf | Thermal-runaway model; water impurity dual role; data at KITopen |
| 3 | Moving beyond 99.9% CE for lithium anodes in liquid electrolytes | Hobold et al. | 2021 | papers/hobold2021_beyond_999_CE_lithium.pdf | Perspective on CE determinants; warns about trace impurity effects |
| 4 | Understanding and applying CE in lithium metal batteries | Xiao et al. | 2020 | papers/xiao2020_understanding_CE_lithium_metal.pdf | Proper CE measurement protocols; CE ≠ cycle life predictor |
| 5 | High lithium oxide prevalence in the lithium SEI for high CE | Hobold et al. | 2024 | papers/li2o_SEI_high_CE_2024.pdf | **CRITICAL**: Li₂O > LiF as CE correlator; challenges fluorination paradigm |
| 6 | Influence of metallic contaminants on Li-ion electrodes | Fink et al. | 2021 | papers/metallic_impurities_recycled_electrodes.pdf | Fe, Al, Mg, Cu, Si at 1 wt% in anode/cathode; electrochemical+thermal |
| 7 | Advancing Li metal electrode beyond 99.9% CE via super-saturated electrolyte | Chen et al. | 2025 | papers/chen2025_supersaturated_electrolyte_999CE.pdf | 16M super-saturated electrolyte, >99.9% CE |
| 8 | Deciphering coulombic loss in lithium-ion batteries and beyond | — | 2025 | papers/coulombic_loss_2025.pdf | Physical mechanisms of coulombic loss |
| 9 | A path towards high Li-metal electrode CE based on electrolyte descriptor | — | 2025 | papers/path_high_CE_electrolyte_descriptor_2025.pdf | ML-based electrolyte interaction motif descriptor |
| 10 | SEI growth on lithium metal anodes — coulometric titration | Otto et al. | 2023 | papers/otto2023_SEI_growth_lithium_metal_coulometric.pdf | Quantitative SEI growth in solid-state batteries |
| 11 | Autonomous discovery of battery electrolytes | Dave et al. | 2020 | papers/dave2020_autonomous_electrolyte_discovery.pdf | Bayesian optimization + robotic electrolyte discovery |
| 12 | Autonomous optimization of non-aqueous Li-ion battery electrolytes | Jiang et al. | 2022 | papers/jiang2022_autonomous_electrolyte_optimization.pdf | Closed-loop robotic optimization of electrolytes |
| 13 | Formulation Graphs for battery electrolytes | Sharma et al. | 2023 | papers/formulation_graphs_electrolyte_2023.pdf | GNN mapping electrolyte composition to performance |
| 14 | Electrochemical Removal of HF from LiPF₆ electrolyte | — | 2024 | papers/HF_removal_electrolyte_2024.pdf | HF impurity management in electrolytes |
| 15 | Four parameter model for SEI to predict battery aging | Single et al. | 2021 | papers/single_2021_four_param_SEI_model.pdf | Physics-based SEI growth model |
| 16 | Modeling battery formation: SEI growth, multi-species reactions | — | 2023 | papers/modeling_battery_formation_SEI_2023.pdf | Formation cycling SEI model |
| 17 | Predictive ML MD of SEI formation in concentrated electrolyte | — | 2026 | papers/predictive_ML_MD_SEI_2026.pdf | ML molecular dynamics for SEI prediction |
| 18 | Morphological stability of metal anodes: SEI roles | — | 2026 | papers/morphological_stability_anodes_SEI_2026.pdf | Theoretical analysis of SEI on metal anodes |

See papers/README.md for detailed descriptions.

---

## Datasets
Total datasets downloaded: 4

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Baakes et al. KITopen | KITopen (DOI:10.35097/1804) | 12.4 MB | Impurity+SEI thermal modeling | datasets/baakes_kitopen/ | **Most directly relevant**: reaction network data for impurity effects |
| F-GCN Electrolyte-to-CE | Figshare | 35 KB | Electrolyte→CE mapping | datasets/fgcn_electrolyte_ce/ | Electrolyte composition to CE; extendable for impurity features |
| Severson et al. Cycle Life | GitHub/data.matr.io | Scripts | Cycle life prediction | datasets/severson2019_cycle_life/ | 124 LFP/graphite cells; CE across fast-charging protocols |
| Open Battery Data List | GitHub | Index | Meta-resource | datasets/open_battery_data_list/ | Curated list of all public battery datasets |

See datasets/README.md for download instructions and detailed descriptions.

---

## Code Repositories
Total repositories cloned: 2

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| PyBaMM | github.com/pybamm-team/PyBaMM | Battery simulation framework | code/pybamm/ | **Primary tool**: Built-in SEI submodels; extensible for impurity-modified kinetics |
| BatteryML (Microsoft) | github.com/microsoft/BatteryML | ML platform for battery data | code/batteryml/ | Unified ML framework integrating multiple datasets; ICLR 2024 |

See code/README.md for detailed descriptions (if applicable).

---

## Resource Gathering Notes

### Search Strategy
1. **Paper-finder service** (unavailable — service not running)
2. **arXiv API**: Searched 6 queries; mostly returned irrelevant physics papers (this is a materials science domain)
3. **Semantic Scholar API**: Rate-limited (429 errors)
4. **Web search**: Most productive method — found key Nature Energy/Communications, Chemical Science, and J. Power Sources papers
5. **Citation following**: Key papers (Hobold 2021, 2024; Choe 2024; Baakes 2023) led to additional relevant work

### Selection Criteria
- Papers directly studying impurity effects on battery performance/CE/SEI
- Papers establishing CE measurement methodology and baselines
- Papers on electrolyte design strategies (fluorination, oxygenation) relevant to impurity roles
- Papers providing computational/ML frameworks applicable to impurity studies
- Datasets with CE measurements and electrolyte composition data

### Challenges Encountered
- Most battery materials papers are in journals (Nature Energy, J. Electrochem. Soc., etc.) rather than arXiv — fewer open-access PDFs
- Semantic Scholar API rate-limited; paper-finder service unavailable
- No single dataset specifically tracking impurity concentration vs. CE exists
- The research topic spans electrochemistry, materials science, and manufacturing — literature is scattered

### Gaps and Workarounds
- **Missing: Systematic impurity dose-response dataset** — No existing public dataset maps trace impurity concentration to CE. The Baakes model data + F-GCN electrolyte data can be combined/extended.
- **Missing: Code for impurity-modified SEI modeling** — PyBaMM provides extensible SEI submodels that can be modified to include impurity reactions.
- **Paywalled papers**: Breddemann 2025 (electrolyte impurities changes over time), Adenusi 2023 (SEI progress), data-driven electrolyte design (PNAS) — could not download.

---

## Recommendations for Experiment Design

### 1. Primary dataset(s)
- **Baakes et al. KITopen data**: Use as basis for extending impurity-SEI reaction models
- **F-GCN electrolyte dataset**: Add impurity concentration features to graph-based CE prediction
- **Generate synthetic data**: Use PyBaMM with modified SEI kinetics to simulate impurity dose-response

### 2. Baseline methods
- **PyBaMM SPM/DFN models** with standard SEI submodels (reaction-limited, solvent-diffusion-limited)
- **Conventional electrolyte baseline**: 1M LiPF₆ EC/DEC (~92% CE, well-characterized by Hobold)
- **High-CE baseline**: LiFSI-based LHCE (~99% CE)

### 3. Evaluation metrics
- Coulombic Efficiency (Li/Cu half-cell protocol per Xiao et al.)
- SEI composition (Li₂O:LiF ratio as key descriptor per Hobold 2024)
- Capacity retention at 200 cycles
- Impedance growth rate

### 4. Code to adapt/reuse
- **PyBaMM**: Extend SEI submodels with impurity-dependent reaction rates
- **BatteryML**: Use for data-driven analysis of impurity effects on degradation trajectories
- **Baakes reaction network**: Implement in Python/PyBaMM for extended parameter studies beyond water
