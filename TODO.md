<!-- this_file: TODO.md -->

# TODO

Larger ideas beyond this modernization pass. The fonts are the product, so
anything here that touches shapes is a design decision for the author, not a
mechanical change.

## Build reproducibility
- [ ] Add a `fontmake`/`gftools` build script that regenerates `Abel.ttf` from
      `sources/Abel.glyphs`, so binaries provably match sources.
- [ ] Wire that build into CI and attach the built font as a release artifact.
- [ ] Reconcile the two source lineages (`.glyphs` vs FontLab `.vfj`/`.vfc`) —
      document which is canonical, or drop the stale one.

## Quality gates
- [ ] Run `gftools qa` / `fontbakery` (Google Fonts profile) in CI and record
      the report.
- [ ] Add `ufo`/designspace export if targeting a Google Fonts onboarding PR.

## Variable font
- [ ] Clarify the status of `sources/AbelVF1.*` — is a shipping variable Abel
      intended? If so, define the axis (likely Weight) and build a VF binary.

## Housekeeping
- [ ] Add `TRADEMARKS.md` (noted as long-outstanding in the old README).
- [ ] Consider Git LFS for committed binaries if the repo keeps accreting them.
- [ ] Decide whether `old/version-1.002/` stays in-tree or moves to a tagged
      archive.
