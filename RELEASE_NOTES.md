# Release notes

## Initial GitHub release — code and recorded notebook outputs

- Included 6 research notebooks in two thematic directories (`interventions`, `raw_models`).
- Preserved numerical computations, intervention design, model settings and previously recorded output cells.
- Replaced machine-specific training CSV and artifact root path definitions with portable environment-variable fallbacks.
- Redacted local home-directory prefixes **only in historical displayed outputs and explanatory Markdown**; no numeric results or embedded images were changed.
- Added rigorous README describing prior-stage dependencies, full/pilot evidence and scientific limitations.
- Did **not** run/recompute any model or intervention after repackaging.
- No raw CSV, weight files, Parquet data, calibration caches or transport banks are included.

### Integrity note

The notebooks' historical output cells document runs completed **before** portability edits. Re-execute in your own environment before claiming a fully reproduced clean run of this release.
