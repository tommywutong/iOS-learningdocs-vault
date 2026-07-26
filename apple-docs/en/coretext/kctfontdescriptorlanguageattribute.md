---
title: kCTFontDescriptorLanguageAttribute
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontdescriptorlanguageattribute
source_url: 'https://developer.apple.com/documentation/coretext/kctfontdescriptorlanguageattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontdescriptorlanguageattribute.json'
content_hash: 'sha256:bd4eb0c563f2ecde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontDescriptorLanguageAttribute

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontDescriptorLanguageAttribute: CFString
```

## Discussion

The language identifier for font fallback selection.

The value associated with this key is a CFStringRef. If specified in a font descriptor, it is used to select the appropriate font fallback list for the language. This key should not be confused with kCTLanguageAttributeName, which is defined in CTStringAttributes.h.
