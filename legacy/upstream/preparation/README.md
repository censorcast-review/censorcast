# CENSORCAST v0.5 — M5 independent protocol

This package prepares a new cross-dataset research boundary after the v0.4
FreshRetailNet guardian failure.

## What this package does

1. verifies the immutable v0.5 protocol and its own source hash;
2. downloads three checksum-pinned M5 files from Zenodo;
3. partitions products into disjoint design, guardian and external groups;
4. applies one fixed prequential censoring mechanism;
5. writes design/context/sealed outcome shards atomically;
6. removes the transient raw sales copy after verification;
7. emits manifests, hashes and a zero-use access ledger;
8. stops before any model training or sealed-outcome metric.

## What this package does not do

- It does not reuse the v0.4 guardian.
- It does not open FreshRetailNet eval/test.
- It does not train or select a forecasting model.
- It does not evaluate the new guardian or external split.
- It does not issue a certificate.

## Colab workflow

Open `RUN_CENSORCAST_V0_5_PREPARE_M5.ipynb` and run through the sealed
preflight.  Return that output for audit before changing the manual preparation
flag.  Data preparation requires a CPU runtime, at least 3 GB free Drive/local
space and roughly 350 MB of network download.

After preparation, return the final audit.  Design-only model development will
be supplied as a separate notebook so that it cannot accidentally import the
sealed guardian or external shards.

