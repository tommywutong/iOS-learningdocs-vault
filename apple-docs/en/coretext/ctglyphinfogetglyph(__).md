---
title: 'CTGlyphInfoGetGlyph(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctglyphinfogetglyph(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfogetglyph(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfogetglyph%28_%3A%29.json'
content_hash: 'sha256:12f06dea5e22a9d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfoGetGlyph(_:)

<sub>Function</sub>

Retrieves the glyph for a glyph info, if that object exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTGlyphInfoGetGlyph(_ glyphInfo: CTGlyphInfo) -> CGGlyph
```

## Parameters

- `glyphInfo` — The glyph info object from which to get the glyph.

## Return Value

A [CGGlyph](../coregraphics/cgglyph.md) value, if the glyph info object was created with a font; otherwise, `0`.

## See Also

### Getting GlyphInfo Data

- [CTGlyphInfoGetGlyphName](<ctglyphinfogetglyphname(__).md>) — Retrieves the glyph name for a glyph info object, if that object exists.
- [CTGlyphInfoGetCharacterIdentifier](<ctglyphinfogetcharacteridentifier(__).md>) — Gets the character identifier for a glyph info object.
- [CTGlyphInfoGetCharacterCollection](<ctglyphinfogetcharactercollection(__).md>) — Gets the character collection for a glyph info object.
