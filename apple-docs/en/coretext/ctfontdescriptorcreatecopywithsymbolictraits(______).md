---
title: 'CTFontDescriptorCreateCopyWithSymbolicTraits(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcreatecopywithsymbolictraits(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatecopywithsymbolictraits(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcreatecopywithsymbolictraits%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1ba30c56307c8ae8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCreateCopyWithSymbolicTraits(_:_:_:)

<sub>Function</sub>

Creates a copy of the font descriptor with the specified symbolic traits as the original.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCreateCopyWithSymbolicTraits(_ original: CTFontDescriptor, _ symTraitValue: CTFontSymbolicTraits, _ symTraitMask: CTFontSymbolicTraits) -> CTFontDescriptor?
```

## Parameters

- `original` — The original font descriptor.

- `symTraitValue` — The value of the symbolic traits.

- `symTraitMask` — The mask bits of the symbolic traits. This parameter represents a bitfield that indicates which traits should be changed and which should be taken from the original font descriptor.

## Return Value

Returns a new font descriptor reference in the same family with the given symbolic traits, or `NULL` if no matching font descriptor is found in the system.

## Discussion

This bitfield of `symTraitValue` parameter indicates the desired value for the traits specified by the `symTraitMask` parameter. Used in conjunction, they can allow for trait removal as well as addition.

## See Also

### Creating Font Descriptors

- [CTFontDescriptorCreateWithNameAndSize](<ctfontdescriptorcreatewithnameandsize(____).md>) — Creates a new font descriptor with the provided PostScript name and size.
- [CTFontDescriptorCreateWithAttributes](<ctfontdescriptorcreatewithattributes(__).md>) — Creates a new font descriptor reference from a dictionary of attributes.
- [CTFontDescriptorCreateCopyWithAttributes](<ctfontdescriptorcreatecopywithattributes(____).md>) — Creates a copy of the original font descriptor with new attributes.
- [CTFontDescriptorCreateCopyWithVariation](<ctfontdescriptorcreatecopywithvariation(______).md>) — Creates a copy of the original font descriptor with a new variation instance.
- [CTFontDescriptorCreateCopyWithFeature](<ctfontdescriptorcreatecopywithfeature(______).md>) — Copies a font descriptor with new feature settings.
- [CTFontDescriptorCreateCopyWithFamily](<ctfontdescriptorcreatecopywithfamily(____).md>) — Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [CTFontDescriptorCreateMatchingFontDescriptors](<ctfontdescriptorcreatematchingfontdescriptors(____).md>) — Returns an array of normalized font descriptors matching the provided descriptor.
- [CTFontDescriptorCreateMatchingFontDescriptor](<ctfontdescriptorcreatematchingfontdescriptor(____).md>) — Returns the single preferred matching font descriptor based on the original descriptor and system precedence.
