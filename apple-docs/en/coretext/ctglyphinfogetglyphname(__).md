---
title: 'CTGlyphInfoGetGlyphName(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctglyphinfogetglyphname(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfogetglyphname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfogetglyphname%28_%3A%29.json'
content_hash: 'sha256:d4dfc743c3b57901'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfoGetGlyphName(_:)

<sub>Function</sub>

Retrieves the glyph name for a glyph info object, if that object exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTGlyphInfoGetGlyphName(_ glyphInfo: CTGlyphInfo) -> CFString?
```

## Parameters

- `glyphInfo` — The glyph info object from which to get the glyph name. This parameter must not be `NULL`.

## Return Value

A glyph name, if the glyph info object was created with a name; otherwise, `NULL`.

## See Also

### Getting GlyphInfo Data

- [CTGlyphInfoGetCharacterIdentifier](<ctglyphinfogetcharacteridentifier(__).md>) — Gets the character identifier for a glyph info object.
- [CTGlyphInfoGetCharacterCollection](<ctglyphinfogetcharactercollection(__).md>) — Gets the character collection for a glyph info object.
- [CTGlyphInfoGetGlyph](<ctglyphinfogetglyph(__).md>) — Retrieves the glyph for a glyph info, if that object exists.
