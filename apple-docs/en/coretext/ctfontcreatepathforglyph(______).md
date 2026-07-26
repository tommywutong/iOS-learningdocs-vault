---
title: 'CTFontCreatePathForGlyph(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreatepathforglyph(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatepathforglyph(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatepathforglyph%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7b5d480c49b5a4e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreatePathForGlyph(_:_:_:)

<sub>Function</sub>

Creates a path for the specified glyph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreatePathForGlyph(_ font: CTFont, _ glyph: CGGlyph, _ matrix: UnsafePointer<CGAffineTransform>?) -> CGPath?
```

## Parameters

- `font` — The font reference.

- `glyph` — The glyph.

- `matrix` — An affine transform applied to the path. Can be `NULL`. If `NULL`, [CGAffineTransformIdentity](../coregraphics/cgaffinetransformidentity.md) is used.

## Return Value

A CGPath object containing the glyph outlines, `NULL` on error. Must be released by caller.

## Discussion

Creates a path from the outlines of the glyph for the specified font. The path reflects the font point size, matrix, and transform parameter, applied in that order. The transform parameter is most commonly be used to provide a translation to the desired glyph origin.

## See Also

### Getting Glyph Data

- [CTFontGetGlyphWithName](<ctfontgetglyphwithname(____).md>) — Returns the glyph for the specified name.
- [CTFontGetBoundingRectsForGlyphs](<ctfontgetboundingrectsforglyphs(__________).md>) — Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [CTFontGetAdvancesForGlyphs](<ctfontgetadvancesforglyphs(__________).md>) — Calculates the advances for an array of glyphs and returns the summed advance.
- [CTFontGetOpticalBoundsForGlyphs](<ctfontgetopticalboundsforglyphs(__________).md>) — Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [CTFontGetVerticalTranslationsForGlyphs](<ctfontgetverticaltranslationsforglyphs(________).md>) — Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.
