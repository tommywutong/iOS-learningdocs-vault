---
title: 'name(for:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/name(for:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/name(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/name%28for%3A%29.json'
content_hash: 'sha256:d713463bd3b17af9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# name(for:)

<sub>Instance Method</sub>

Returns the glyph name of the specified glyph in the specified font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func name(for glyph: CGGlyph) -> CFString?
```

## Parameters

- `glyph` — The glyph whose name is desired.

## Return Value

The name of the specified glyph, or `nil` if the glyph isn’t associated with the font object.

## See Also

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontGetGlyphWithGlyphName](<getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGFontGetGlyphAdvances](<getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [CGGlyph](../cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](../kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](../cgglyph.md).
- [CGFontIndex](../cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](../kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](../cgfontindex.md).
- [kCGFontIndexInvalid](../kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
