---
title: kSecAttrApplicationTag
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrapplicationtag
source_url: 'https://developer.apple.com/documentation/security/ksecattrapplicationtag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrapplicationtag.json'
content_hash: 'sha256:d9a4f3eb86b4bd59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrApplicationTag

<sub>Global Variable</sub>

A key whose value indicates the item’s private tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrApplicationTag: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md) and contains private tag data.

On key creation, if not explicitly specified, this attribute defaults to `NULL`.
