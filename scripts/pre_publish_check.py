#!/usr/bin/env python3
"""A static audit aid: does not execute notebooks or send data anywhere."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    "notebooks/interventions/04_FORCE_frozen_RF_whole_curve_outage_intervention_engine.ipynb",
    "notebooks/interventions/04B_FORCE_class_pair_support_and_quantile_transport_registry.ipynb",
    "notebooks/interventions/04C_FORCE_shared_class_conditional_transport_bank.ipynb",
    "notebooks/raw_models/05A_FORCE_raw_log_feature_contract.ipynb",
    "notebooks/raw_models/05B_FORCE_raw_log_RF_grouped_well_CV.ipynb",
    "notebooks/raw_models/05C_FORCE_raw_RF_strict_nested_temperature_calibration.ipynb",
]
RED_FLAGS = [
    re.compile(r"/Users/[^/\s<>]+/Desktop/", re.I),
    re.compile(r"[A-Za-z]:\\Users\\[^\\]+\\", re.I),
    re.compile(r"Path[.]home\(\).{0,80}Desktop", re.I),
]
errors = 0
for rel in EXPECTED:
    path = ROOT / rel
    if not path.exists():
        errors += 1
        print(f"ERROR missing notebook: {rel}")
        continue
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
        assert nb["nbformat"] == 4
        cells = nb["cells"]
    except Exception as e:
        errors += 1
        print(f"ERROR malformed notebook: {rel}: {e}")
        continue
    count = sum(bool(c.get("outputs")) for c in cells)
    mb = path.stat().st_size / 1024 / 1024
    print(f"OK {rel}  |  {len(cells)} cells  |  {count} cells with recorded outputs  |  {mb:.2f} MiB")
    if mb > 20:
        print("  WARNING: large notebook may not render well on GitHub")
    all_text = path.read_text(encoding="utf-8")
    for pattern in RED_FLAGS:
        if pattern.search(all_text):
            errors += 1
            print(f"  ERROR: possible personal filesystem path: {pattern.pattern}")
            break
for rel in ("data/raw/train.csv", "data/raw/test.csv"):
    if (ROOT / rel).exists():
        print(f"WARNING: dataset present locally; verify it is not staged for Git: {rel}")
ignore=(ROOT / ".gitignore").read_text(encoding="utf-8")
if "/data/raw/*" not in ignore or "/artifacts/*" not in ignore:
    errors += 1
    print("ERROR: .gitignore does not protect local datasets and artifacts")
print("\nPASS (static checks only)" if not errors else f"\nFAIL: {errors} issue(s)")
sys.exit(bool(errors))
