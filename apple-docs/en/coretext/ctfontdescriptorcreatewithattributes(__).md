---
title: 'CTFontDescriptorCreateWithAttributes(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcreatewithattributes(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatewithattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcreatewithattributes%28_%3A%29.json'
content_hash: 'sha256:08b665f7058d6d58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCreateWithAttributes(_:)

<sub>Function</sub>

Creates a new font descriptor reference from a dictionary of attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCreateWithAttributes(_ attributes: CFDictionary) -> CTFontDescriptor
```

## Parameters

- `attributes` — A dictionary containing arbitrary attributes.

## Return Value

A new font descriptor with the attributes specified.

## Discussion

The provided attribute dictionary can contain arbitrary attributes that are preserved; however, unrecognized attributes are ignored on font creation and may not be preserved over the round trip from descriptor to font and back to descriptor.

## See Also

### Creating Font Descriptors

- [CTFontDescriptorCreateWithNameAndSize](<ctfontdescriptorcreatewithnameandsize(____).md>) — Creates a new font descriptor with the provided PostScript name and size.
- [CTFontDescriptorCreateCopyWithAttributes](<ctfontdescriptorcreatecopywithattributes(____).md>) — Creates a copy of the original font descriptor with new attributes.
- [CTFontDescriptorCreateCopyWithVariation](<ctfontdescriptorcreatecopywithvariation(______).md>) — Creates a copy of the original font descriptor with a new variation instance.
- [CTFontDescriptorCreateCopyWithFeature](<ctfontdescriptorcreatecopywithfeature(______).md>) — Copies a font descriptor with new feature settings.
- [CTFontDescriptorCreateCopyWithFamily](<ctfontdescriptorcreatecopywithfamily(____).md>) — Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [CTFontDescriptorCreateCopyWithSymbolicTraits](<ctfontdescriptorcreatecopywithsymbolictraits(______).md>) — Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [CTFontDescriptorCreateMatchingFontDescriptors](<ctfontdescriptorcreatematchingfontdescriptors(____).md>) — Returns an array of normalized font descriptors matching the provided descriptor.
- [CTFontDescriptorCreateMatchingFontDescriptor](<ctfontdescriptorcreatematchingfontdescriptor(____).md>) — Returns the single preferred matching font descriptor based on the original descriptor and system precedence.
