<!-- this_file: CHANGELOG.md -->

# Changelog

All notable changes to this repository are recorded here. The fonts themselves
follow their own version string in the `name` table (currently 2.002); the tags
below version the *repository*.

## [Unreleased]

### Added
- Font validation script (`tests/validate_fonts.py`): every `.ttf`/`.otf`
  parses with fontTools and carries the required name records plus OFL license
  metadata. Runnable locally and under pytest.
- GitHub Actions workflow (`.github/workflows/validate.yml`) running the
  validator on every push and pull request.
- Concept icon at `docs/assets/icon.png`.

### Changed
- Rewrote `README.md`: text specimen, repository layout, install snippet,
  validation instructions, and license note.
- Expanded `.gitignore` with font-build output, Python, and generated-snapshot
  entries.

### Removed
- Untracked generated cruft `llms.txt` (a ~4.8 MB codebase snapshot) and
  `md.txt` (a stray path file). Neither belongs in version control.

### Fixed
- Repaired 7 missing tree objects in git history (referenced by the `v1.0.0`
  and `6a23c34` commits) via `git fetch --refetch`; `git fsck` is now clean.

## [1.0.1] — 2025-09-24
- Prior tagged release (font Version 2.002).

## [1.0.0]
- First tagged repository release after conversion to `.glyphs` sources.

## Font history

For the typeface's own version history and authorship, see
[`FONTLOG.txt`](FONTLOG.txt).
