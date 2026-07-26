---
title: kSecMatchDiacriticInsensitive
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchdiacriticinsensitive
source_url: 'https://developer.apple.com/documentation/security/ksecmatchdiacriticinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchdiacriticinsensitive.json'
content_hash: 'sha256:0d33a714dafa9633'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchDiacriticInsensitive

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether diacritic-insensitive matching is performed.

<sub>macOS</sub>

```swift
let kSecMatchDiacriticInsensitive: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). If this value is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md), or if this attribute is not provided, then diacritic-sensitive string matching is performed.
