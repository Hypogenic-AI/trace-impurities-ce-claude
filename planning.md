# Research Plan: Decoding the Role of Trace Impurities on Coulombic Efficiency

## Motivation & Novelty Assessment

### Why This Research Matters
Lithium battery performance is critically sensitive to trace impurities in electrode materials and electrolytes. While the battery industry spends billions pursuing ultra-high purity materials, emerging evidence (Choe 2024, Hobold 2024) suggests some "contaminants" may actually improve performance. Understanding which impurities help vs. hurt — and at what concentrations — could reduce manufacturing costs and unlock new design strategies.

### Gap in Existing Work
Based on the literature review, no systematic computational study exists that:
1. Models the dose-response relationship of multiple trace impurities on CE across concentration ranges (ppm to wt%)
2. Compares impurity effects on SEI growth kinetics and composition simultaneously
3. Quantifies the "sweet spot" where beneficial impurities maximize CE before becoming detrimental

Most prior work studied single impurities at high concentrations (1 wt%, Fink et al.) or focused on a single mechanism (water → thermal runaway, Baakes et al.). The high-CE regime (>99%) where trace impurities become critical (Hobold 2021) remains computationally unexplored.

### Our Novel Contribution
We conduct a systematic computational study using physics-based battery models (PyBaMM) combined with data-driven analysis of existing electrolyte-CE datasets to:
1. Simulate how trace impurities modify SEI growth kinetics and resulting CE
2. Map dose-response curves for multiple impurity types (Mg, Fe, water, oxygen-containing species)
3. Identify impurity concentrations that maximize CE by promoting beneficial SEI phases (Li₂O over LiF)
4. Validate computational predictions against published experimental data

### Experiment Justification
- **Experiment 1 (PyBaMM Simulation)**: Needed to establish a mechanistic understanding of how impurities alter SEI formation kinetics and CE. Uses physics-based models that can be parameterized from literature data.
- **Experiment 2 (F-GCN Dataset Analysis)**: Needed to identify real electrolyte composition features that correlate with CE from experimental data, grounding our simulations in reality.
- **Experiment 3 (Dose-Response Modeling)**: Needed to generate quantitative predictions of optimal impurity concentrations — the key deliverable for "engineering happy accidents."

## Research Question
Can trace impurities (typically considered contaminants) improve Coulombic Efficiency in lithium batteries, and if so, at what concentrations and through what mechanisms?

## Background and Motivation
The battery industry assumes purer = better. But recent findings challenge this:
- Choe et al. (2024): ~1% Mg "impurity" in Li₂CO₃ improved NCM622 cathode capacity retention by 6.5%
- Hobold et al. (2024): Li₂O (formable from trace water/oxygen) correlates more strongly with high CE than LiF
- Hobold et al. (2021): At CE >99%, trace impurities become "inadvertent differentiators across suppliers"
- Baakes et al. (2023): Moderate water (168-260 ppm) shows no safety difference; thick inorganic SEI delays self-heating

## Hypothesis Decomposition
1. **H1**: Impurities that promote Li₂O-rich SEI formation (e.g., trace water, oxygen species) improve CE relative to ultra-pure systems
2. **H2**: There exists an optimal concentration range for beneficial impurities — too little has no effect, too much is detrimental
3. **H3**: The effect of impurities depends on the base electrolyte system — impurities are more impactful in high-CE regimes
4. **H4**: Metallic impurities (Fe, Cu) are universally detrimental, while Mg and oxygen-containing species can be beneficial

## Proposed Methodology

### Approach
Three-pronged computational and data-driven approach:
1. **Physics-based simulation** (PyBaMM): Model SEI growth with impurity-modified reaction kinetics
2. **Data analysis** (F-GCN dataset): Mine existing electrolyte-CE data for composition-performance relationships
3. **Dose-response modeling**: Combine simulation and data to predict optimal impurity levels

### Experimental Steps
1. Set up PyBaMM with SPMe model and SEI submodel
2. Parameterize impurity effects on SEI kinetics from literature values
3. Simulate cycling at multiple impurity concentrations (0, 10, 50, 100, 500, 1000 ppm)
4. Track CE, capacity, SEI thickness, and composition over 200+ cycles
5. Analyze F-GCN electrolyte dataset for composition-CE correlations
6. Build dose-response curves and identify optimal concentrations
7. Compare predictions against published experimental values

### Baselines
- **Pure system** (0 ppm impurity): Standard PyBaMM SPMe with default SEI parameters
- **Literature CE values**: 92% (conventional carbonate), 99%+ (advanced), 99.9% (state-of-art)
- **Fink et al. data**: 1 wt% metallic impurity effects as upper bound

### Evaluation Metrics
- **Coulombic Efficiency** (primary): Averaged over cycles 10-200 (excluding formation)
- **CE stability**: Standard deviation of CE over cycling
- **SEI thickness growth rate**: nm/cycle
- **Capacity retention**: At cycle 200 relative to cycle 5

### Statistical Analysis Plan
- ANOVA for comparing CE across impurity types and concentrations
- Tukey HSD post-hoc tests for pairwise comparisons
- Regression analysis for dose-response curves (linear, quadratic, logarithmic fits)
- Bootstrap confidence intervals (n=1000) for parameter estimates
- Significance level: α = 0.05

## Expected Outcomes
- **Supporting H1**: CE improvement of 0.1-1% with trace water/oxygen species at 50-200 ppm
- **Supporting H2**: Inverted-U dose-response curve with peak at ~100-500 ppm for beneficial impurities
- **Supporting H3**: Larger CE improvement in high-purity baseline systems
- **Supporting H4**: Monotonic CE decrease with Fe/Cu; non-monotonic for Mg

## Timeline and Milestones
1. Environment setup + data exploration: 15 min
2. PyBaMM simulation implementation: 45 min
3. F-GCN dataset analysis: 30 min
4. Dose-response modeling: 30 min
5. Statistical analysis + visualization: 30 min
6. Report writing: 30 min

## Potential Challenges
- PyBaMM SEI submodels may not directly support impurity parameters → Workaround: modify reaction rate constants as proxy
- F-GCN dataset may lack explicit impurity data → Workaround: use composition features as implicit impurity indicators
- Limited experimental validation data → Workaround: compare against published literature values

## Success Criteria
1. Successfully simulate CE differences between pure and impurity-doped systems
2. Identify at least one impurity type/concentration that improves CE over the pure baseline
3. Generate dose-response curves with quantified optimal concentrations
4. Results consistent with published experimental findings (Choe, Hobold, Fink)
