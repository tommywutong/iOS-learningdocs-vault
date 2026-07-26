---
title: 'CTFontCreateCopyWithAttributes(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreatecopywithattributes(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatecopywithattributes(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatecopywithattributes%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:faac9ecedd3d8760'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateCopyWithAttributes(_:_:_:_:)

<sub>Function</sub>

Returns a new font with additional attributes based on the original font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreateCopyWithAttributes(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ attributes: CTFontDescriptor?) -> CTFont
```

## Parameters

- `font` — The original font reference on which to base the new font.

- `size` — The point size for the font reference. If `0.0` is specified, the original font’s size is preserved.

- `matrix` — The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL` is specified, the original font’s matrix is preserved.

- `attributes` — A font descriptor containing additional attributes that the new font should contain.

## Return Value

A new font reference converted from the original with the specified attributes.

## Discussion

This function provides a mechanism to change attributes quickly on a given font reference in response to user actions. For instance, the size can be changed in response to a user manipulating a size slider.

## See Also

### Creating Fonts

- [CTFontCreateWithName](<ctfontcreatewithname(______).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithNameAndOptions](<ctfontcreatewithnameandoptions(________).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithFontDescriptor](<ctfontcreatewithfontdescriptor(______).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateWithFontDescriptorAndOptions](<ctfontcreatewithfontdescriptorandoptions(________).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateUIFontForLanguage](<ctfontcreateuifontforlanguage(______).md>) — Returns the special user-interface font for the given language and user-interface type.
- [CTFontCreateCopyWithSymbolicTraits](<ctfontcreatecopywithsymbolictraits(__________).md>) — Returns a new font in the same font family as the original with the specified symbolic traits.
- [CTFontCreateCopyWithFamily](<ctfontcreatecopywithfamily(________).md>) — Returns a new font in the specified family based on the traits of the original font.
- [CTFontCreateForString](<ctfontcreateforstring(______).md>) — Returns a font reference that most accurately maps the string range based on the current font.
- [CTFontCreateForStringWithLanguage](<ctfontcreateforstringwithlanguage(________).md>) — Returns a font reference that most accurately maps the string range based on the current font and language.
