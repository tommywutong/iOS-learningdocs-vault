---
title: 'getGlyphBBoxes(glyphs:count:bboxes:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/getglyphbboxes(glyphs:count:bboxes:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/getglyphbboxes(glyphs:count:bboxes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/getglyphbboxes%28glyphs%3Acount%3Abboxes%3A%29.json'
content_hash: 'sha256:15e41e3a657fb9bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# getGlyphBBoxes(glyphs:count:bboxes:)

<sub>Instance Method</sub>

Get the bounding box of each glyph in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getGlyphBBoxes(glyphs: UnsafePointer<CGGlyph>, count: Int, bboxes: UnsafeMutablePointer<CGRect>) -> Bool
```

## Parameters

- `glyphs` — A array of glyphs.

- `count` — The number of items in the `glyphs` array.

- `bboxes` — On return, the bounding boxes for each glyph.

## Return Value

`false` if bounding boxes can’t be retrieved for any reason; `true`  otherwise.

## See Also

### Working with Glyphs

- [CGFontGetNumberOfGlyphs](numberofglyphs.md) — Returns the number of glyphs in a font.
- [CGFontCopyGlyphNameForGlyph](<name(for_).md>) — Returns the glyph name of the specified glyph in the specified font.
- [CGFontGetGlyphWithGlyphName](<getglyphwithglyphname(name_).md>) — Returns the glyph for the glyph name associated with the specified font object.
- [CGFontGetGlyphAdvances](<getglyphadvances(glyphs_count_advances_).md>) — Gets the advance width of each glyph in the provided array.
- [CGGlyph](../cgglyph.md) — An index into the internal glyph table of a font.
- [kCGGlyphMax](../kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](../cgglyph.md).
- [CGFontIndex](../cgfontindex.md) — An index into a font table.
- [kCGFontIndexMax](../kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](../cgfontindex.md).
- [kCGFontIndexInvalid](../kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
