---
title: 'CTFontGetAdvancesForGlyphs(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetadvancesforglyphs(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetadvancesforglyphs(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetadvancesforglyphs%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:503747d83082966b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetAdvancesForGlyphs(_:_:_:_:_:)

<sub>Function</sub>

Calculates the advances for an array of glyphs and returns the summed advance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetAdvancesForGlyphs(_ font: CTFont, _ orientation: CTFontOrientation, _ glyphs: UnsafePointer<CGGlyph>, _ advances: UnsafeMutablePointer<CGSize>?, _ count: CFIndex) -> Double
```

## Parameters

- `font` — The font reference.

- `orientation` — The intended drawing orientation of the glyphs. Used to determined which glyph metrics to return.

- `glyphs` — An array of `count` number of glyphs.

- `advances` — An array of `count` number of [CGSize](../corefoundation/cgsize.md) objects to receive the computed glyph advances. If `NULL`, only the overall advance is calculated.

- `count` — The capacity of the `glyphs` and `advances` buffers.

## Return Value

The summed glyph advance of an array of glyphs.

## Discussion

Individual glyph advances are passed back via the `advances` parameter. These are the ideal metrics for each glyph scaled and transformed in font space.

## See Also

### Getting Glyph Data

- [CTFontCreatePathForGlyph](<ctfontcreatepathforglyph(______).md>) — Creates a path for the specified glyph.
- [CTFontGetGlyphWithName](<ctfontgetglyphwithname(____).md>) — Returns the glyph for the specified name.
- [CTFontGetBoundingRectsForGlyphs](<ctfontgetboundingrectsforglyphs(__________).md>) — Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [CTFontGetOpticalBoundsForGlyphs](<ctfontgetopticalboundsforglyphs(__________).md>) — Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [CTFontGetVerticalTranslationsForGlyphs](<ctfontgetverticaltranslationsforglyphs(________).md>) — Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.
