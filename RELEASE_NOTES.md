# Update: Stage 06 evaluation + 07A robustness

- Selected final 06A/06A2/06B/06C notebooks and completed 07A robustness candidate study.
- Removed Persian-language explanatory Markdown from **all 11 included notebooks**; preserved code cells, output values, and execution metadata.
- Made 07A paths environment-configurable and preserved previous Stage-06 portability edits.
- Upgraded published README and static prepublication checks.
- Does not contain upstream datasets, caches, trained models, or large artifacts.
- **Not rerun** after path/Markdown edits.

# Release notes

## Stage 06 — Full intervention evaluation and representation amplification

- Added **four selected, completed notebooks** (06A, 06A2, 06B, 06C) under `notebooks/intervention_evaluation/`; older/failing development variants were excluded.
- Extended the README workflow, dependencies, results and scientific interpretation limits.
- Updated `pre_publish_check.py` to validate the ten published notebooks.
- Extended `check_inputs.py` to report upstream prerequisites for stage 06.
- Changed only the stage-06 notebooks' machine-specific **filesystem configuration**, and the corresponding explanatory Markdown example, not the fitted model settings or intervention/effect calculations.
- Retained original notebook output cells and their reported numerical results; redacted old macOS home-directory prefixes from historical text outputs.
- **No stage-06 notebook was re-executed** after the portability edits. Stored stage gates relate to prior local runs.
- No CSV/parquet data, trained model artifacts, large transport banks, logs or local output directories are included in this update.

## Initial release — Stages 04 and 05

- Published six notebooks for outage piloting, directed class-pair support, transport bank creation, raw-feature modeling and nested calibration.
- Kept notebook results while omitting dataset and derived artifacts.
