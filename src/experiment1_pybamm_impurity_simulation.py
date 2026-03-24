"""
Experiment 1: PyBaMM Simulation of Trace Impurity Effects on Coulombic Efficiency

Simulates Li-ion battery cycling with modified SEI parameters to model
how trace impurities alter SEI growth kinetics and resulting CE.

Approach:
- Use SPMe model with SEI growth submodel
- Modify SEI-related parameters to represent impurity effects:
  * SEI reaction rate (k_SEI): impurities catalyze/inhibit SEI formation
  * SEI resistivity: impurities change SEI ionic conductivity
  * Exchange current density: impurities affect electrode kinetics
- Compare CE across pure and impurity-modified systems
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
import os
import sys
import warnings
warnings.filterwarnings('ignore')

# Reproducibility
np.random.seed(42)

os.chdir("/data/hypogenicai/workspaces/trace-impurities-ce-claude")

import pybamm

print(f"Python: {sys.version}")
print(f"NumPy: {np.__version__}")
print(f"PyBaMM: {pybamm.__version__}")

# ============================================================
# Define impurity scenarios
# ============================================================
# We model impurities by modifying SEI-related parameters.
# Literature basis:
# - Mg promotes Li₂O-rich SEI (Choe 2024): reduces SEI resistivity, slight increase in k_SEI
# - Water promotes inorganic SEI (Baakes 2023): increases k_SEI, produces LiOH/Li₂O
# - Fe catalyzes electrolyte decomposition (Fink 2021): large increase in k_SEI, increases resistivity
# - Oxygen species promote Li₂O (Hobold 2024): moderate k_SEI increase, reduces resistivity

# Impurity effects modeled as multipliers on base parameters
# Format: {name: {param: multiplier}}
# k_SEI_multiplier > 1 means faster SEI growth (more side reactions → lower CE initially)
# resistivity_multiplier < 1 means better SEI conductivity (passivation → eventually higher CE)
# j0_multiplier represents effect on main reaction kinetics

impurity_scenarios = {
    "Ultra-pure (baseline)": {
        "k_SEI_mult": 1.0,
        "resistivity_mult": 1.0,
        "j0_mult": 1.0,
        "description": "No impurities - reference case"
    },
    "Mg (50 ppm)": {
        "k_SEI_mult": 1.05,
        "resistivity_mult": 0.85,
        "j0_mult": 1.02,
        "description": "Trace Mg promotes Li₂O-rich compact SEI"
    },
    "Mg (200 ppm)": {
        "k_SEI_mult": 1.15,
        "resistivity_mult": 0.75,
        "j0_mult": 1.05,
        "description": "Higher Mg - more pronounced SEI modification"
    },
    "Mg (1000 ppm)": {
        "k_SEI_mult": 1.40,
        "resistivity_mult": 0.70,
        "j0_mult": 1.08,
        "description": "Bulk Mg - significant SEI modification"
    },
    "Water (50 ppm)": {
        "k_SEI_mult": 1.10,
        "resistivity_mult": 0.90,
        "j0_mult": 0.98,
        "description": "Trace water promotes inorganic SEI (Li₂O, LiOH)"
    },
    "Water (200 ppm)": {
        "k_SEI_mult": 1.30,
        "resistivity_mult": 0.80,
        "j0_mult": 0.95,
        "description": "Moderate water - dual role (SEI + HF generation)"
    },
    "Water (1000 ppm)": {
        "k_SEI_mult": 2.0,
        "resistivity_mult": 1.10,
        "j0_mult": 0.85,
        "description": "High water - detrimental (HF corrosion, gas)"
    },
    "Fe (50 ppm)": {
        "k_SEI_mult": 1.20,
        "resistivity_mult": 1.15,
        "j0_mult": 0.97,
        "description": "Trace Fe catalyzes electrolyte decomposition"
    },
    "Fe (200 ppm)": {
        "k_SEI_mult": 1.50,
        "resistivity_mult": 1.35,
        "j0_mult": 0.92,
        "description": "Moderate Fe - significant parasitic reactions"
    },
    "Fe (1000 ppm)": {
        "k_SEI_mult": 2.50,
        "resistivity_mult": 1.60,
        "j0_mult": 0.80,
        "description": "High Fe - severe degradation, dissolution/plating"
    },
    "O₂ species (50 ppm)": {
        "k_SEI_mult": 1.08,
        "resistivity_mult": 0.88,
        "j0_mult": 1.01,
        "description": "Trace oxygen promotes Li₂O formation (Hobold 2024)"
    },
    "O₂ species (200 ppm)": {
        "k_SEI_mult": 1.20,
        "resistivity_mult": 0.78,
        "j0_mult": 1.03,
        "description": "Moderate oxygen - more Li₂O in SEI"
    },
    "O₂ species (1000 ppm)": {
        "k_SEI_mult": 1.60,
        "resistivity_mult": 0.85,
        "j0_mult": 0.95,
        "description": "High oxygen - excessive oxidation"
    },
}

# ============================================================
# Run simulations
# ============================================================
def run_simulation(scenario_name, params, n_cycles=100):
    """Run PyBaMM cycling simulation with modified SEI parameters."""
    print(f"\n  Simulating: {scenario_name}...")

    # Create model with SEI
    options = {"SEI": "reaction limited"}
    model = pybamm.lithium_ion.SPMe(options=options)

    # Get default parameter values
    param = pybamm.ParameterValues("Chen2020")

    # Modify SEI kinetic rate constant
    base_k_sei = param["SEI kinetic rate constant [m.s-1]"]
    param["SEI kinetic rate constant [m.s-1]"] = base_k_sei * params["k_SEI_mult"]

    # Modify SEI resistivity
    base_sei_resistivity = param["SEI resistivity [Ohm.m]"]
    param["SEI resistivity [Ohm.m]"] = base_sei_resistivity * params["resistivity_mult"]

    # Modify exchange current density (negative electrode)
    base_j0_neg = param["Negative electrode exchange-current density [A.m-2]"]
    if callable(base_j0_neg):
        mult = params["j0_mult"]
        param["Negative electrode exchange-current density [A.m-2]"] = lambda c_e, c_s_surf, c_s_max, T, j0=base_j0_neg, m=mult: j0(c_e, c_s_surf, c_s_max, T) * m

    # Define experiment: cycling at 1C for n_cycles
    experiment = pybamm.Experiment(
        [
            (
                "Discharge at 1C until 2.5 V",
                "Rest for 5 minutes",
                "Charge at 1C until 4.2 V",
                "Hold at 4.2 V until C/50",
                "Rest for 5 minutes",
            )
        ] * n_cycles,
    )

    # Solve
    sim = pybamm.Simulation(model, parameter_values=param, experiment=experiment)
    try:
        sol = sim.solve(calc_esoh=False, initial_soc=1.0)
    except Exception as e:
        print(f"    Solver error: {e}")
        return None

    return sol


def extract_cycle_metrics(sol, n_cycles=100):
    """Extract CE, capacity, and SEI thickness per cycle from solution."""
    cycles = []

    for i in range(n_cycles):
        try:
            cycle = sol.cycles[i]
            # Discharge capacity
            Q_dis = cycle["Discharge capacity [A.h]"].entries
            Q_dis_max = np.max(Q_dis) if len(Q_dis) > 0 else np.nan

            # Charge throughput (negative current = charge)
            Q_ch = cycle["Throughput capacity [A.h]"].entries
            # Use total throughput as proxy
            t = cycle["Time [s]"].entries
            I = cycle["Current [A]"].entries

            # Calculate charge and discharge separately
            dt = np.diff(t)
            I_mid = (I[:-1] + I[1:]) / 2.0
            # Discharge: positive current
            q_discharge = np.sum(np.abs(I_mid[I_mid > 0]) * dt[I_mid > 0]) / 3600
            # Charge: negative current
            q_charge = np.sum(np.abs(I_mid[I_mid < 0]) * dt[I_mid < 0]) / 3600

            # Coulombic efficiency
            ce = (q_discharge / q_charge * 100) if q_charge > 0 else np.nan

            # SEI thickness
            try:
                sei = cycle["Loss of lithium to SEI [mol]"].entries
                sei_loss = sei[-1] - sei[0] if len(sei) > 0 else np.nan
            except KeyError:
                sei_loss = np.nan

            cycles.append({
                "cycle": i + 1,
                "discharge_capacity_Ah": q_discharge,
                "charge_capacity_Ah": q_charge,
                "CE_pct": ce,
                "sei_loss_mol": sei_loss,
            })
        except (IndexError, KeyError) as e:
            continue

    return pd.DataFrame(cycles)


# Run all scenarios
print("=" * 60)
print("EXPERIMENT 1: PyBaMM Impurity Simulation")
print("=" * 60)

n_cycles = 100
all_results = {}
summary_data = []

for name, params in impurity_scenarios.items():
    sol = run_simulation(name, params, n_cycles=n_cycles)
    if sol is not None:
        metrics = extract_cycle_metrics(sol, n_cycles=n_cycles)
        if len(metrics) > 0:
            all_results[name] = metrics

            # Summary stats (cycles 10-100 to exclude formation)
            stable = metrics[metrics["cycle"] >= 10]
            mean_ce = stable["CE_pct"].mean()
            std_ce = stable["CE_pct"].std()
            cap_retention = (
                stable["discharge_capacity_Ah"].iloc[-1]
                / stable["discharge_capacity_Ah"].iloc[0]
                * 100
                if len(stable) > 1
                else np.nan
            )
            total_sei_loss = stable["sei_loss_mol"].sum()

            summary_data.append({
                "scenario": name,
                "mean_CE_pct": mean_ce,
                "std_CE_pct": std_ce,
                "capacity_retention_pct": cap_retention,
                "total_SEI_loss_mol": total_sei_loss,
                "n_cycles_completed": len(metrics),
            })
            print(f"    CE: {mean_ce:.4f}% ± {std_ce:.4f}%, Cap retention: {cap_retention:.2f}%")
        else:
            print(f"    No valid cycles extracted")
    else:
        print(f"    Simulation failed")

# Save results
summary_df = pd.DataFrame(summary_data)
summary_df.to_csv("results/data/experiment1_summary.csv", index=False)
print(f"\nSummary saved to results/data/experiment1_summary.csv")
print(summary_df.to_string(index=False))

# Save per-cycle data
for name, df in all_results.items():
    safe_name = name.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    df.to_csv(f"results/data/exp1_cycles_{safe_name}.csv", index=False)

# ============================================================
# Visualization
# ============================================================
print("\nGenerating plots...")

# Plot 1: CE vs Cycle for all scenarios
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Group by impurity type
impurity_groups = {
    "Mg": ["Ultra-pure (baseline)", "Mg (50 ppm)", "Mg (200 ppm)", "Mg (1000 ppm)"],
    "Water": ["Ultra-pure (baseline)", "Water (50 ppm)", "Water (200 ppm)", "Water (1000 ppm)"],
    "Fe": ["Ultra-pure (baseline)", "Fe (50 ppm)", "Fe (200 ppm)", "Fe (1000 ppm)"],
    "O₂ species": ["Ultra-pure (baseline)", "O₂ species (50 ppm)", "O₂ species (200 ppm)", "O₂ species (1000 ppm)"],
}

colors = {50: '#2196F3', 200: '#4CAF50', 1000: '#F44336'}

for ax, (group_name, scenarios) in zip(axes.flat, impurity_groups.items()):
    for scenario in scenarios:
        if scenario in all_results:
            df = all_results[scenario]
            label = scenario
            if "baseline" in scenario:
                ax.plot(df["cycle"], df["CE_pct"], 'k-', linewidth=2, label=label, alpha=0.8)
            else:
                conc = int(scenario.split("(")[1].split(" ")[0])
                ax.plot(df["cycle"], df["CE_pct"], '-', color=colors[conc],
                       linewidth=1.5, label=label, alpha=0.8)
    ax.set_xlabel("Cycle Number")
    ax.set_ylabel("Coulombic Efficiency (%)")
    ax.set_title(f"{group_name} Impurity Effect on CE")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("results/plots/exp1_CE_vs_cycle_by_impurity.png", dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: results/plots/exp1_CE_vs_cycle_by_impurity.png")

# Plot 2: Summary bar chart - mean CE by scenario
fig, ax = plt.subplots(figsize=(14, 6))
df_plot = summary_df.sort_values("mean_CE_pct", ascending=True)
colors_bar = []
for s in df_plot["scenario"]:
    if "baseline" in s:
        colors_bar.append('#607D8B')
    elif "Mg" in s:
        colors_bar.append('#4CAF50')
    elif "Water" in s:
        colors_bar.append('#2196F3')
    elif "Fe" in s:
        colors_bar.append('#F44336')
    elif "O₂" in s:
        colors_bar.append('#FF9800')
    else:
        colors_bar.append('#9E9E9E')

bars = ax.barh(range(len(df_plot)), df_plot["mean_CE_pct"], color=colors_bar, alpha=0.8)
ax.set_yticks(range(len(df_plot)))
ax.set_yticklabels(df_plot["scenario"], fontsize=9)
ax.set_xlabel("Mean Coulombic Efficiency (%)")
ax.set_title("Effect of Trace Impurities on Coulombic Efficiency (Cycles 10-100)")
ax.axvline(x=summary_df[summary_df["scenario"].str.contains("baseline")]["mean_CE_pct"].values[0],
           color='k', linestyle='--', alpha=0.5, label='Baseline')

# Add value labels
for bar, val in zip(bars, df_plot["mean_CE_pct"]):
    ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
            f'{val:.3f}%', va='center', fontsize=8)

ax.legend()
plt.tight_layout()
plt.savefig("results/plots/exp1_CE_summary_bar.png", dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: results/plots/exp1_CE_summary_bar.png")

# Plot 3: Capacity retention
fig, ax = plt.subplots(figsize=(14, 6))
df_plot = summary_df.sort_values("capacity_retention_pct", ascending=True)
bars = ax.barh(range(len(df_plot)), df_plot["capacity_retention_pct"], color=colors_bar, alpha=0.8)
ax.set_yticks(range(len(df_plot)))
ax.set_yticklabels(df_plot["scenario"], fontsize=9)
ax.set_xlabel("Capacity Retention at Cycle 100 (%)")
ax.set_title("Effect of Trace Impurities on Capacity Retention")
plt.tight_layout()
plt.savefig("results/plots/exp1_capacity_retention.png", dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: results/plots/exp1_capacity_retention.png")

# Plot 4: Discharge capacity vs cycle for baseline vs best/worst
fig, ax = plt.subplots(figsize=(10, 6))
for scenario in ["Ultra-pure (baseline)", "Mg (200 ppm)", "O₂ species (200 ppm)", "Fe (1000 ppm)", "Water (1000 ppm)"]:
    if scenario in all_results:
        df = all_results[scenario]
        ax.plot(df["cycle"], df["discharge_capacity_Ah"], '-', linewidth=1.5, label=scenario)
ax.set_xlabel("Cycle Number")
ax.set_ylabel("Discharge Capacity (Ah)")
ax.set_title("Capacity Fade: Selected Impurity Scenarios")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("results/plots/exp1_capacity_fade_selected.png", dpi=150, bbox_inches='tight')
plt.close()
print("  Saved: results/plots/exp1_capacity_fade_selected.png")

print("\n" + "=" * 60)
print("EXPERIMENT 1 COMPLETE")
print("=" * 60)
