---
title: CGGlyph
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgglyph
source_url: 'https://developer.apple.com/documentation/coregraphics/cgglyph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgglyph.json'
content_hash: 'sha256:168cea0af5f71e47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGlyph

<sub>Type Alias</sub>

An index into the internal glyph table of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGGlyph = CGFontIndex
```

## Discussion

When drawing text, you typically specify a sequence of characters. However, Core Graphics also allows you to use [CGGlyph](cgglyph.md) values to specify glyphs. In either case, Core Graphics renders the text using font data provided by the Apple Type Services (ATS) framework.

You provide [CGGlyph](cgglyph.md) values to the functions [CGContextShowGlyphs](<cgcontext/showglyphs(g_count_).md>) and [CGContextShowGlyphsAtPoint](<cgcontext/showglyphsatpoint(x_y_glyphs_count_).md>). These functions display an array of glyphs at the current text position or at a position you specify, respectively.

## See Also

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](cgfont/numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontCopyGlyphNameForGlyph](<cgfont/name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<cgfont/getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<cgfont/getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGFontGetGlyphAdvances](<cgfont/getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [kCGGlyphMax](kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](cgglyph.md).
- [CGFontIndex](cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](cgfontindex.md).
- [kCGFontIndexInvalid](kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
