# When More Predictions Cover Less: Accuracy and Coverage under Ratio Risk

Anonymous manuscript source, experiments, and numerical evidence.

The paper studies how acceptance utility changes selector choice under a
ratio-risk cap. It combines quantitative theory, accepted-set budget audits,
an unchanged frozen external contrast, and retrospective experiments on
retail forecasting and urban mobility. The latest addition compares five
selector rankings under the same calibration protocol, then selects by case
or exposure coverage. A separate-window risk screen measures the coverage
cost of adding a risk margin and checking it before utility selection.

## Complete repository

This repository includes manuscript source, experiment code, fitted model
objects, saved predictions, calibration inputs, sufficient statistics, and
verification scripts. Source and PDF files can be viewed directly. Numerical
assets are packaged into 53 original parts and a separate additional-results archive under `data_parts/` to support reliable
transfer; no Git LFS or external data download is needed for the supported replay.
Run `python code/restore_large_assets.py` once after cloning. It restores the
original file layout and checks every asset against the original SHA-256 hashes.
Allow approximately 1 GB of free disk space for restoration.

The manuscript is [available as a PDF](paper/CENSORCAST_ICLR_2027_Final.pdf).
Start with the verification commands before attempting a new fit. The new
accuracy/coverage experiment is retrospective; the original external test and
its frozen records are preserved byte for byte.

`MANIFEST.json` binds every distributed source and numerical file. The preceding
release manifest is retained in `evidence/SOURCE_RELEASE_MANIFEST.json`.
Repository packaging does not constitute a new experiment, protocol freeze, or
holdout opening. `legacy/` and all original experiment records are unchanged.

## Utility-based policy selection and separate-window risk screening

`evidence/policy_choice/` retains all 22 declared cap/menu settings, all 15
screen candidates, frozen choices, complete results, and cluster sufficient
statistics. These are **additional retrospective audits**, not new confirmation
trials. They fit no model and do not reopen the original external partition.

- At the primary cap, case utility selects the excess ranking. Exposure utility
  selects descending predicted demand for all three M5 predictors and the
  ratio ranking for Bike. Evaluation demand gains are 7.64, 8.31, 10.63, and
  5.01 percentage points, respectively, at lower case coverage.
- Eight fit-conditional coverage intervals, adjusted within this audit, exclude
  zero. The three M5 comparisons share data and are not independent replications.
- The stricter A-window design has ten feasible candidates; all ten pass the
  separate approximate B-window risk screen. The six utility-selected policies
  have Later pointwise 95% risk intervals below the reporting cap, with reduced
  coverage. This is not a distribution-free or groupwise deployment guarantee.
- The original Bike row/ratio/union risk intervals all cross the cap. The sample
  union is infeasible, but its population infeasibility is not established.

After restoring assets:

```bash
OPENBLAS_NUM_THREADS=1 python code/verify_policy_choice.py
python code/replay_bike_risk_audit.py
# Optional full audit replay (threshold search; no model fit):
OPENBLAS_NUM_THREADS=1 python code/run_policy_choice.py \
  --output reproduction_outputs/policy_choice_replay
# Rebuild generated tables and figure from the saved audit:
python code/build_policy_choice_assets.py
```

`code/policy_audit.py` provides reusable score, threshold-design, utility-choice,
and sufficient-statistic functions. `choose` returns `None` for an empty eligible
menu. Undefined risk is retained for zero accepted exposure. `PROTOCOL.json`
documents the utility, eligibility rules, tie order, cap grids, and resampling.

## Non-retail evidence and scope

The added UCI Bike Sharing check exhibits the primary row-versus-exposure
contrast: -13.34 case-coverage points and +5.01 rental-coverage points. Both
point risks meet the reporting cap; their union does not. All three approximate
risk intervals cross the cap, so this is sample-level accounting. The design uses
randomized day groups and recorded weather, so this is conditional prediction,
not chronological deployment validation. Delicious is infeasible at its primary
calibration condition; the earlier Yeast primary result is null. All outcomes
and declared cap settings are retained, along with models and prediction arrays.

The original retail external policies have a feasible union. They confirm a
selected contrast's transfer, not transfer of binding budget competition.
A descending-demand baseline outperforms the fitted pure-ratio rule in demand
coverage on M5. The paper does not claim universal superiority for estimated
ratio ranking.

```bash
python code/verify_nonretail.py
# Optional reruns of disclosed tests, into new output directories:
python code/rerun_nonretail.py bike --output reproduction_outputs/bike_rerun
python code/rerun_nonretail.py delicious --output reproduction_outputs/delicious_rerun
```

## Additional prespecified checks

The new `evidence/additional/` directory contains the 288-configuration M5
cap/floor sweep and the official-split Yeast classification check, including
frozen classifiers, calibration arrays, test masks, and the complete negative
result. The Yeast primary comparison does **not** establish a strict reversal.
Its weight is predicted-positive label count, not true-positive coverage.
M5 sensitivity is retrospective development analysis with zero new fits and
zero access to the original holdouts. The error-only baseline adapts Franc et
al.'s regression-based uncertainty ranking to WAPE calibration; it does not
reproduce SELE or establish the original method's risk guarantees.

After restoring the existing asset parts, replay the additional saved metrics:

```bash
python code/verify_additional.py
```

Optional complete reruns write to a new directory and preserve original records:

```bash
python code/rerun_additional.py yeast --output reproduction_outputs/yeast_rerun
python code/rerun_additional.py sensitivity --output reproduction_outputs/sensitivity_rerun
```

Historical execution scripts are preserved byte-for-byte under
`evidence/additional/` because their hashes precede execution. The wrapper
recreates their relative working paths in a temporary workspace. Rerunning an
already disclosed test is a reproducibility check, not a new confirmation test.
The raw Yeast files come from the Mulan maintainer's official repository;
`download_yeast.py` checks their Git blob identities. The original protocol,
freeze record, and single evaluation receipt are retained alongside results.

## Quick verification and manuscript build

Use Python 3.12 and an isolated environment, then install `requirements.txt`.
LaTeX with pdfLaTeX and BibTeX is required only to build the PDF.

```bash
git clone https://github.com/censorcast-review/censorcast.git
cd censorcast
python code/restore_large_assets.py
python -m pip install -r requirements.txt
python code/verify_release.py
python code/verify_core.py
python code/build_paper.py
```

The last command writes `reproduction_outputs/paper/CENSORCAST_ICLR_2027_Final.pdf`.
It enforces at most nine main-text pages and rejects undefined references and
overfull boxes. The supplied PDF has been visually inspected separately.

## Full numerical replay of the added experiment

The numerical inputs are already included:

```bash
python code/verify_release.py
python code/verify_accuracy_selection.py evidence/accuracy_selection
python code/extract_development_inputs.py --output reproduction_outputs/m5_inputs
python code/replay_selector_models.py \
  --forecast-package forecast_archive \
  --data reproduction_outputs/m5_inputs \
  --evidence evidence/accuracy_selection \
  --output reproduction_outputs/selector_model_replay.json
```

The first replay reconstructs all nine masks, metrics, budget decompositions,
and paired item-bootstrap intervals. The second rebuilds origin-valid features,
checks 50,000 later head predictions, and repeats every calibration threshold
search from model outputs. Both preserve saved evidence.

To refit the four new heads and all nine thresholds from scratch, use a new
output directory (the runner refuses an existing directory):

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=4 python code/run_accuracy_selection.py \
  --forecast-package forecast_archive \
  --data reproduction_outputs/m5_inputs \
  --output reproduction_outputs/accuracy_refit
```

This reuses frozen forecasting objects and the pre-censoring development target.
It does not access either held-out partition or create an independent test.
Model fitting on 600,000 rows and inference on millions of rows require several
GB of memory; the recorded run used a CPU environment with 21 GB available.

## Evidence boundaries

1. **Theory and original external comparison.** `legacy/` is the unchanged
   anonymous release. Its own hash verifier checks 620 files, 19 frozen guardian
   objects, and 26 copied external dependencies. The external pair was amended
   before first access: 14:29 initial freeze, 14:47 replacement, 15:10 opening,
   15:13 completion on 2026-09-06 UTC. The earlier plan is retained byte for byte.
   External statistical replay uses already-released item sufficient statistics.
2. **New accuracy/utility comparison.** `evidence/accuracy_selection/` contains
   the protocol, four heads, frozen thresholds, forecast/head arrays, item statistics, and full results. Training days 1555–1610;
   calibration 1611–1645 / 1646–1673; evaluation 1800–1913. All use development
   items and previously consumed periods. Bootstrap intervals are descriptive
   and conditional on the fitted models and prior research history.
3. **Forecasting controls.** `forecast_archive/` preserves only the dependency
   subset needed for the added comparison and reported M5/FreshRetailNet controls.
   `evidence/PRESERVED_FORECAST_SUBSET.json` records their byte-identical source
   hashes. The preceding full forecasting archive SHA-256 is recorded there.
   Historical utilities requiring omitted experiments are archival source, not
   entry points for this manuscript. The commands above are the supported path.
4. **Natural data.** FreshRetailNet's later learned-model comparisons reuse a
   previously opened seven-day cohort. Non-stockout rows target recorded sales
   conditional on realized availability. All-row metrics also target sales;
   neither measures latent stockout demand or inventory cost. The no-risk-feature
   residual model is a separately tuned adaptive follow-up.

## Files and attribution

- `paper/`: current LaTeX, references, figures, and tables.
- `code/`: integration experiment, model replay, verification, and PDF build.
- `docs/`: auxiliary theoretical derivations from the original paper.
- `legacy/`: original anonymous theory/confirmation source and frozen records.
- `forecast_archive/`: saved predictor dependencies and forecasting controls.
- `evidence/`: the new experiment and current verification reports.

M5 recorded sales: https://zenodo.org/records/10203108.
FreshRetailNet-50K: https://arxiv.org/abs/2505.16319 and
https://huggingface.co/datasets/Dingdong-Inc/FreshRetailNet-50K.
Chronos-2: https://arxiv.org/abs/2510.15821 and
https://huggingface.co/amazon/chronos-2.
Dataset and third-party software licenses remain those of their original
providers. The repository includes derived development arrays for replay,
not a new dataset claim. Chronos weights are not redistributed; saved predictions
and the exact upstream revision/weight hashes are supplied.

All scientific checks write to `reproduction_outputs/`. Do not rerun historical
opening scripts to obtain a supposedly new confirmation. The manuscript and
supplement disclose AI assistance, including simulated peer review.
