---
title: 'CTGlyphInfoGetCharacterIdentifier(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctglyphinfogetcharacteridentifier(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfogetcharacteridentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfogetcharacteridentifier%28_%3A%29.json'
content_hash: 'sha256:6ba8b99aa4b67426'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfoGetCharacterIdentifier(_:)

<sub>Function</sub>

Gets the character identifier for a glyph info object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTGlyphInfoGetCharacterIdentifier(_ glyphInfo: CTGlyphInfo) -> CGFontIndex
```

## Parameters

- `glyphInfo` — The glyph info from which to get the character identifier. May not be `NULL`.

## Return Value

The character identifier of the given glyph info object.

## See Also

### Getting GlyphInfo Data

- [CTGlyphInfoGetGlyphName](<ctglyphinfogetglyphname(__).md>) — Retrieves the glyph name for a glyph info object, if that object exists.
- [CTGlyphInfoGetCharacterCollection](<ctglyphinfogetcharactercollection(__).md>) — Gets the character collection for a glyph info object.
- [CTGlyphInfoGetGlyph](<ctglyphinfogetglyph(__).md>) — Retrieves the glyph for a glyph info, if that object exists.
