# Response to the second-round minor-revision decision

Taylor Kalin; manuscript version 1.2.0. Existing paper:
`p_MqlDy04jWkowJcek`. Title: *First-passage attribution and regional particle
energization in multiscale reconnection*.

This revision adds the four scientific/reporting items below and the dated
author data request described in item 5. It preserves the distinction
between a measured consequence on the released histories and a correction
of the full historical Figure 6 cohort. No author reply or additional data
is represented as received.

## 1. Complete execution of the pinned original function

Section 5 now reports a direct execution of the complete unchanged
60-line Appendix D function on all 1,003 released input histories. The
validation rereads the 32 local source files after checking their recorded
sizes and complete SHA-256 values. Stored float32 Lorentz factors and exact
integer region values are assembled in a memory-bounded form; the original
module's unrelated top-level filesystem operations are not executed.

The function itself selects 667 intermediate and 84 high-band histories,
excluding 252 below the source's lower cut. Its two selected-index lists
and all six returned regional-gain arrays match the streaming calculation
exactly: zero mismatching values and zero absolute difference. This
supersedes the earlier validation limited to 32 systematic histories per
staging batch; the earlier tests remain supporting checks.

The source's native sum-of-phase-terms denominator is also distinguished
from the common endpoint denominator used for the paired comparisons.
Using that source sum changes the downstream particle mean by only
`-6.55764e-11` in the intermediate band and `-3.35025e-9` in the high band.
These arithmetic effects are separate from the attribution shifts.

Evidence: `experiments/validate_full_source_and_bootstrap.py` and
`results/full-source-validation-v1.2.0.json`. The original v1.1 per-particle
exports and previously versioned results remain unchanged.

## 2. Paired resampling diagnostics under both estimands

Section 5 adds 20,000 paired history-bootstrap replicates per energy band,
using fixed seed 20261029, separately identified PCG64 streams, and linear
2.5th/97.5th percentile extraction. Each draw resamples complete history IDs
with replacement from the already selected band. Identical resampled IDs
are used for first passage, left, symmetric and right conventions and for
both estimands. Regional gains remain signed. The energy-share denominator
is recomputed from the same resampled histories rather than independently
resampled or held fixed.

For the available high band, the symmetric-minus-first-passage
particle-mean difference is -13.0189 percentage points, with a conditional
empirical 2.5--97.5 percentile range of [-20.4864, -6.6663] points. The
corresponding total-net-gain-share change is -9.7236 points, with range
[-17.2950, -3.3956]. The full table reports both bands, all three
alternatives and both estimands, including the intermediate right-rule
particle-mean change of +0.4888 points and its range [-4.3746, +5.8511].

These are explicitly **conditional iid empirical bootstrap percentile
ranges**, not population confidence intervals, significance tests or
physical uncertainty bounds. Release probabilities are unknown, particles
share one simulation and can be correlated, and iid history resampling
can understate uncertainty. No independent-run or defensible cluster
replication is supplied. The ranges do not repair archive selection,
resolve temporal/mask cadence or certify continuous electric work. No
population-significance inference is made from whether a range includes
zero.

Evidence: `results/paired-history-bootstrap-v1.2.0.json`, its replicate
NPZ and complete range-table CSV. A separate compact-only implementation
reproduces all 240,000 shift values using multiplicities and separate
full-history/first-passage arithmetic, with maximum absolute discrepancy
`1.6515e-15`; all summary and table values agree. Its receipt is
`results/full-source-bootstrap-independent-v1.2.0.json`. These are
computational checks, not independent human peer review. Reference [11]
now cites Efron's primary bootstrap paper.

## 3. Staging-folder composition and release selection

Section 5 now makes the mixture visible. The intermediate-band selection
contains 265 records from `inter_energy/p008` and 402 from
`high_energy/p000`. The folder names describe coarse staging groups,
rather than the final strict analysis bands.

For the former group, the downstream first-passage and symmetric particle
means are 0.885079 and 0.916422, a paired increase of 3.13425 percentage
points. For the latter intermediate-band group, they are 0.616068 and
0.541209, a decrease of 7.48594 points. Their observed record-count mixture
gives the pooled -3.26652-point change. Thus composition can matter even
for the sign of the available-sample comparison.

This is a measured mixture of released records. Neither physical equal
macroparticle weights nor filename indices identify archive inclusion
probabilities. Missing conditional means and the historical mixture remain
unknown; no sign or magnitude of full-population selection bias is
inferred. The newly added conditional bootstrap cannot repair that gap.

The revision continues to report that the available intermediate FP mean
does not reproduce the original Figure 6 point, whereas the high-band
agreement holds only at three-decimal reporting precision. It does not
favor an unverified historical explanation such as a particular missing
batch or analysis revision.

## 4. Direct DOI and archive verification

Section 7 now gives the precise direct checks for references [9] and [10].
On 29 October 2026 the public DataCite record for software v1.0.0 returned
HTTP 200 with state `findable` at 18:26:49 UTC, and doi.org resolved it to
Zenodo record 23774456 with HTTP 200 at 18:26:52 UTC. Software v1.1.0
returned the same positive DataCite state at 19:12:20 UTC and resolved to
record 23775167 at 19:12:22 UTC. The doi.org registration-authority
responses identify DataCite.

Direct primary links are:

- https://api.datacite.org/dois/10.5281/zenodo.23774456 and
  https://zenodo.org/records/23774456 .
- https://api.datacite.org/dois/10.5281/zenodo.23775167 and
  https://zenodo.org/records/23775167 .

Timestamped receipts also bind the anonymous archive checksums. A Crossref
`not_found` result does not invalidate these independently verified
DataCite registrations. The additional software v1.2.0 archive is published
at https://doi.org/10.5281/zenodo.23777646 , snapshot
`83660394cdbd789f297c6da5f18470c00942254a`; reference [12] and the matching
public receipt identify it. Software publication is not paper acceptance.

## 5. Dated request to the source author; reply pending

On 29 October 2026 at 19:58:41 UTC, Taylor Kalin sent the requested email
from teylersf@gmail.com to Alexander Velberg at velberg@mit.edu, with subject
“Fig. 6 data and analysis provenance request for arXiv:2511.15988v1”. The
request seeks the missing Figure 6 cohort histories, weights and analysis
provenance. It was sent once from the prepared draft and verified in the
sender's Sent record at 19:59:19 UTC. The public-safe evidence is
`submissions/author-correspondence.json`.

Section 7 now records the dated request and pending outcome. No author
reply, additional data or endorsement has been received as of the recorded
verification. The Sent record confirms dispatch; it does not certify that
the recipient read or received the message. Consequently the released
sample remains the empirical scope of this revision. No refusal or
negative author response is inferred, and no awaited outcome is used to
change the reported calculations.
