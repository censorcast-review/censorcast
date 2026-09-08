# When More Predictions Cover Less: Objective Mismatch under Ratio Risk

Anonymous publication supplement accompanying the current manuscript. This
distribution is separate from the complete internal working and audit archive.

## Start here

Use Python 3.12 and an isolated environment, then install `requirements.txt`.
Run `python code/verify_public_package.py` before and after reproduction.
New reports and rebuilt figures are written only under `reproduction_outputs/`
(or a separately specified output directory); retained evidence stays unchanged. The generic `REPRODUCE_ANONYMOUS.ipynb` runs included invariant
checks, the general ratio-risk and bounded-exposure theorems, group-budget certificates, and aggregate
likelihood diagnostics, and the completed external comparison from retained
item sufficient statistics; it optionally replays saved,
already-consumed prediction caches. It never initiates a new holdout opening.
The new checks use only mathematical constructions and retained aggregate records: `verify_bounded_exposure.py`, `verify_external_budget.py`, `verify_shared_error_intervention.py`, and `verify_nb_nll_uncertainty.py`. The last check replays the paired item bootstrap from validation NLL sufficient statistics. No new model fit or policy evaluation is run.
The current manuscript can be built with `python code/build_review10_pdf.py`;
this optional step also requires `pypdf` and a LaTeX installation.

## Scientific material

- `paper/`: current manuscript source, bibliography, official conference style,
  and tables/figures; compiler logs and historical unused sections are omitted.
- `docs/standard_calibration.tex`: the ancillary fixed-family concentration bound
  and its proof; `docs/wape_worked_example.tex` retains the worked WAPE construction
  verified by `code/verify_objective_geometry.py`. `docs/supervised_controls.tex`
  retains implementation details for the supervised objective and capacity/loss controls.
  `docs/two_context_no_reversal.tex` gives the analytic two-context no-reversal argument
  under unrestricted contextwise randomized acceptance, the sole pooled ratio-risk cap,
  and the common row-coverage floor.
- `code/`: experiments and verification routines. Historical editorial utilities
  and personal notebook launchers are omitted.
- `results/`: completed numerical readouts, available model files, and audits.
- `provenance/`: input hashes, original scientific freeze records and ledgers.
- `upstream/`: data preparation and origin-alignment source, with its citations.
- `inputs/`: retained frozen forecasting object required by historical checks.

## Data availability and replay

The compact source archive does not contain all per-row prediction or feature
arrays. Cached objective/loss replay requires the seven consumed-cache archives
whose names and SHA-256 digests are retained in `provenance/REVIEW3_LINEAGE.json`.
Restore their documented relative paths, including the sibling
`evaluation_checkpoints` directory. Do not substitute raw held-out outcomes.
Observable-likelihood models are retained, but regenerating their per-row
moments requires the development-only inputs named in
`code/reproduce_observable_from_models.py`; aggregate moment audits are included.
Data preparation requirements and dataset attribution are in `upstream/` and
`provenance/input_manifest.json`.

## Public paths and immutable evidence

Result directories use scientific topics (`objectives/`, `utility_tradeoffs/`,
`nb_grid/`, and `external_audits/`). `provenance/PUBLIC_PATHS.json` resolves
original paths to their byte-identical public copies. Changed executable
publication copies have separate hashes; their unmodified input sources are
retained under `provenance/frozen_sources/`. Historical JSON records keep their
original path strings and hashes as provenance, rather than pretending that
renamed publication derivatives existed at preregistration.

## Distribution transformations

`ANONYMIZATION_MANIFEST.json` records an original SHA-256 and a public SHA-256 for
each copied or transformed file, plus explicit exclusions and the provenance of
the newly authored generic notebook. Original research files are not changed by
packaging. Historical hash ledgers continue to describe the original artifacts;
they are not rewritten to claim that publication derivatives were frozen.
All scientific files listed in the guardian freeze are preserved byte for byte.
Two conversational administration fields in the opening receipt are rendered in
English in the public derivative, with both hashes disclosed. Bibliographic
authors and public dataset attribution are preserved.

Historical code paths that perform original experiments are provided for
transparency. Re-running a historical opening is not a new independent test.
The manuscript distinguishes the completed frozen external comparison from
exploratory analyses. The public external replay regenerates all prespecified
primary contrasts and 48 secondary bounds from item sufficient statistics; it
does not regenerate forecasts or open raw external arrays. This distinction
limits the reproduction claim to the recorded statistical evaluation.

## External confirmation provenance

`provenance/external_confirmation/PUBLIC_PROTOCOL.json` documents the two
policies, fixed thresholds, 23-day primary window, and evaluation rules.
`PLAN_EVOLUTION.md` and `PLAN_EVOLUTION.json` disclose the pre-opening policy-pair replacement with exact timestamps and source hashes. `PUBLIC_PROTOCOL.json` is a neutral current rendering; it is not a new freeze record.

`FROZEN_PLAN_ORIGINAL.json` and the archived prior plan are immutable historical
pre-opening records: their pending/unopened status describes the time of
preregistration. `SCIENTIFIC_RECEIPT.json` records the completed comparison,
its actual result hash, and the approved independent comparison after the earlier
held-out operating checks failed. It does not grant a deployment certificate.
The original plans and original frozen `freeze_plan.py` retain their historical wording, including references to simulated review, solely to preserve their recorded bytes. Active explanatory copies use neutral terminology and point to their original hashes. These archival phrases are provenance, not author identifiers, and are not silently edited.

`EXTERNAL_TRANSFER.json` maps all 27 frozen dependencies to their public paths
and original hashes. Twenty-six are preserved byte for byte. The administrative
access ledger is omitted with its original hash disclosed; exact personal
approval text and mutable ledgers are excluded. Relocated evaluator, predictor,
and test source remains byte-identical to the frozen implementation.
The default notebook runs only sufficient-statistic replay. The predictor and
historical opening source are retained for inspection; their inclusion does not
initiate or authorize a new holdout opening.
