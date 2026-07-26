---
title: kSecAttrServer
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrserver
source_url: 'https://developer.apple.com/documentation/security/ksecattrserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrserver.json'
content_hash: 'sha256:7b79ff3f85f14fbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrServer

<sub>Global Variable</sub>

A key whose value is a string indicating the item’s server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrServer: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and contains the server’s domain name or IP address. Items of class [kSecClassInternetPassword](ksecclassinternetpassword.md) have this attribute.
