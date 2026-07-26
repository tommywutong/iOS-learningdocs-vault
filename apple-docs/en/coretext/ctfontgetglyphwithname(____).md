---
title: 'CTFontGetGlyphWithName(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetglyphwithname(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetglyphwithname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetglyphwithname%28_%3A_%3A%29.json'
content_hash: 'sha256:bd791e4f16a3b2c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetGlyphWithName(_:_:)

<sub>Function</sub>

Returns the glyph for the specified name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetGlyphWithName(_ font: CTFont, _ glyphName: CFString) -> CGGlyph
```

## Parameters

- `font` — The font reference.

- `glyphName` — The glyph name as a `CFString` object.

## Return Value

The glyph value for the named glyph as a [CGGlyph](../coregraphics/cgglyph.md) object, or if the glyph name is not recognized, the `.notdef` glyph index value.

## Discussion

The returned `CGGlyph` object can be used with any of the subsequent glyph data accessors or directly with Core Graphics.

## See Also

### Getting Glyph Data

- [CTFontCreatePathForGlyph](<ctfontcreatepathforglyph(______).md>) — Creates a path for the specified glyph.
- [CTFontGetBoundingRectsForGlyphs](<ctfontgetboundingrectsforglyphs(__________).md>) — Calculates the bounding rects for an array of glyphs and returns the overall bounding rectangle for the glyph run.
- [CTFontGetAdvancesForGlyphs](<ctfontgetadvancesforglyphs(__________).md>) — Calculates the advances for an array of glyphs and returns the summed advance.
- [CTFontGetOpticalBoundsForGlyphs](<ctfontgetopticalboundsforglyphs(__________).md>) — Calculates the optical bounds for an array of glyphs and returns the overall optical bounds for the run.
- [CTFontGetVerticalTranslationsForGlyphs](<ctfontgetverticaltranslationsforglyphs(________).md>) — Calculates the offset from the default (horizontal) origin to the vertical origin for an array of glyphs.
