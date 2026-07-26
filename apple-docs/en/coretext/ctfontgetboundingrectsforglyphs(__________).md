---
title: 'CTFontGetBoundingRectsForGlyphs(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetboundingrectsforglyphs(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetboundingrectsforglyphs(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetboundingrectsforglyphs%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ab16ccae10a83317'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetBoundingRectsForGlyphs(_:_:_:_:_:)

<sub>Function</sub>

Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetBoundingRectsForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ boundingRects: UnsafeMutablePointer<CGRect>?, _ count: CFIndex) -> CGRect
```

## Parameters

- `font` — The font reference.

- `orientation` — The intended drawing orientation of the glyphs. Used to determined which glyph metrics to return.

- `glyphs` — An array of `count` number of glyphs.

- `boundingRects` — On output, the computed glyph rectangles in an array of `count` number of [CGRect](../corefoundation/cgrect.md) objects. If `NULL`, only the overall bounding rectangle is calculated.

- `count` — The capacity of the `glyphs` and `boundingRects` buffers.

## Return Value

The overall bounding rectangle for an array or run of glyphs. Returns [CGRectNull](../coregraphics/cgrectnull.md) on error.

## Discussion

The bounding rectangles of the individual glyphs are returned through the `boundingRects` parameter. These are the design metrics from the font transformed in font space.

## See Also

### Getting Glyph Data

- [CTFontCreatePathForGlyph](<ctfontcreatepathforglyph(______).md>) — Creates a path for the specified glyph.
- [CTFontGetGlyphWithName](<ctfontgetglyphwithname(____).md>) — Returns the glyph for the specified name.
- [CTFontGetAdvancesForGlyphs](<ctfontgetadvancesforglyphs(__________).md>) — Calculates the advances for an array of glyphs and returns the summed advance.
- [CTFontGetOpticalBoundsForGlyphs](<ctfontgetopticalboundsforglyphs(__________).md>) — Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [CTFontGetVerticalTranslationsForGlyphs](<ctfontgetverticaltranslationsforglyphs(________).md>) — Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.
