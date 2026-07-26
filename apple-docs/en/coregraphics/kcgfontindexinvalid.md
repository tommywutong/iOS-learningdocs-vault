---
title: kCGFontIndexInvalid
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgfontindexinvalid
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgfontindexinvalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgfontindexinvalid.json'
content_hash: 'sha256:9b59ec2ac08fce16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGFontIndexInvalid

<sub>Global Variable</sub>

An invalid font index (a value which never represents a valid glyph).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCGFontIndexInvalid: CGFontIndex { get }
```

## See Also

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](cgfont/numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontCopyGlyphNameForGlyph](<cgfont/name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<cgfont/getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<cgfont/getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGFontGetGlyphAdvances](<cgfont/getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [CGGlyph](cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](cgglyph.md).
- [CGFontIndex](cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](cgfontindex.md).
