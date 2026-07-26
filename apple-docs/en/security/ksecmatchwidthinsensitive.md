---
title: kSecMatchWidthInsensitive
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchwidthinsensitive
source_url: 'https://developer.apple.com/documentation/security/ksecmatchwidthinsensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchwidthinsensitive.json'
content_hash: 'sha256:59eaaf150e9611e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchWidthInsensitive

<sub>Global Variable</sub>

A key whose value is a Boolean indicating whether width-insensitive matching is performed.

<sub>macOS</sub>

```swift
let kSecMatchWidthInsensitive: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). If this value is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md), or if this attribute is not provided, then width-sensitive string matching is performed (for example, the ASCII character `a` does not match the UTF-8 full-width letter `a` (`U+FF41`).
