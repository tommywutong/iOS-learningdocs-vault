---
title: 'CTFontDescriptorCopyAttributes(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptorcopyattributes(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorcopyattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorcopyattributes%28_%3A%29.json'
content_hash: 'sha256:f8c1292117f8b588'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorCopyAttributes(_:)

<sub>Function</sub>

Returns the attributes dictionary of the font descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorCopyAttributes(_ descriptor: CTFontDescriptor) -> CFDictionary
```

## Parameters

- `descriptor` — The font descriptor.

## Return Value

The font descriptor attributes dictionary. This dictionary contains the minimum number of attributes to specify fully this particular font descriptor.

## See Also

### Getting Attributes

- [CTFontDescriptorCopyAttribute](<ctfontdescriptorcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute.
- [CTFontDescriptorCopyLocalizedAttribute](<ctfontdescriptorcopylocalizedattribute(______).md>) — Returns a localized value for the requested attribute, if available.
