---
title: kSecAttrCreator
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrcreator
source_url: 'https://developer.apple.com/documentation/security/ksecattrcreator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrcreator.json'
content_hash: 'sha256:6320b495baaeea24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrCreator

<sub>Global Variable</sub>

A key with a value that indicates the item’s creator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrCreator: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and represents the item’s creator. This number is the unsigned integer representation of a four-character code (for example, `'aCrt'`).
