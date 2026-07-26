---
title: 'CTFontCreateForString(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreateforstring(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreateforstring(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreateforstring%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fa9b06bbd291c849'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateForString(_:_:_:)

<sub>Function</sub>

Returns a font reference that most accurately maps the string range based on the current font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreateForString(_ currentFont: CTFont, _ string: CFString, _ range: CFRange) -> CTFont
```

## Parameters

- `currentFont` — The current font that contains a valid cascade list.

- `string` — A Unicode string containing characters that can’t be encoded by the current font.

- `range` — A [CFRange](../corefoundation/cfrange.md) structure specifying the range of the string to map.

## Return Value

The best substitute font from the cascade list of the current font that can encode the specified string range.

## Discussion

If the current font can encode the string range, the function retains and returns the font.

## See Also

### Related Documentation

- [CTFontCopyCharacterSet](<ctfontcopycharacterset(__).md>) — Returns the Unicode character set of the font.
- [CTFontGetGlyphsForCharacters](<ctfontgetglyphsforcharacters(________).md>) — Performs basic character-to-glyph mapping.
- [kCTFontCascadeListAttribute](kctfontcascadelistattribute.md) — The cascade list used for a font reference.

### Creating Fonts

- [CTFontCreateWithName](<ctfontcreatewithname(______).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithNameAndOptions](<ctfontcreatewithnameandoptions(________).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithFontDescriptor](<ctfontcreatewithfontdescriptor(______).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateWithFontDescriptorAndOptions](<ctfontcreatewithfontdescriptorandoptions(________).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateUIFontForLanguage](<ctfontcreateuifontforlanguage(______).md>) — Returns the special user-interface font for the given language and user-interface type.
- [CTFontCreateCopyWithAttributes](<ctfontcreatecopywithattributes(________).md>) — Returns a new font with additional attributes based on the original font.
- [CTFontCreateCopyWithSymbolicTraits](<ctfontcreatecopywithsymbolictraits(__________).md>) — Returns a new font in the same font family as the original with the specified symbolic traits.
- [CTFontCreateCopyWithFamily](<ctfontcreatecopywithfamily(________).md>) — Returns a new font in the specified family based on the traits of the original font.
- [CTFontCreateForStringWithLanguage](<ctfontcreateforstringwithlanguage(________).md>) — Returns a font reference that most accurately maps the string range based on the current font and language.
