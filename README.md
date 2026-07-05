<!-- this_file: README.md -->

# Abel

**A condensed sans that says a lot in a narrow column.**

Abel is a modern take on the condensed, flat-sided sans serif — the kind of
letter that once ran newspaper headlines and pasted-up posters. Angled
terminals and spiked stems give it character at display sizes; its even,
mono-weight stroke keeps it readable when it drops down to body text. Narrow
letters, wide reach.

Designed by **Matt Desmond** ([madtype.com](http://www.madtype.com)). Released
under the SIL Open Font License 1.1 and available on
[Google Fonts](https://fonts.google.com/specimen/Abel).

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789  &  .,;:!?

The quick brown fox jumps over the lazy dog.
NARROW LETTERS, WIDE REACH — headlines that fit.
```

## What's in this repository

This is the design-source repository — the editable masters plus a reference
build. The fonts are the product; nothing here changes their shapes.

| Path | What it is |
| --- | --- |
| `sources/Abel.glyphs` | Glyphs.app source (single master) |
| `sources/Abel.vfj` / `.vfc` | FontLab sources |
| `sources/AbelVF1.vfj` / `.vfc` | Variable-font FontLab sources |
| `sources/Abel.ttf` | Reference build (Version 2.002, 259 glyphs) |
| `old/version-1.002/` | The original 2011 release, kept for provenance |
| `OFL.txt` | License |
| `FONTLOG.txt` | Version history and authorship, per OFL convention |

## Using the font

If you just want to *use* Abel, install it from
[Google Fonts](https://fonts.google.com/specimen/Abel) or embed it:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Abel&display=swap" rel="stylesheet">
<style>body { font-family: "Abel", sans-serif; }</style>
```

To use the binary in this repo directly, grab `sources/Abel.ttf`.

## Validating a build

Every font here parses cleanly, carries the name records a released font needs,
and declares the OFL. The check runs in CI on every push and is one command
locally:

```bash
pip install fonttools
python tests/validate_fonts.py
```

It reports one line per font (`OK` / `FAIL`) and exits non-zero if any font is
malformed or missing its license metadata.

## Editing

The masters need their respective editors — [Glyphs](https://glyphsapp.com) for
`.glyphs`, [FontLab](https://www.fontlab.com) for `.vfj`/`.vfc`. After editing,
re-export the TTF and run the validator before committing.

## License

Abel is licensed under the [SIL Open Font License 1.1](OFL.txt), with Reserved
Font Name *Abel*. You can use, study, modify, and redistribute it freely,
including bundling it with your own work. See `OFL.txt` for the full terms and
`FONTLOG.txt` for the modification convention.