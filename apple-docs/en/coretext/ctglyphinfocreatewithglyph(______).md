---
title: 'CTGlyphInfoCreateWithGlyph(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctglyphinfocreatewithglyph(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctglyphinfocreatewithglyph(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctglyphinfocreatewithglyph%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:74e71713194d7023'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTGlyphInfoCreateWithGlyph(_:_:_:)

<sub>Function</sub>

Creates an immutable glyph info object with a glyph index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTGlyphInfoCreateWithGlyph(_ glyph: CGGlyph, _ font: CTFont, _ baseString: CFString) -> CTGlyphInfo?
```

## Parameters

- `glyph` — The index of the glyph.

- `font` — The font to be associated with the returned CTGlyphInfo object.

- `baseString` — The part of the string the returned object is intended to override.

## Return Value

A valid reference to an immutable CTGlyphInfo object, If glyph info creation was successful; otherwise, `NULL`.

## Discussion

This function creates an immutable glyph info object for a glyph index using a specified font.

## See Also

### Creating GlyphInfo Objects

- [CTGlyphInfoCreateWithGlyphName](<ctglyphinfocreatewithglyphname(______).md>) — Creates an immutable glyph info object with a glyph name.
- [CTGlyphInfoCreateWithCharacterIdentifier](<ctglyphinfocreatewithcharacteridentifier(______).md>) — Creates an immutable glyph info object with a character identifier.
