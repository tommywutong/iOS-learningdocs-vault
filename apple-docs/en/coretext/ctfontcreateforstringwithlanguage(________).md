---
title: 'CTFontCreateForStringWithLanguage(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreateforstringwithlanguage(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreateforstringwithlanguage(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreateforstringwithlanguage%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:25b7bffe98d4b61d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateForStringWithLanguage(_:_:_:_:)

<sub>Function</sub>

Returns a font reference that most accurately maps the string range based on the current font and language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreateForStringWithLanguage(_ currentFont: CTFont, _ string: CFString, _ range: CFRange, _ language: CFString?) -> CTFont
```

## Parameters

- `currentFont` — The current font that contains a valid cascade list.

- `string` — A Unicode string containing characters that can’t be encoded by the current font.

- `range` — A [CFRange](../corefoundation/cfrange.md) specifying the range of the string to map.

- `language` — A language identifier to select a font for a particular localization.

## Return Value

The best substitute font that can encode the specified string range.

## Discussion

The current font itself can be returned if it covers the string provided. If the caller does not specify the language parameter, the function uses the current system language. The format of the language identifier should conform to [UTS #35](http://unicode.org/reports/tr35/).

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
- [CTFontCreateForString](<ctfontcreateforstring(______).md>) — Returns a font reference that most accurately maps the string range based on the current font.
