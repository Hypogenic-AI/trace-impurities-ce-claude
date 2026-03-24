"""Explore available datasets for trace impurity study."""
import pandas as pd
import numpy as np
import json
import os

# Set working directory
os.chdir("/data/hypogenicai/workspaces/trace-impurities-ce-claude")

print("=" * 60)
print("DATASET EXPLORATION")
print("=" * 60)

# 1. F-GCN Electrolyte-CE Dataset
print("\n--- F-GCN Electrolyte-to-CE Dataset ---")
try:
    fgcn_path = "datasets/fgcn_electrolyte_ce/ci3c01030_si_002.xlsx"
    xls = pd.ExcelFile(fgcn_path)
    print(f"Sheets: {xls.sheet_names}")
    for sheet in xls.sheet_names:
        df = pd.read_excel(fgcn_path, sheet_name=sheet)
        print(f"\nSheet '{sheet}': {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print(df.head(3).to_string())
except Exception as e:
    print(f"Error: {e}")

# 2. Baakes KITopen Dataset
print("\n\n--- Baakes KITopen Dataset ---")
try:
    baakes_path = "datasets/baakes_kitopen/10.35097-1804/data/dataset/DataSources.xlsx"
    xls = pd.ExcelFile(baakes_path)
    print(f"Sheets: {xls.sheet_names}")
    for sheet in xls.sheet_names[:5]:  # First 5 sheets
        df = pd.read_excel(baakes_path, sheet_name=sheet)
        print(f"\nSheet '{sheet}': {df.shape}")
        print(f"Columns: {list(df.columns)[:10]}")
        if len(df) > 0:
            print(df.head(2).to_string())
except Exception as e:
    print(f"Error: {e}")

# 3. Test PyBaMM basic functionality
print("\n\n--- PyBaMM Test ---")
try:
    import pybamm
    print(f"PyBaMM version: {pybamm.__version__}")
    model = pybamm.lithium_ion.SPMe()
    print(f"Model: {model.name}")
    print(f"Available SEI options: {pybamm.lithium_ion.SPMe.default_quick_plot_variables}")
except Exception as e:
    print(f"PyBaMM test error: {e}")
