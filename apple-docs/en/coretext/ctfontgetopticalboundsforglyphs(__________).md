---
title: 'CTFontGetOpticalBoundsForGlyphs(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetopticalboundsforglyphs(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetopticalboundsforglyphs(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetopticalboundsforglyphs%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:374257e886de9617'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetOpticalBoundsForGlyphs(_:_:_:_:_:)

<sub>Function</sub>

Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetOpticalBoundsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>?, _ count: CFIndex, _ options: CFOptionFlags) -> CGRect
```

## Parameters

- `font` — The font reference.

- `glyphs` — An array of glyphs.

- `boundingRects` — An array of [CGRect](../corefoundation/cgrect.md)s to receive the computed glyph bounds. This parameter can be `NULL`, in which case the function only calculates the overall bounding rectangle.

- `count` — The capacity of the `glyphs` and `boundingRects` buffers.

- `options` — Reserved, set to zero.

## Return Value

This function returns the overall bounding rectangle for an array of glyphs. The `boundingRects` parameter returns the bounding rectangles of the individual glyphs. These rectangles are the design metrics from the font transformed in font space.

## Discussion

Fonts may specify the optical edges of glyphs that can be used to make the edges of lines of text line up in a more visually pleasing way. This function returns bounding rectangles that correspond to these specifications if the font provides them; otherwise, it returns typographic bounding rectangles, composed of the font’s ascender and descender and a glyph’s advance width.

## See Also

### Getting Glyph Data

- [CTFontCreatePathForGlyph](<ctfontcreatepathforglyph(______).md>) — Creates a path for the specified glyph.
- [CTFontGetGlyphWithName](<ctfontgetglyphwithname(____).md>) — Returns the glyph for the specified name.
- [CTFontGetBoundingRectsForGlyphs](<ctfontgetboundingrectsforglyphs(__________).md>) — Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [CTFontGetAdvancesForGlyphs](<ctfontgetadvancesforglyphs(__________).md>) — Calculates the advances for an array of glyphs and returns the summed advance.
- [CTFontGetVerticalTranslationsForGlyphs](<ctfontgetverticaltranslationsforglyphs(________).md>) — Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.
