# When More Predictions Cover Less: Accuracy and Coverage under Ratio Risk

Anonymous manuscript source, experiments, and numerical evidence.

The paper studies acceptance utility under a ratio-risk cap. Its original
external test is preserved. A new retrospective experiment asks whether better
full-coverage accuracy removes the difference between row and demand coverage.
It refits three predictor-specific error heads and one common demand head;
no original selector is reused for a changed predictor.

## Complete repository

This repository includes manuscript source, experiment code, fitted model
objects, saved predictions, calibration inputs, sufficient statistics, and
verification scripts. Source and PDF files can be viewed directly. Numerical
assets are packaged into 53 parts under `data_parts/` to support reliable
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
