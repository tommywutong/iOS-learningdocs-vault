---
title: kSecAttrCreationDate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrcreationdate
source_url: 'https://developer.apple.com/documentation/security/ksecattrcreationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrcreationdate.json'
content_hash: 'sha256:e1965d5547b5759d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrCreationDate

<sub>Global Variable</sub>

A key with a value that indicates the item’s creation date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrCreationDate: CFString
```

## Discussion

The corresponding value is of type [CFDate](../corefoundation/cfdate.md) and represents the date the item was created. Read only.
