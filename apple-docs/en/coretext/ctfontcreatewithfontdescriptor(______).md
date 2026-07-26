---
title: 'CTFontCreateWithFontDescriptor(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreatewithfontdescriptor(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatewithfontdescriptor(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatewithfontdescriptor%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:52a41b74fdaf9c1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateWithFontDescriptor(_:_:_:)

<sub>Function</sub>

Returns a new font reference that best matches the given font descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreateWithFontDescriptor(_ descriptor: CTFontDescriptor, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?) -> CTFont
```

## Parameters

- `descriptor` — A font descriptor containing attributes that specify the requested font.

- `size` — The point size for the font reference. If `0.0` is specified, the default font size of `12.0` is used.  This parameter is optional.

- `matrix` — The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL` is specified, the identity matrix is used.  This parameter is optional.

## Return Value

A CTFontRef that best matches the attributes provided with the font descriptor.

## Discussion

The `size` and `matrix` parameters override any specified in the font descriptor unless they are unspecified (`0.0` for `size` and `NULL` for `matrix`). A best match font is always returned, and default values are used for any unspecified parameters.

## See Also

### Creating Fonts

- [CTFontCreateWithName](<ctfontcreatewithname(______).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithNameAndOptions](<ctfontcreatewithnameandoptions(________).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithFontDescriptorAndOptions](<ctfontcreatewithfontdescriptorandoptions(________).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateUIFontForLanguage](<ctfontcreateuifontforlanguage(______).md>) — Returns the special user-interface font for the given language and user-interface type.
- [CTFontCreateCopyWithAttributes](<ctfontcreatecopywithattributes(________).md>) — Returns a new font with additional attributes based on the original font.
- [CTFontCreateCopyWithSymbolicTraits](<ctfontcreatecopywithsymbolictraits(__________).md>) — Returns a new font in the same font family as the original with the specified symbolic traits.
- [CTFontCreateCopyWithFamily](<ctfontcreatecopywithfamily(________).md>) — Returns a new font in the specified family based on the traits of the original font.
- [CTFontCreateForString](<ctfontcreateforstring(______).md>) — Returns a font reference that most accurately maps the string range based on the current font.
- [CTFontCreateForStringWithLanguage](<ctfontcreateforstringwithlanguage(________).md>) — Returns a font reference that most accurately maps the string range based on the current font and language.
