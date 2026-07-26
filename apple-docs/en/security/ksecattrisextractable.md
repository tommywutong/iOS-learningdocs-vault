---
title: kSecAttrIsExtractable
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrisextractable
source_url: 'https://developer.apple.com/documentation/security/ksecattrisextractable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrisextractable.json'
content_hash: 'sha256:f28d3371b73017c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrIsExtractable

<sub>Global Variable</sub>

A key whose value indicates the item’s extractability.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrIsExtractable: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md) and indicates whether the item can be exported from its keychain. Items of class [kSecClassKey](ksecclasskey.md) have this attribute.
