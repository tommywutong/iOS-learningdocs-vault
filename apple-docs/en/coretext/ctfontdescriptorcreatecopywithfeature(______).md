---
title: 'CTFontDescriptorCreateCopyWithFeature(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcreatecopywithfeature(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatecopywithfeature(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcreatecopywithfeature%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:82aa39e00fa67454'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCreateCopyWithFeature(_:_:_:)

<sub>Function</sub>

Copies a font descriptor with new feature settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCreateCopyWithFeature(_ original: CTFontDescriptor, _ featureTypeIdentifier: CFNumber, _ featureSelectorIdentifier: CFNumber) -> CTFontDescriptor
```

## Parameters

- `original` — The original font descriptor.

- `featureTypeIdentifier` — The feature type identifier.

- `featureSelectorIdentifier` — The feature selector identifier.

## Return Value

A copy of the original font descriptor modified with the given feature settings.

## Discussion

This is a convenience method to toggle more easily the state of individual features.

## See Also

### Creating Font Descriptors

- [CTFontDescriptorCreateWithNameAndSize](<ctfontdescriptorcreatewithnameandsize(____).md>) — Creates a new font descriptor with the provided PostScript name and size.
- [CTFontDescriptorCreateWithAttributes](<ctfontdescriptorcreatewithattributes(__).md>) — Creates a new font descriptor reference from a dictionary of attributes.
- [CTFontDescriptorCreateCopyWithAttributes](<ctfontdescriptorcreatecopywithattributes(____).md>) — Creates a copy of the original font descriptor with new attributes.
- [CTFontDescriptorCreateCopyWithVariation](<ctfontdescriptorcreatecopywithvariation(______).md>) — Creates a copy of the original font descriptor with a new variation instance.
- [CTFontDescriptorCreateCopyWithFamily](<ctfontdescriptorcreatecopywithfamily(____).md>) — Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [CTFontDescriptorCreateCopyWithSymbolicTraits](<ctfontdescriptorcreatecopywithsymbolictraits(______).md>) — Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [CTFontDescriptorCreateMatchingFontDescriptors](<ctfontdescriptorcreatematchingfontdescriptors(____).md>) — Returns an array of normalized font descriptors matching the provided descriptor.
- [CTFontDescriptorCreateMatchingFontDescriptor](<ctfontdescriptorcreatematchingfontdescriptor(____).md>) — Returns the single preferred matching font descriptor based on the original descriptor and system precedence.
