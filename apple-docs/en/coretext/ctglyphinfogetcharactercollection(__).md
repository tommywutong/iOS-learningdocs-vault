---
title: 'CTGlyphInfoGetCharacterCollection(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctglyphinfogetcharactercollection(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfogetcharactercollection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfogetcharactercollection%28_%3A%29.json'
content_hash: 'sha256:6587d50bf82b6e3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfoGetCharacterCollection(_:)

<sub>Function</sub>

Gets the character collection for a glyph info object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTGlyphInfoGetCharacterCollection(_ glyphInfo: CTGlyphInfo) -> CTCharacterCollection
```

## Parameters

- `glyphInfo` — The glyph info from which to get the character collection. May not be `NULL`.

## Return Value

The character collection of the given glyph info object.

## Discussion

If the glyph info object was created with a glyph name or a glyph index, its character collection is [kCTIdentityMappingCharacterCollection](ctcharactercollection/kctidentitymappingcharactercollection.md).

## See Also

### Getting GlyphInfo Data

- [CTGlyphInfoGetGlyphName](<ctglyphinfogetglyphname(__).md>) — Retrieves the glyph name for a glyph info object, if that object exists.
- [CTGlyphInfoGetCharacterIdentifier](<ctglyphinfogetcharacteridentifier(__).md>) — Gets the character identifier for a glyph info object.
- [CTGlyphInfoGetGlyph](<ctglyphinfogetglyph(__).md>) — Retrieves the glyph for a glyph info, if that object exists.
