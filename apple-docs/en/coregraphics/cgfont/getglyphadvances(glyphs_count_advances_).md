---
title: 'getGlyphAdvances(glyphs:count:advances:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/getglyphadvances(glyphs:count:advances:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/getglyphadvances(glyphs:count:advances:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/getglyphadvances%28glyphs%3Acount%3Aadvances%3A%29.json'
content_hash: 'sha256:06681383cc03b7ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# getGlyphAdvances(glyphs:count:advances:)

<sub>Instance Method</sub>

Gets the advance width of each glyph in the provided array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getGlyphAdvances(glyphs: UnsafePointer<CGGlyph>, count: Int, advances: UnsafeMutablePointer<Int32>) -> Bool
```

## Parameters

- `glyphs` — An array of glyphs.

- `count` — The number of glyphs in the array.

- `advances` — On output, an array of advance widths for the provided glyphs.

## Return Value

[true](../../swift/true.md) unless the advance widths can’t be provided for some reason.

## See Also

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontCopyGlyphNameForGlyph](<name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphBBoxes](<getglyphbboxes(glyphs_count_bboxes_).md>) — Get the bounding box of each glyph in an array.
- [CGGlyph](../cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](../kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](../cgglyph.md).
- [CGFontIndex](../cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](../kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](../cgfontindex.md).
- [kCGFontIndexInvalid](../kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
