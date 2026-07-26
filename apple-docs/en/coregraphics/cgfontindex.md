---
title: CGFontIndex
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfontindex
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfontindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfontindex.json'
content_hash: 'sha256:af89254b7b1ee25c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFontIndex

<sub>Type Alias</sub>

An index into a font table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGFontIndex = UInt16
```

## Discussion

This integer type provides an additional way to specify a glyph identifier. [CGFontIndex](cgfontindex.md) is equivalent to [CGGlyph](cgglyph.md), and you can use constants of either type interchangeably.

## See Also

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](cgfont/numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontCopyGlyphNameForGlyph](<cgfont/name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<cgfont/getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<cgfont/getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGFontGetGlyphAdvances](<cgfont/getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [CGGlyph](cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](cgglyph.md).
- [kCGFontIndexMax](kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](cgfontindex.md).
- [kCGFontIndexInvalid](kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
