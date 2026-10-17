#!/usr/bin/env python3
"""Static publishing checks only; does not execute model-training notebooks."""
from pathlib import Path
import json,re,sys,ast
ROOT=Path(__file__).resolve().parents[1]
EXPECTED = ['notebooks/interventions/04_FORCE_frozen_RF_whole_curve_outage_intervention_engine.ipynb', 'notebooks/interventions/04B_FORCE_class_pair_support_and_quantile_transport_registry.ipynb', 'notebooks/interventions/04C_FORCE_shared_class_conditional_transport_bank.ipynb', 'notebooks/raw_models/05A_FORCE_raw_log_feature_contract.ipynb', 'notebooks/raw_models/05B_FORCE_raw_log_RF_grouped_well_CV.ipynb', 'notebooks/raw_models/05C_FORCE_raw_RF_strict_nested_temperature_calibration.ipynb', 'notebooks/intervention_evaluation/06A_FORCE_raw_RF_class_conditional_transport_interventions_TIE_SAFE.ipynb', 'notebooks/intervention_evaluation/06A2_FORCE_all_class_probability_redistribution_MEMORY_TIE_SAFE_FIXED.ipynb', 'notebooks/intervention_evaluation/06B_FORCE_legacy_RF_FULL_PRECISION_FIXED.ipynb', 'notebooks/intervention_evaluation/06C_FORCE_raw_vs_legacy_representation_amplification.ipynb', 'notebooks/robustness/07A_FORCE_robust_RF_nested_grouped_candidate_selection.ipynb']
FAILS=[]
for rel in EXPECTED:
    p=ROOT/rel
    if not p.is_file():
        FAILS.append(f"Missing notebook: {rel}")
        continue
    try:
        nb=json.loads(p.read_text(encoding='utf8'))
        assert nb['nbformat']==4
        for i,cell in enumerate(nb['cells']):
            st=''.join(cell.get('source',[]))
            if cell['cell_type']=='markdown' and re.search(r'[\u0600-\u06FF]',st):
                FAILS.append(f"Persian markdown in {rel}, cell {i}")
            if cell['cell_type']=='code':
                compile(st, f"{rel} cell {i}", 'exec')
                if 'Path.home()' in st and 'Desktop' in st:
                    FAILS.append(f"Nonportable path in {rel}, cell {i}")
        print(f"OK: {rel} | {len(nb['cells'])} cells | {sum(bool(c.get('outputs')) for c in nb['cells'])} stored-output cells")
    except Exception as e:
        FAILS.append(f"Parse/code issue in {rel}: {e}")
print('\n'+'PASS (static only)' if not FAILS else '\nFAIL\n'+'\n'.join(FAILS))
sys.exit(bool(FAILS))
