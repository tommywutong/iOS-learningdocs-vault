---
title: kSecValueData
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecvaluedata
source_url: 'https://developer.apple.com/documentation/security/ksecvaluedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecvaluedata.json'
content_hash: 'sha256:1c4e8ac23a14e7c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecValueData

<sub>Global Variable</sub>

A key whose value is the item’s data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecValueData: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md).  For keys and password items, the data is secret (encrypted) and may require the user to enter a password for access.
