---
title: kSecAttrService
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrservice
source_url: 'https://developer.apple.com/documentation/security/ksecattrservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrservice.json'
content_hash: 'sha256:2ca59bf260f2d268'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrService

<sub>Global Variable</sub>

A key whose value is a string indicating the item’s service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrService: CFString
```

## Discussion

The corresponding value is a string of type [CFString](../corefoundation/cfstring.md) that represents the service associated with this item. Items of class [kSecClassGenericPassword](ksecclassgenericpassword.md) have this attribute.
