# Baseline, provenance and reproduction

## Checks executed for this agenda

On 8 October 2026, at community revision `56b66d58297deca1d7dd130247d720e960f77a37`:

1. Compared all 16 manuscript build-source files listed in `upstream/manifest.json` byte-for-byte against the supplied OpenAI revision. Their SHA-256 hashes also matched the manifest.
2. Executed `python3 scripts/audit_pair_candidate.py --check docs/research/community-pair-arithmetic.json` in a fresh community checkout. It passed, reporting independent moments, the complete child ledger, assembly and Lean source binding.
3. Checked the agenda's elementary rank-ledger and rational comparisons with `python3 scripts/check_baseline.py`.

Step 2 executes the upstream audit implementation. It reconstructs the ledger from stored profiles and checks rational bounds and generated Lean source. It does **not** regenerate the physical networks, build Lean, independently derive the 47 assembly conditions, or prove the analytic and tape interfaces. No full `make verify` run was performed for this agenda.

`evidence/baseline.json` contains transcribed numerical data with an explicit scope statement. `sources.json` pins the source revisions and hashes of the selected evidence. No third-party circuit code or manuscript is vendored here.

## Reproduce the arithmetic audit

Use a fresh working directory and Python 3.11 or later:

```sh
git clone https://github.com/CrocSwap/integer-mult-bounds.git integer-mult-bounds-source
cd integer-mult-bounds-source
git checkout --detach 56b66d58297deca1d7dd130247d720e960f77a37
python3 scripts/audit_pair_candidate.py --check docs/research/community-pair-arithmetic.json
```

For physical replay and formal builds, follow that checkout's `docs/reproducibility.md` and `docs/ci-verification.md`. Preserve the distinction between arithmetic-only checks and full producer regeneration. The upstream Makefile specifies sequential verification because some steps regenerate certificates used by others.

## Validate the agenda

From this repository:

```sh
python3 scripts/check_baseline.py
```

The GitHub workflow also validates `agenda.json` using the Public Observatory schema. These checks validate the repository and its elementary deductions; they do not certify a multiplication algorithm.

## Updating the checkpoint

Update the source revision, file hashes, numerical data and source-dependent text together. Retain the old revision in git history. Record exactly which commands were run, their results and any inherited assumptions. A larger number in an unreviewed contribution is a candidate until its evidence has been examined.
