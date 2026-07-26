---
title: 'CTFontDescriptorCreateMatchingFontDescriptor(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcreatematchingfontdescriptor(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatematchingfontdescriptor(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcreatematchingfontdescriptor%28_%3A_%3A%29.json'
content_hash: 'sha256:3bb16a55194964c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCreateMatchingFontDescriptor(_:_:)

<sub>Function</sub>

Returns the single preferred matching font descriptor based on the original descriptor and system precedence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCreateMatchingFontDescriptor(_ descriptor: CTFontDescriptor, _ mandatoryAttributes: CFSet?) -> CTFontDescriptor?
```

## Parameters

- `descriptor` — The original font descriptor.

- `mandatoryAttributes` — A set of attribute keys which must be identically matched in any returned font descriptors. May be `NULL`.

## Return Value

A retained, normalized font descriptor matching the attributes present in `descriptor`.

## Discussion

The original descriptor may be returned in normalized form. The caller is responsible for releasing the result. In the context of font descriptors, _normalized_ infers that the input values were matched up with actual existing fonts, and the descriptors for those existing fonts are the returned normalized descriptors.

## See Also

### Creating Font Descriptors

- [CTFontDescriptorCreateWithNameAndSize](<ctfontdescriptorcreatewithnameandsize(____).md>) — Creates a new font descriptor with the provided PostScript name and size.
- [CTFontDescriptorCreateWithAttributes](<ctfontdescriptorcreatewithattributes(__).md>) — Creates a new font descriptor reference from a dictionary of attributes.
- [CTFontDescriptorCreateCopyWithAttributes](<ctfontdescriptorcreatecopywithattributes(____).md>) — Creates a copy of the original font descriptor with new attributes.
- [CTFontDescriptorCreateCopyWithVariation](<ctfontdescriptorcreatecopywithvariation(______).md>) — Creates a copy of the original font descriptor with a new variation instance.
- [CTFontDescriptorCreateCopyWithFeature](<ctfontdescriptorcreatecopywithfeature(______).md>) — Copies a font descriptor with new feature settings.
- [CTFontDescriptorCreateCopyWithFamily](<ctfontdescriptorcreatecopywithfamily(____).md>) — Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [CTFontDescriptorCreateCopyWithSymbolicTraits](<ctfontdescriptorcreatecopywithsymbolictraits(______).md>) — Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [CTFontDescriptorCreateMatchingFontDescriptors](<ctfontdescriptorcreatematchingfontdescriptors(____).md>) — Returns an array of normalized font descriptors matching the provided descriptor.
