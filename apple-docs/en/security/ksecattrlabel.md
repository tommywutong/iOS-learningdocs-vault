---
title: kSecAttrLabel
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrlabel
source_url: 'https://developer.apple.com/documentation/security/ksecattrlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrlabel.json'
content_hash: 'sha256:3f1b6744b916b69c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrLabel

<sub>Global Variable</sub>

A key with a value that’s a string indicating the item’s label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrLabel: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and contains the user-visible label for this item.

On key creation, if not explicitly specified, this attribute defaults to `NULL`.
