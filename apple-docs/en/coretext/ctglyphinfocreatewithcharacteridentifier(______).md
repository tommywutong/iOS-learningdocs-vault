---
title: 'CTGlyphInfoCreateWithCharacterIdentifier(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctglyphinfocreatewithcharacteridentifier(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfocreatewithcharacteridentifier(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfocreatewithcharacteridentifier%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6ebb0db6899b1225'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfoCreateWithCharacterIdentifier(_:_:_:)

<sub>Function</sub>

Creates an immutable glyph info object with a character identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTGlyphInfoCreateWithCharacterIdentifier(_ cid: CGFontIndex, _ collection: CTCharacterCollection, _ baseString: CFString) -> CTGlyphInfo?
```

## Parameters

- `cid` — A character identifier.

- `collection` — A character collection identifier.

- `baseString` — The part of the string the returned object is intended to override.

## Return Value

A valid reference to an immutable CTGlyphInfo object if glyph info creation was successful; otherwise, `NULL`.

## Discussion

This function creates an immutable glyph info object for a character identifier and a character collection.

## See Also

### Creating GlyphInfo Objects

- [CTGlyphInfoCreateWithGlyphName](<ctglyphinfocreatewithglyphname(______).md>) — Creates an immutable glyph info object with a glyph name.
- [CTGlyphInfoCreateWithGlyph](<ctglyphinfocreatewithglyph(______).md>) — Creates an immutable glyph info object with a glyph index.
