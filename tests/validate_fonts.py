#!/usr/bin/env python3
# this_file: tests/validate_fonts.py
"""Sanity checks for the Abel font binaries.

Every TTF/OTF in the repo must parse with fontTools, carry the core name
records a released font needs, and declare the OFL. A font that fails here is
a font a user cannot trust, so the check is intentionally strict and loud.

Run directly (``python tests/validate_fonts.py``) or under pytest. The same
file backs the CI validation job.
"""

from __future__ import annotations

import sys
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent

# Name table IDs (OpenType spec).
FAMILY, SUBFAMILY, FULL, VERSION, PS_NAME = 1, 2, 4, 5, 6
LICENSE_DESC, LICENSE_URL = 13, 14

OFL_URL_FRAGMENT = "scripts.sil.org/OFL"


def font_files() -> list[Path]:
    """Every shipped font binary, sorted for stable output."""
    return sorted(p for ext in ("*.ttf", "*.otf") for p in ROOT.rglob(ext))


def check_font(path: Path) -> list[str]:
    """Return a list of problems for one font; empty means it passed."""
    problems: list[str] = []
    try:
        font = TTFont(path)
    except Exception as exc:  # noqa: BLE001 — a parse failure is the finding
        return [f"does not parse with fontTools: {exc}"]

    if "name" not in font:
        return ["missing 'name' table"]
    name = font["name"]

    for nid, label in (
        (FAMILY, "family (1)"),
        (SUBFAMILY, "subfamily (2)"),
        (FULL, "full name (4)"),
        (VERSION, "version (5)"),
        (PS_NAME, "PostScript name (6)"),
    ):
        if not name.getDebugName(nid):
            problems.append(f"missing name record {label}")

    if not name.getDebugName(LICENSE_DESC):
        problems.append("missing OFL license description (name 13)")
    url = name.getDebugName(LICENSE_URL) or ""
    if OFL_URL_FRAGMENT not in url:
        problems.append(f"license URL (name 14) is not the OFL URL: {url!r}")

    # OFL fonts must stay installable and embeddable: fsType bit 1 forbids that.
    if "OS/2" in font and font["OS/2"].fsType & 0x02:
        problems.append("OS/2 fsType marks the font as restricted (bit 1 set)")

    return problems


def main() -> int:
    fonts = font_files()
    if not fonts:
        print("FAIL: no .ttf/.otf font files found in repo", file=sys.stderr)
        return 1

    failed = False
    for path in fonts:
        rel = path.relative_to(ROOT)
        problems = check_font(path)
        if problems:
            failed = True
            print(f"FAIL {rel}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"OK   {rel}")

    if failed:
        print("\nFont validation failed.", file=sys.stderr)
        return 1
    print(f"\nAll {len(fonts)} font(s) valid.")
    return 0


def test_all_fonts_valid() -> None:
    """pytest entry point mirroring ``main``."""
    offenders = {
        str(p.relative_to(ROOT)): probs
        for p in font_files()
        if (probs := check_font(p))
    }
    assert not offenders, f"invalid fonts: {offenders}"


if __name__ == "__main__":
    raise SystemExit(main())
