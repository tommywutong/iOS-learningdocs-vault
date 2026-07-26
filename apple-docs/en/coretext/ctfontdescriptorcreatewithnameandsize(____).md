---
title: 'CTFontDescriptorCreateWithNameAndSize(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcreatewithnameandsize(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatewithnameandsize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcreatewithnameandsize%28_%3A_%3A%29.json'
content_hash: 'sha256:46d9a38b51ef5146'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCreateWithNameAndSize(_:_:)

<sub>Function</sub>

Creates a new font descriptor with the provided PostScript name and size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCreateWithNameAndSize(_ name: CFString, _ size: CGFloat) -> CTFontDescriptor
```

## Parameters

- `name` — The PostScript name to be used for the font descriptor as a [CFString](../corefoundation/cfstring.md) object.

- `size` — The point size. If `0.0`, the font size attribute ([kCTFontSizeAttribute](kctfontsizeattribute.md)) is omitted from the returned font descriptor.

## Return Value

A new font descriptor reference with the given PostScript name and point size.

## See Also

### Creating Font Descriptors

- [CTFontDescriptorCreateWithAttributes](<ctfontdescriptorcreatewithattributes(__).md>) — Creates a new font descriptor reference from a dictionary of attributes.
- [CTFontDescriptorCreateCopyWithAttributes](<ctfontdescriptorcreatecopywithattributes(____).md>) — Creates a copy of the original font descriptor with new attributes.
- [CTFontDescriptorCreateCopyWithVariation](<ctfontdescriptorcreatecopywithvariation(______).md>) — Creates a copy of the original font descriptor with a new variation instance.
- [CTFontDescriptorCreateCopyWithFeature](<ctfontdescriptorcreatecopywithfeature(______).md>) — Copies a font descriptor with new feature settings.
- [CTFontDescriptorCreateCopyWithFamily](<ctfontdescriptorcreatecopywithfamily(____).md>) — Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [CTFontDescriptorCreateCopyWithSymbolicTraits](<ctfontdescriptorcreatecopywithsymbolictraits(______).md>) — Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [CTFontDescriptorCreateMatchingFontDescriptors](<ctfontdescriptorcreatematchingfontdescriptors(____).md>) — Returns an array of normalized font descriptors matching the provided descriptor.
- [CTFontDescriptorCreateMatchingFontDescriptor](<ctfontdescriptorcreatematchingfontdescriptor(____).md>) — Returns the single preferred matching font descriptor based on the original descriptor and system precedence.
