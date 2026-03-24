# Cloned Repositories

## Repo 1: PyBaMM
- **URL**: https://github.com/pybamm-team/PyBaMM
- **Purpose**: Open-source battery modeling framework with physics-based models
- **Location**: code/pybamm/
- **Key features**:
  - Single Particle Model (SPM) and Doyle-Fuller-Newman (DFN) model
  - Built-in SEI submodels: reaction-limited, solvent-diffusion-limited, electron-migration-limited
  - Solved in <0.1s; extensible Python API
  - Can modify SEI kinetics to include impurity-dependent reaction rates
- **Relevance**: Primary simulation tool for modeling how trace impurities modify SEI growth kinetics and CE
- **Installation**: `pip install pybamm` or from source

## Repo 2: BatteryML (Microsoft)
- **URL**: https://github.com/microsoft/BatteryML
- **Purpose**: Unified ML platform for battery data analysis and degradation prediction
- **Location**: code/batteryml/
- **Key features**:
  - Integrates multiple public datasets (Severson, CALCE, etc.)
  - Standard ML pipelines for cycle life prediction
  - Feature engineering for battery cycling data
  - ICLR 2024 paper
- **Relevance**: Can be used for data-driven analysis of impurity effects on degradation trajectories
- **Installation**: See code/batteryml/README.md

## Additional Repositories (Not Cloned — Available for Future Use)

- **Dragonfly** (github.com/dragonfly/dragonfly): Bayesian optimization; used for autonomous electrolyte discovery
- **BLAST-Lite** (github.com/NREL/BLAST-Lite): NREL battery lifetime/degradation model library
- **PINN4SOH** (github.com/wang-fujin/PINN4SOH): Physics-informed neural network for degradation
