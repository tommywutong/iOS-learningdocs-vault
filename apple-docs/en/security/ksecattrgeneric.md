---
title: kSecAttrGeneric
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrgeneric
source_url: 'https://developer.apple.com/documentation/security/ksecattrgeneric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrgeneric.json'
content_hash: 'sha256:9b07ec7b914ccc55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrGeneric

<sub>Global Variable</sub>

A key whose value indicates the item’s user-defined attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrGeneric: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md) and contains a user-defined attribute. Items of class [kSecClassGenericPassword](ksecclassgenericpassword.md) have this attribute.
