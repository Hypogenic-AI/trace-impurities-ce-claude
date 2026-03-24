# Literature Review: Decoding the Role of Trace Impurities on Coulombic Efficiency

## Research Area Overview

This review examines how trace impurities — often considered mere contaminants — influence battery performance, particularly Coulombic Efficiency (CE) and solid-electrolyte interphase (SEI) formation in lithium-ion and lithium-metal batteries. The central hypothesis is that certain trace elements or compounds may catalyze favorable SEI formation or lithium kinetics, and their controlled introduction could improve CE. The literature reveals a nuanced picture: while most impurities are detrimental at high concentrations, several studies demonstrate beneficial effects at trace levels, challenging the conventional wisdom that ultra-high purity is always necessary.

---

## Key Papers

### Paper 1: Re-evaluation of battery-grade lithium purity toward sustainable batteries
- **Authors**: Choe, Kim, Kwon, Jung, Park, Kim
- **Year**: 2024
- **Source**: Nature Communications 15, 1185
- **DOI**: 10.1038/s41467-024-44812-3
- **Key Contribution**: Demonstrates that ~1% Mg impurity in Li₂CO₃ precursor is *beneficial* for cathode performance
- **Methodology**: Synthesized NCM622 cathodes from Li₂CO₃ with controlled Mg levels (0-2.52%); compared lithium-carbonate doping (LCD), solid-state doping (SSD), and coprecipitation doping (CPD) at 1.5 mol% Mg
- **Datasets Used**: Pilot plant data from Hombre Muerto Salt Lake brine (Argentina) and Western Australian spodumene
- **Results**:
  - LCD: 82.6% capacity retention at 200 cycles (half-cell); 89.1% (full-cell at 40°C)
  - Bare (no Mg): 76.1% (half-cell); 80.8% (full-cell)
  - Neutron diffraction: >80% of Mg²⁺ occupies Li site (3a) in LCD vs ~65% in SSD/CPD
  - Economic: 19.4% CAPEX reduction, 9.0% CO₂ reduction for brine processing
- **Code Available**: No (experimental study)
- **Relevance**: **CRITICAL** — directly supports hypothesis that trace impurities can be beneficial. The Mg "impurity" outperforms intentional doping strategies.

### Paper 2: Impact of electrolyte impurities and SEI composition on battery safety
- **Authors**: Baakes, Witt, Krewer
- **Year**: 2023
- **Source**: Chemical Science 14, 13783-13798
- **DOI**: 10.1039/d3sc04186g
- **Key Contribution**: First mechanistic model linking water impurity levels and SEI composition to thermal runaway behavior
- **Methodology**: Zero-dimensional thermal-runaway model with 12 degradation reactions, 20 species; parameterized from Stich et al. (2018) and Maleki et al. (1999) ARC data
- **Key Findings**:
  - SEI thickness and LEDC content are dominant safety factors (more than water impurities)
  - Water at 168-260 ppm: no safety difference; >500 ppm: detrimental
  - Thick inorganic SEI delays self-heating by ~19°C
  - Water plays dual role: endothermic heat sink (PFD reaction) + exothermic LiOH decomposition
  - H₂O-HF regeneration cycle in thermal abuse
- **Data Available**: KITopen repository at https://doi.org/10.35097/1804
- **Relevance**: Shows that moderate water "impurity" is tolerable and that SEI composition (controlled by impurities) dominates safety behavior

### Paper 3: Moving beyond 99.9% Coulombic efficiency for lithium anodes in liquid electrolytes
- **Authors**: Hobold, Lopez, Guo, Minafra, Banerjee, Meng, Shao-Horn, Gallant
- **Year**: 2021
- **Source**: Nature Energy 6, 951-960
- **DOI**: 10.1038/s41560-021-00910-w
- **Key Contribution**: Comprehensive perspective on CE determinants; explicitly warns about trace impurity effects at high CE
- **Key Findings**:
  - CE > 99.95% needed for 1,000+ cycles; current best is ~99.9% (liquefied gas electrolyte)
  - Two regimes: Li⁰-dominated (CE < ~95%) and SEI-dominated (CE > ~95%)
  - Fluorination is dominant strategy but not monotonically beneficial
  - **"When approaching high CE, the role of minor electrolyte impurities can become substantial... and may become an inadvertent differentiator across suppliers"**
  - LiF is not necessarily the most beneficial SEI phase
- **Relevance**: **CRITICAL** — explicitly identifies trace impurities as an under-studied variable at high CE

### Paper 4: Understanding and applying coulombic efficiency in lithium metal batteries
- **Authors**: Xiao, Li, Bi, Cai, Dunn, Glossmann, Liu, Osaka, Sugiura, Wu, Yang, Zhang, Whittingham
- **Year**: 2020
- **Source**: Nature Energy 5, 561-568
- **DOI**: 10.1038/s41560-020-0648-z
- **Key Contribution**: Establishes proper CE measurement protocols; shows CE alone is insufficient for cycle life prediction
- **Key Findings**:
  - CE does NOT predict cycle life in Li metal cells the same way as in Li-ion cells
  - Testing conditions (electrolyte volume, Li thickness) profoundly affect measured CE
  - Compatible electrolyte (1.2M LiFSI in TEP/BTFE): 99.69% CE in Li/NMC, 97.79% anode-free
  - Carbonate electrolyte with *higher* CE (99.76%) died sooner (50 vs 180+ cycles)
- **Relevance**: Provides methodological framework for properly measuring CE effects of impurities

### Paper 5: High lithium oxide prevalence in the lithium SEI for high Coulombic efficiency
- **Authors**: Hobold, Wang, Steinberg, Li, Gallant
- **Year**: 2024
- **Source**: Nature Energy 9, 580-591
- **DOI**: 10.1038/s41560-024-01494-x
- **Key Contribution**: Demonstrates Li₂O (not LiF) is the strongest CE correlator across diverse electrolytes
- **Methodology**: Novel quantitative titration (2-butoxyethanol/Karl Fischer) to measure Li₂O in cycled anodes; tested 10 electrolytes from 40% to >99% CE
- **Key Findings**:
  - Li₂O is most abundant identifiable SEI phase (14.6% of capacity loss in 1M LiPF₆ EC/DEC)
  - Li₂O prevalence correlates more strongly with high CE than LiF
  - Fluorine-free electrolytes achieving >99% CE when Li₂O-rich SEI forms
  - Challenges the LiF-centric electrolyte design paradigm
- **Relevance**: **CRITICAL** — suggests that impurities promoting Li₂O formation (e.g., trace water, oxygen-containing species) could be beneficial

### Paper 6: Influence of metallic contaminants on electrochemical and thermal behavior of Li-ion electrodes
- **Authors**: Fink, Polzin, Vaughey, Major, Dunlop, Trask, Jeka, Spangenberger, Keyser
- **Year**: 2021
- **Source**: Journal of Power Sources (230760)
- **DOI**: 10.1016/j.jpowsour.2021.230760
- **Key Contribution**: Systematic study of metallic impurities (Fe, Al, Mg, Cu, Si) at 1 wt% in both anode and cathode
- **Methodology**: Half-cell and full-cell testing with isothermal microcalorimetry; impurities added at 1 wt% to graphite anodes or NMC-111 cathodes
- **Key Findings**:
  - At anode: metallic contaminants disrupt performance through direct reaction with Li; may catalyze electrolyte degradation
  - At cathode: metallic contaminants cross over during formation cycling to disrupt SEI formation
  - Each impurity has distinct electrochemical/thermal signature
  - Low-level doping can increase capacity retention, thermal stability (from literature refs)
- **Relevance**: Provides quantitative framework for studying individual impurity effects on CE and SEI

### Paper 7: Advancing lithium metal electrode beyond 99.9% CE via super-saturated electrolyte
- **Authors**: Chen et al.
- **Year**: 2025
- **Source**: Nature Communications
- **DOI**: 10.1038/s41467-025-59563-y
- **Key Contribution**: Super-saturated electrolyte (16M Li salt in solvent phase) achieving >99.9% CE

### Paper 8: Deciphering coulombic loss in lithium-ion batteries and beyond
- **Year**: 2025
- **Source**: Nature Communications
- **DOI**: 10.1038/s41467-025-60833-y
- **Key Contribution**: Resolves physical mechanisms of coulombic loss; shows it arises from synergy between local charge neutrality and global charge compensation

### Paper 9: A path towards high lithium-metal electrode CE based on electrolyte interaction motif descriptor
- **Year**: 2025
- **Source**: Nature Communications
- **DOI**: 10.1038/s41467-025-59955-0
- **Key Contribution**: Develops ML-based electrolyte descriptor for CE prediction

### Paper 10: SEI growth on lithium metal anodes quantified with coulometric titration time analysis
- **Authors**: Otto et al.
- **Year**: 2023
- **Source**: Nature Communications
- **DOI**: 10.1038/s41467-023-42512-y
- **Key Contribution**: Quantitative measurement of SEI growth on Li metal in solid-state batteries

---

## Common Methodologies

- **Electrochemical cycling**: Half-cell (Li/Cu) and full-cell (Li/NMC, graphite/NMC) testing with controlled protocols — Used in [Papers 1, 4, 5, 6]
- **Titration-based analysis**: Quantifying inactive Li⁰ and SEI phases (Li₂O, LiF, ROCO₂Li) — Used in [Papers 3, 5]
- **Thermal analysis**: ARC and isothermal microcalorimetry for impurity detection — Used in [Papers 2, 6]
- **Structural characterization**: Neutron diffraction, XRD, XPS, cryo-TEM for SEI/electrode analysis — Used in [Papers 1, 5]
- **Computational modeling**: Thermal-runaway models, Bayesian optimization, GNNs — Used in [Papers 2, 7, 9]

## Standard Baselines

- **Electrolytes**: 1M LiPF₆ in EC/DEC or EC/EMC (conventional); LiFSI-based ethers (advanced)
- **CE benchmarks**: 92-93% (conventional carbonate), 99%+ (advanced fluorinated), 99.9% (liquefied gas)
- **SEI composition baselines**: Li₂O, LiF, ROCO₂Li, Li₂CO₃ content via titration

## Evaluation Metrics

- **Coulombic Efficiency (CE)**: Primary metric; measured in Li/Cu half-cells or anode-free configurations
- **Capacity retention**: At 200+ cycles, at multiple temperatures (25°C, 40°C)
- **SEI composition**: Quantitative phase analysis via titration, XPS, cryo-TEM
- **Thermal stability**: Self-heating onset temperature, time to thermal runaway

## Datasets in the Literature

- **Baakes et al. KITopen data**: Degradation reaction network parameters (DOI:10.35097/1804) — [Paper 2]
- **Hobold et al. Source Data**: CE and SEI titration data across 10 electrolytes — [Paper 5]
- **Choe et al. Supplementary**: Economic/environmental data, structural characterization — [Paper 1]
- **Severson et al.**: 124 LFP/graphite cells, CE across fast-charging protocols
- **KIT NMC/C-SiO Dataset**: 228 cells, CE and energy efficiency over 600+ days

---

## Gaps and Opportunities

1. **No systematic study of trace impurity effects on CE at high-CE regime (>99%)**: Most impurity studies focus on bulk contamination (1 wt%+); the effect of ppm-level impurities on ultra-high CE is unexplored
2. **Beneficial impurities for SEI formation are understudied**: Choe (Mg), Hobold (Li₂O from water/oxygen), and Baakes (moderate water) all hint at beneficial roles, but no controlled systematic study exists
3. **Water impurity has dual role**: Detrimental at high levels but may promote beneficial LiF/Li₂O formation at trace levels — needs systematic dose-response study
4. **Li₂O vs LiF debate**: Hobold 2024 challenges LiF dominance; trace impurities that promote Li₂O could be key
5. **Cross-electrode effects**: Fink et al. show metallic impurities cross from cathode to anode; how this affects SEI at trace levels is unknown
6. **Machine learning opportunity**: Data-driven approaches (electrolyte descriptors, GNNs) could incorporate impurity features to predict CE effects

---

## Recommendations for Our Experiment

### Recommended datasets
1. **Baakes et al. KITopen data** — directly models impurity effects on SEI, can be extended
2. **F-GCN electrolyte dataset** — maps electrolyte composition to CE; extendable to include impurity features
3. **Severson et al. cycling data** — baseline CE behavior for comparison

### Recommended baselines
1. **1M LiPF₆ in EC/DEC** (conventional, ~92% CE) — well-characterized SEI composition from Hobold
2. **LiFSI-based electrolytes** (advanced, ~99% CE) — for high-CE regime study
3. **Ultra-pure reference** — establish baseline before introducing controlled impurities

### Recommended metrics
1. **Coulombic Efficiency** in Li/Cu half-cells (primary)
2. **SEI composition** via titration (Li₂O, LiF, ROCO₂Li quantification)
3. **Capacity retention** over 200+ cycles at 25°C and 40°C
4. **Impedance growth** (EIS) to track SEI evolution with impurity exposure

### Methodological considerations
- Use multiple cell replicates (n≥3) due to high variability with impurities (noted by Fink et al.)
- Control electrolyte volume precisely (Xiao et al. showed CE sensitivity to volume)
- Start with dose-response studies: 10 ppm → 100 ppm → 1000 ppm of target impurities
- Consider both metallic (Fe⁰, Cu⁰, Mg⁰) and ionic (water, HF) impurity forms
- Simulate experiments using PyBaMM with modified SEI submodels before physical testing
