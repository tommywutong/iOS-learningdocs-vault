---
title: kSecAttrPort
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrport
source_url: 'https://developer.apple.com/documentation/security/ksecattrport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrport.json'
content_hash: 'sha256:4e81afc679bc6ff8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrPort

<sub>Global Variable</sub>

A key whose value indicates the item’s port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrPort: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and represents an Internet port number. Items of class [kSecClassInternetPassword](ksecclassinternetpassword.md) have this attribute.
