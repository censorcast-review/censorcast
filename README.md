# When More Predictions Cover Less: Accuracy and Coverage under Ratio Risk

## Integrated v13 reproducibility source

The v12 and v13 **source code and execution protocols** are now integrated here.
This includes the three-seed M5 audit, Dominick's external trial, Bibtex and
Mediamill, direct learned gates, conditional-bound checks, and manuscript sources.
All three external tests miss their declared joint success criteria.

This update publishes source code and configuration, not the new numerical-data
archives. The current 54-page PDF (9 main pages) and compact numerical replay
package are supplied separately as the anonymous submission supplement.
Pre-existing repository assets and old PDFs are retained as historical material;
they must not be mistaken for the current integrated PDF or complete v13 inputs.
No frozen experimental code or protocol is altered to change the reported result.

## Reproduce

Use Python 3.12 and requirements-v12.txt; the non-WAPE dependencies are listed in
evidence/revision_v13_nonwape/requirements-v13.txt. Place the contents of the
current submission supplement's CENSORCAST directory into this checkout before
running numerical replay, preserving this repository's root README.md and
MANIFEST.json rather than replacing them with the supplement entrypoint. The
source manifest alone does not supply missing data.

```bash
python code/verify_release.py
OPENBLAS_NUM_THREADS=1 python code/verify_compact_m5.py --output reproduction_outputs/m5.json
OPENBLAS_NUM_THREADS=1 python code/verify_revision_v12.py --part external --output reproduction_outputs/external.json
OPENBLAS_NUM_THREADS=1 python code/verify_revision_v12.py --part theory --output reproduction_outputs/theory.json
OPENBLAS_NUM_THREADS=1 python evidence/revision_v13_nonwape/audit/verify_nonwape.py --output reproduction_outputs/nonwape.json
python code/build_paper.py --output reproduction_outputs/paper
```

The compact package supports fixed-policy M5 statistics; complete threshold and
prediction replay needs the separate large research archive. Refitting also needs
provider data. Raw Dominick's/Mulan archives are not redistributed. Source URLs
and acquisition logic are in the external/non-WAPE runners. Run training only in
new directories; never overwrite frozen evidence. The M5 and non-WAPE bootstrap
assumptions do not establish population risk guarantees.

Mixed uses case coefficient lambda=.25 for M5/Dominick's and frozen .5 for the two
non-WAPE tests; the .25 non-WAPE analysis is retrospective. Some frozen files say
v12 was unavailable at their original execution time. That historical record is
preserved; v12 has since been recovered and integrated.

The source-only MANIFEST.json records the current published source snapshot.
The complete numerical inventory belongs to the separately supplied supplement.
