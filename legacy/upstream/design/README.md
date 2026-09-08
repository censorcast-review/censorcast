# CENSORCAST v0.5 — M5 design-only development

This package starts model development only after the independent M5 data
preparation audit has passed.  It can read the design outcome shard and the
shared calendar/price covariates.  It cannot read either sealed outcome shard,
open the fresh guardian, open the external split, spend confirmatory alpha, or
issue a certificate.

The workflow fits a strong pooled forecasting baseline, a lower-bound-aware
censored-Poisson EM expert, and a deployable prequential risk layer.  It searches
every unique risk-score threshold on calibration A/B, freezes the best
margin-feasible candidate before shadow evaluation, and audits the fixed policy
with item-cluster bootstrap bounds across temporal blocks and product-category
strata.

Use `RUN_CENSORCAST_V0_5_M5_DESIGN_DEVELOPMENT.ipynb` in Colab.  The long
development cell is resumable: completed models and block predictions are
checkpointed to Drive.  If Colab disconnects, reconnect, run setup/preflight,
and rerun the same development cell with `--resume`.

Even a design GO is not confirmatory evidence.  A separate future notebook is
required to consume the fresh guardian exactly once.  No such command exists
in this package.
