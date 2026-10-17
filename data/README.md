# Local data layout

Place `train.csv` inside `data/raw/` or set `STRATASHIFT_TRAIN_CSV` to the training CSV location. Do not commit the dataset. The official test CSV is not needed for these six stages.

Place prior-stage intermediate files inside `artifacts/` in the stage subfolders described in `README.md`, or point `STRATASHIFT_ARTIFACT_ROOT` to your existing `FORCE_Causal_Project` directory. The model weights, OOF probabilities and transport banks are intentionally not bundled with the public code.

Dataset source: https://doi.org/10.5281/zenodo.4351156
