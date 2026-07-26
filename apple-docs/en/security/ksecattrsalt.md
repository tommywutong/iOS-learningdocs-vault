---
title: kSecAttrSalt
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrsalt
source_url: 'https://developer.apple.com/documentation/security/ksecattrsalt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrsalt.json'
content_hash: 'sha256:991fdbb50e9229d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrSalt

<sub>Global Variable</sub>

A key whose value indicates the salt to use for this item.

<sub>macOS</sub>

```swift
let kSecAttrSalt: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md) that indicates the salt to use with this cryptographic key.
