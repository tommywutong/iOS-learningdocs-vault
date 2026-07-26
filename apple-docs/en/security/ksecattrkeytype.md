---
title: kSecAttrKeyType
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrkeytype
source_url: 'https://developer.apple.com/documentation/security/ksecattrkeytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrkeytype.json'
content_hash: 'sha256:4c7a4e011d6689d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrKeyType

<sub>Global Variable</sub>

A key whose value indicates the item’s algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrKeyType: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and indicates the algorithm associated with this cryptographic key. See [Key Type Values](item-attribute-keys-and-values.md#Key-Type-Values) for a list of valid values.
