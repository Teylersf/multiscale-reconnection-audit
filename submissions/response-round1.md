# Response to the first-round major-revision decision

Taylor Kalin; manuscript version 1.1.0. Existing paper:
`p_MqlDy04jWkowJcek`. Title: *First-passage attribution and regional particle
energization in multiscale reconnection*.

The revision adds the requested empirical comparison using every trajectory
in the two publicly posted batches, prints the complete audited routine,
strengthens provenance and DOI verification, and moves supporting checks
to appendices. It does not claim that the complete historical Figure 6
cohort or a representative probability sample has been recovered.

## 1. Measured consequence on a documented available subcohort

We downloaded and verified all 32 posted trajectory/region files,
3,107,362,288 bytes in total. They contain 1,003 disjoint particle histories,
each with 40,764 samples. The revised Section 5 pools the individual records
before applying the source's strict final-gamma cuts: 667 intermediate,
84 high, and 252 below the lower cutoff. No particle equals a separator.
Folder names are coarse staging groups, not the final analysis bands.

Every attribution convention uses the same selected IDs, stored samples and
denominator. All 751 selected histories have positive, finite, nonzero net
gains, so no denominator filter changes the cohort. Signed regional gains
remain signed; top/bottom is retained separately from actual sheet-plus-
island work and from the source's chronological phase residual.

For the available high-energy histories, downstream mean-particle fractions
are FP 0.500318, left 0.370742, symmetric 0.370129 and right 0.369515.
The symmetric change is -13.0189 percentage points. The corresponding
fractions of total net gain are 0.490959, 0.377414, 0.393724 and 0.410033.
The latter estimand was already below one half for FP; we therefore do not
describe both estimands as undergoing the same dominance reversal.
Intermediate histories retain downstream dominance under every tested
convention, although their paired values differ. Section 5 reports the
complete table and figure, returns and signed-gain diagnostics.

Weights are explicitly unit empirical weights. The posted electron loader
uses a common physical macroparticle weight, which cancels from these
within-batch estimands under that setup. Archive release probabilities are
not supplied, so we do not manufacture inverse-inclusion weights or infer
an unbiased population correction. The posted driver expects additional
intermediate batches that are not public. Its high staging index likewise
does not certify historical completeness merely from the filename.

We checked the original Figure 6 vector artwork rather than assuming the
public union was the original cohort. Its L320 intermediate DS point is
approximately 0.681, whereas our available-cohort FP mean is 0.722947.
The high point is 0.500 and our mean is 0.500318, agreeing at three-decimal
reporting precision without an exact vector-coordinate match. These facts
are now stated explicitly. The new result is a measured paired consequence
on the documented released records, not a corrected full Figure 6 point.

Reproducibility files include `experiments/analyze_public_batches.py`,
`experiments/fetch_public_batches.py`, the 32-file inventory, compact
per-particle NPZ/CSV outputs, `results/public-batch-checks.json` and a
separately implemented summary verifier using scalar reductions without
importing the analyzer. Source-function branches, time-block joins, ID
alignment and signed closure were checked. These are computational/internal
checks and are not represented as independent human peer review.

No additional data request has been sent to the source authors as of this
response. We have not obtained private data or author confirmation, and
make no claim that the authors refused data. This revision uses all public
batch files rather than treating the on-request dataset as already held.

## 2. Print the routine

Appendix D now prints all 60 unmodified lines 344-403 of the pinned version-1
`tracer_functions.py`, with attribution, the parent-file and excerpt
SHA-256 values, and original line numbering. The no-sheet and no-subsequent-
downstream branches are included, not replaced by the simplified
counterexample formula. Readers can inspect the entire relevant function
from the manuscript itself.

## 3. Clarify the relation to the preprint

Sections 3-5 distinguish documented purpose, numerical agreement and
historical execution identity. The deposited script's header identifies
Figure 6 and supplemental trajectories as its purpose. Its posted driver
loads the L320 batches and prints the particle-mean DS and pooled phase
fractions. The listed December 2025 source version was deposited after the
November preprint; no pre-v1 execution receipt or earlier source version
has been found.

The routine reproduces all eight printed CS/DS annotations on the four
released illustrations. We additionally verified that Figs. 9, 10 and 11
match columns of the larger public batch exactly across all 40,764 samples
of gamma, x, z and region labels, including canonical-array digests.
Figure 8 was not found in either larger batch. These are direct example-
level links; neither they nor rounded agreement with a population marker
prove a complete historical cohort or a particular executed source file.
The main empirical claim remains about the posted implementation and
explicitly identified available data.

## 4. Persistent, verifiable software archive

Both disputed identifiers are registered through DataCite. Public registry
metadata, the doi.org authority/resolver and anonymous archive downloads
were checked directly. A failed lookup in another registry does not
establish DOI invalidity. Direct primary evidence is supplied:

- Source project: https://osf.io/epwtu/ and
  https://api.datacite.org/dois/10.17605/OSF.IO/EPWTU .
- Revised software record: https://zenodo.org/records/23775167 and
  https://api.datacite.org/dois/10.5281/zenodo.23775167 .
- Original software record: https://zenodo.org/records/23774456 .

The revised software snapshot is
`a8cb56dadaf6fdf6d07ce6aba0d94b9ad291f9d5`. Its 2,702,929-byte archive has
SHA-256 `82835a9d7e53c929a690cc5ccc30f3cfdc0efa75ea23344c9f6682ad737b421e`.
It includes the compact results, acquisition/analysis code, full source
provenance and independent verification. Raw gigabyte files remain at
their pinned public OSF origins; the package's explicit serial fetcher
checks complete sizes and hashes. Section 7 and references 9-10 distinguish
the software archive versions from paper publication or acceptance.

## 5. Plotting transformations

Appendix C now labels the reconstruction as inferred and separates its
evidence levels. The source clock/unit conventions corroborate the factors
t_raw/5 and D_raw/25 independently of the vector-coordinate fit: the
related tracer driver divides by wci=5, and the raw cumulative multiplier
4000 differs from the nominal plasma-time interval 160 by a factor 25.
These facts do not identify the historically executed plotting revision.
The Gaussian width 1.5, boundary handling and its historical use remain
explicitly inferred. No claim of a published factor-25 normalization error
is made. Exact vector paths, not a raster digitization, supply the numeric
comparison; complete provenance is in `data/source-claim-evidence.json`.

## 6. Focus and remaining limitations

The main text now leads with particle attribution and the executed matched
batch calculation. Field, guide-profile and caption checks are in Appendix
B, proxy reconstruction and unit checks in Appendix C, and the full
routine in Appendix D. Appendix A retains the estimator identities and
sampling limits needed to interpret the calculations.

The revision does not infer a general bias sign, a full-cohort reversal,
statistical representativeness or a uniquely recovered continuous-work
partition. The arrays have no timestamp channel, and unresolved crossings
or sign-changing work can evade endpoint allocations. Section 6 now
describes the remaining extension to the completely identified historical
cohort and separate physical-work validation, rather than presenting the
available-data comparison as an unexecuted proposal.
