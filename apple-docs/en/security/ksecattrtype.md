---
title: kSecAttrType
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrtype
source_url: 'https://developer.apple.com/documentation/security/ksecattrtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrtype.json'
content_hash: 'sha256:37a202f6c900c554'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrType

<sub>Global Variable</sub>

A key with a value that indicates the item’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrType: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and represents the item’s type. This number is the unsigned integer representation of a four-character code (for example, ‘aTyp’).
