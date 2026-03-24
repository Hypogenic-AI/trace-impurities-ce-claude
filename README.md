# Trace Impurity Effects on Battery Coulombic Efficiency

A systematic computational study investigating whether trace impurities — typically considered contaminants — can improve lithium battery performance when present at controlled concentrations.

## Key Findings

- **Mg impurity is beneficial**: At ~1000 ppm, Mg improves capacity retention by +0.10% and CE by +0.0018% (p=0.018) by promoting compact, low-resistivity SEI
- **O₂ species improve performance**: Moderate oxygen-containing species (~200-500 ppm) promote Li₂O-rich SEI, correlating with higher CE (consistent with Hobold 2024)
- **Fe is universally detrimental**: -0.33% capacity retention at 1000 ppm due to parasitic electrolyte decomposition
- **Water shows threshold behavior**: Neutral below ~260 ppm, detrimental above 500 ppm (R²=0.992 fit)
- **SEI resistivity is the key predictor**: Impurities that reduce SEI resistivity improve performance (r=-0.891, p<0.0001)

## How to Reproduce

```bash
# Set up environment
uv venv && source .venv/bin/activate
uv add numpy pandas matplotlib scipy scikit-learn openpyxl seaborn pybamm

# Run experiments (in order)
python src/experiment1_pybamm_impurity_simulation.py   # ~15 min
python src/experiment2_baakes_analysis.py               # ~1 min
python src/experiment3_dose_response.py                 # ~20 min
python src/experiment4_statistics.py                    # ~1 min
```

## File Structure

```
├── REPORT.md                    # Full research report with results
├── README.md                    # This file
├── planning.md                  # Research plan and motivation
├── literature_review.md         # Synthesized literature review
├── resources.md                 # Catalog of all resources
├── src/
│   ├── explore_data.py          # Dataset exploration
│   ├── experiment1_*.py         # PyBaMM impurity simulation (13 scenarios × 100 cycles)
│   ├── experiment2_*.py         # Baakes SEI composition analysis
│   ├── experiment3_*.py         # Dose-response modeling with literature data
│   └── experiment4_*.py         # Statistical analysis and visualization
├── results/
│   ├── data/                    # CSV/JSON result files
│   └── plots/                   # All figures (PNG)
├── datasets/                    # Pre-downloaded experimental datasets
├── papers/                      # Downloaded research papers (18 PDFs)
└── code/                        # Cloned repositories (PyBaMM, BatteryML)
```

## Methodology

1. **PyBaMM simulation**: SPMe model with reaction-limited SEI, modified parameters to model impurity effects on SEI kinetics
2. **Baakes dataset analysis**: SEI composition effects on thermal stability from published modeling data
3. **Dose-response modeling**: Hormesis and monotonic models fitted to combined simulation + literature data
4. **Statistical analysis**: Welch's t-tests, ANOVA, Pearson correlations, curve fitting

See [REPORT.md](REPORT.md) for full details.
