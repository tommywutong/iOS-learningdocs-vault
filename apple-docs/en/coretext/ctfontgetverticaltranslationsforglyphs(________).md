---
title: 'CTFontGetVerticalTranslationsForGlyphs(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetverticaltranslationsforglyphs(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetverticaltranslationsforglyphs(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetverticaltranslationsforglyphs%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0c7dcf6556d5377f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetVerticalTranslationsForGlyphs(_:_:_:_:)

<sub>Function</sub>

Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetVerticalTranslationsForGlyphs(_ font: CTFont, _ glyphs: UnsafePointer<CGGlyph>, _ translations: UnsafeMutablePointer<CGSize>, _ count: CFIndex)
```

## Parameters

- `font` — The font reference.

- `glyphs` — An array of `count` number of glyphs.

- `translations` — On output, the computed origin offsets in an array of `count` number of [CGSize](../corefoundation/cgsize.md) objects.

- `count` — The capacity of the `glyphs` and `translations` buffers.

## See Also

### Getting Glyph Data

- [CTFontCreatePathForGlyph](<ctfontcreatepathforglyph(______).md>) — Creates a path for the specified glyph.
- [CTFontGetGlyphWithName](<ctfontgetglyphwithname(____).md>) — Returns the glyph for the specified name.
- [CTFontGetBoundingRectsForGlyphs](<ctfontgetboundingrectsforglyphs(__________).md>) — Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [CTFontGetAdvancesForGlyphs](<ctfontgetadvancesforglyphs(__________).md>) — Calculates the advances for an array of glyphs and returns the summed advance.
- [CTFontGetOpticalBoundsForGlyphs](<ctfontgetopticalboundsforglyphs(__________).md>) — Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
