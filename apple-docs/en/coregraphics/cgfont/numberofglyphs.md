---
title: numberOfGlyphs
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/numberofglyphs
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/numberofglyphs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/numberofglyphs.json'
content_hash: 'sha256:d929852cbb9066d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# numberOfGlyphs

<sub>Instance Property</sub>

Returns the number of glyphs in a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfGlyphs: Int { get }
```

## See Also

### Working with Glyphs

- [CGFontCopyGlyphNameForGlyph](<name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGFontGetGlyphAdvances](<getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [CGGlyph](../cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](../kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](../cgglyph.md).
- [CGFontIndex](../cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](../kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](../cgfontindex.md).
- [kCGFontIndexInvalid](../kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
