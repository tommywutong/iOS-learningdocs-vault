---
title: kSecAttrIsSensitive
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrissensitive
source_url: 'https://developer.apple.com/documentation/security/ksecattrissensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrissensitive.json'
content_hash: 'sha256:bb0bbf55080430a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrIsSensitive

<sub>Global Variable</sub>

A key whose value indicates the item’s sensitivity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrIsSensitive: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). When set to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), the item can only be exported in an encrypted format. Items of class [kSecClassKey](ksecclasskey.md) have this attribute.
