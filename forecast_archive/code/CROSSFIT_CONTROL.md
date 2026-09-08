# Fixed cross-fitted feature control

`run_crossfit_control.py` adds one exploratory control on the previously used
M5 development panel. It changes how the appended risk feature is obtained on
the base model's training rows. It does not replace any original frozen result.

Both original protocols specify **1,200,000 sampled rows**, training days
365–1313 and seed 20260906. The stored sample from the earlier exact model refit
is compared element by element before this experiment fits anything. Within
each category, sorted item identifiers are shuffled using seed 20260908 and
assigned round-robin to five folds. Every store carrying an item belongs to
the same fold. For each fold, the risk classifier is trained on the other
four folds, and predicts only the held-out items' sampled rows. The five
classifiers retain the original 300-tree LightGBM configuration.

The base model uses the original 40 features plus the out-of-fold risk
prediction, the original 1.2M sampled observed-sales labels and the original
750-round XGBoost L1 configuration. Validation and Later use the already saved
full-training risk classifier. Category multipliers are estimated from
validation alone and frozen before Later scoring. There is no hyperparameter
search, candidate selection, new risk-head refit for inference, or fresh
holdout access. Exactly five risk classifiers and one base model are fit.

This design excludes each row's entire item from the risk model supplying its
training feature. It is **item cross-fitting, not forward-time cross-fitting**:
the training folds cover the same historical period, and feature histories
remain the observed histories available at each forecast origin. Fold risk
models also have about 80% of the original risk training sample. A comparison
with this configuration is not a comparison with all possible stacking
methods.

The extracted inputs are those produced by `replay_m5.py`. Run only in a new
output directory; the experiment refuses to overwrite existing outputs:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=8 python code/run_crossfit_control.py \
  --package . \
  --input-dir /path/to/extracted_inputs \
  --output /path/to/new_crossfit_run
```

The supplied run is in `evidence/cell_audit/crossfit/`. It includes the
pre-fit protocol; item assignments; the exact training sample; all five
training/prediction membership lists; out-of-fold and original in-sample risk
predictions; all six models; fit receipts; the validation scale freeze;
validation and Later forecasts; item sufficient statistics; and results.
Paired item bootstrap intervals compare the control with both the
category-scaled hierarchy base and the frozen RC policy. All intervals are
descriptive on this previously used dataset.

Verify the supplied run without fitting or modifying evidence:

```bash
OPENBLAS_NUM_THREADS=1 python code/verify_crossfit_control.py \
  --package . \
  --input-dir /path/to/extracted_inputs \
  --output /path/to/crossfit_verification.json
```

The verifier checks artifact hashes, the exact original sample and model
parameters, pre-fit protocol ordering, item exclusions, exactly one
out-of-fold prediction per training row, observable target labels, weighted
median category scales, metric reconstruction and paired intervals. Its
checks do not certify a new confirmatory test or establish general superiority
over alternative feature-integration methods.
