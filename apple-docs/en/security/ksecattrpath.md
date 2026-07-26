---
title: kSecAttrPath
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrpath
source_url: 'https://developer.apple.com/documentation/security/ksecattrpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrpath.json'
content_hash: 'sha256:ea593e5d76967b77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrPath

<sub>Global Variable</sub>

A key whose value is a string indicating the item’s path attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrPath: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and represents a path, typically the path component of the URL. Items of class [kSecClassInternetPassword](ksecclassinternetpassword.md) have this attribute.
