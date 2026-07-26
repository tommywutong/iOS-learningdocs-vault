---
title: 'CTFontCreateCopyWithSymbolicTraits(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcreatecopywithsymbolictraits(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcreatecopywithsymbolictraits(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcreatecopywithsymbolictraits%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f342aa6a95bdfaca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCreateCopyWithSymbolicTraits(_:_:_:_:_:)

<sub>Function</sub>

Returns a new font in the same font family as the original with the specified symbolic traits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCreateCopyWithSymbolicTraits(_ font: CTFont, _ size: CGFloat, _ matrix: UnsafePointer<CGAffineTransform>?, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFont?
```

## Parameters

- `font` — The original font reference on which to base the new font.

- `size` — The point size for the font reference. If `0.0` is specified, the original font’s size is preserved.

- `matrix` — The transformation matrix for the font.  In most cases, set this parameter to be `NULL`.  If `NULL` is specified, the original font’s matrix is preserved.

- `symTraitValue` — The value of the symbolic traits.

- `symTraitMask` — The mask bits of the symbolic traits.

## Return Value

A new font reference in the same family with the given symbolic traits. or `NULL` if none is found in the system.

## See Also

### Creating Fonts

- [CTFontCreateWithName](<ctfontcreatewithname(______).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithNameAndOptions](<ctfontcreatewithnameandoptions(________).md>) — Returns a new font reference for the given name.
- [CTFontCreateWithFontDescriptor](<ctfontcreatewithfontdescriptor(______).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateWithFontDescriptorAndOptions](<ctfontcreatewithfontdescriptorandoptions(________).md>) — Returns a new font reference that best matches the given font descriptor.
- [CTFontCreateUIFontForLanguage](<ctfontcreateuifontforlanguage(______).md>) — Returns the special user-interface font for the given language and user-interface type.
- [CTFontCreateCopyWithAttributes](<ctfontcreatecopywithattributes(________).md>) — Returns a new font with additional attributes based on the original font.
- [CTFontCreateCopyWithFamily](<ctfontcreatecopywithfamily(________).md>) — Returns a new font in the specified family based on the traits of the original font.
- [CTFontCreateForString](<ctfontcreateforstring(______).md>) — Returns a font reference that most accurately maps the string range based on the current font.
- [CTFontCreateForStringWithLanguage](<ctfontcreateforstringwithlanguage(________).md>) — Returns a font reference that most accurately maps the string range based on the current font and language.
