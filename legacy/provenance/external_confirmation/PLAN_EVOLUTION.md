# Pre-opening policy-pair replacement

The two-policy plan was replaced once before the recorded external opening. The earlier pair was direct excess versus demand-normalized error with denominator floor 0.25. After diagnostics on the already-consumed held-out partition, the final pair became composed excess (lambda = 1) versus mixed utility (lambda = 0.25). The final pair was selected to test transfer of a previously observed contrast; it does not test demand-normalized optimality.

| Event | UTC timestamp |
| --- | --- |
| Earlier pair frozen, still pending approval | 2026-09-06T14:29:07.055512+00:00 |
| Replacement pair frozen | 2026-09-06T14:47:36.694813+00:00 |
| External partition opened once | 2026-09-06T15:10:45.169571+00:00 |
| Fixed comparison completed | 2026-09-06T15:13:38.277616+00:00 |

The replacement occurred before external access. The final plan records that no external access had occurred; the opening receipt is later than both freezes. The earlier plan is preserved byte for byte as `PRIOR_FROZEN_PLAN_ORIGINAL.json`; the executed plan is `FROZEN_PLAN_ORIGINAL.json`. Only the final pair was evaluated, with zero new fits and zero threshold searches. The superseded pair was not tested.

Earlier-plan SHA-256: `390e11d0494c7fe493545063001c8dd479d50cd4a3f4fd00bf836e60dec9cd19`.

Executed-plan SHA-256: `8173b957c2c1d4fdb3a962862a4435a1531e378569f8a6602d02af97a0dd7f1d`.

`PLAN_EVOLUTION.json` provides the complete policy fields, times, and hash pointers. `PUBLIC_PROTOCOL.json` renders the current explanation neutrally. Exact original plans and archived frozen source retain their original editorial wording to keep preregistration hashes valid; this is historical evidence, not a revised record. Active publication copies are separately hashed.
