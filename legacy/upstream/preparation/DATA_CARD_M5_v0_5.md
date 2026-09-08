# Data card: M5 boundary for CENSORCAST v0.5

## Source

- Dataset: M5 Forecasting Accuracy
- Fixed record: Zenodo `10203108`
- DOI: `10.5281/zenodo.10203108`
- Acquired files: `calendar.csv`, `sales_train_evaluation.csv`,
  `sell_prices.csv`
- Integrity: provider MD5 plus locally recorded SHA-256

The source is independent of FreshRetailNet.  No v0.4 guardian or
FreshRetailNet eval/test artifact is accepted by the v0.5 preparation program.

## Unit of separation

The split unit is `item_id`, not an individual store-day.  All store series for
one product remain together.  The manifest exposes design item IDs but records
only set hashes for guardian and external items.

## Outcome visibility

- Design: truth and mechanically censored observations through day 1,913.
- Guardian context: observed history through day 1,553.
- Guardian sealed outcomes: days 1,554–1,913.
- External context: observed history through day 1,913.
- External sealed outcomes: days 1,914–1,941.

Creating a sealed shard is a blind custodial transformation, not statistical
opening.  Opening is defined by a separate immutable receipt and access-ledger
transition in a future runner.

## Known limitations

M5 has no inventory-on-hand field and cannot reveal naturally unmet demand.
The controlled cap creates known hidden demand and allows exact recovery
evaluation, but its operational realism is limited.  Results must be described
as controlled-censoring evidence and not as proof of natural stockout recovery.

Public benchmark data can never be secret in the ordinary sense.  The seal is
therefore procedural and cryptographic (hashes, allowlists and one-way receipts),
not a claim that the bytes are unknowable.

