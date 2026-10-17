#!/usr/bin/env python3
"""Display whether local upstream inputs required by each experiment exist."""
import os
from pathlib import Path
root = Path(__file__).resolve().parents[1]
train = Path(os.environ.get("STRATASHIFT_TRAIN_CSV", root / "data/raw/train.csv")).expanduser()
art = Path(os.environ.get("STRATASHIFT_ARTIFACT_ROOT", root / "artifacts")).expanduser()
sets = {
    "04 (outage pilot)": [
        art/"01_clean_splits_support/10_grouped_5fold_well_assignment.csv",
        art/"02B_legacy_RF_grouped_well_CV/full/artifacts",
        art/"02B_legacy_RF_grouped_well_CV/full/oof_predictions",
        art/"02B_legacy_RF_grouped_well_CV/full/12_run_configuration.json",
        art/"03_nested_grouped_temperature_calibration/full/11_run_configuration.json",
        art/"03_nested_grouped_temperature_calibration/full/10_nested_temperature_registry.json",
        art/"03_nested_grouped_temperature_calibration/full/calibrated_outer_oof",
    ],
    "04B (registry)": [art/"01_clean_splits_support/10_grouped_5fold_well_assignment.csv"],
    "04C (transport bank)": [
        art/"04B_class_pair_support_transport_registry/full/05_directed_pair_support_registry.csv",
        art/"04B_class_pair_support_transport_registry/full/06_pair_stability_summary.csv",
        art/"04B_class_pair_support_transport_registry/full/10_recommended_pilot_pairs.csv",
        art/"04B_class_pair_support_transport_registry/full/13_registry_gate.json",
        art/"04B_class_pair_support_transport_registry/full/14_run_configuration.json",
    ],
    "05A (raw feature contract)": [
        art/"04C_shared_class_conditional_transport_bank/full/07_transport_bank_gate.json",
        art/"04C_shared_class_conditional_transport_bank/full/08_run_configuration.json",
    ],
    "05B (raw RF CV)": [
        art/"05A_raw_log_feature_contract/full/10_primary_raw_feature_contract.json",
        art/"05A_raw_log_feature_contract/full/12_fold_safe_preprocessing_policy.json",
        art/"05A_raw_log_feature_contract/full/13_raw_feature_contract_gate.json",
        art/"05A_raw_log_feature_contract/full/15_input_file_hashes.json",
    ],
    "05C (nested calibration)": [
        art/"05A_raw_log_feature_contract/full/13_raw_feature_contract_gate.json",
        art/"05A_raw_log_feature_contract/full/15_input_file_hashes.json",
        art/"05B_raw_log_RF_grouped_well_CV/full/17_stage_gate.json",
        art/"05B_raw_log_RF_grouped_well_CV/full/18_run_configuration.json",
        art/"05B_raw_log_RF_grouped_well_CV/full/16_OOF_predictions_raw8.parquet",
        art/"05B_raw_log_RF_grouped_well_CV/full/16_OOF_predictions_core6.parquet",
    ]
}
print("Training CSV:", train, "[OK]" if train.exists() else "[MISSING]")
print("Artifact root:", art)
for stage, paths in sets.items():
    missing=[p for p in paths if not p.exists()]
    print(f"{stage}: {len(paths)-len(missing)}/{len(paths)} artifacts available")
    for p in missing:print("    missing:",p.relative_to(art))
