---
title: kSecMatchSubjectEndsWith
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchsubjectendswith
source_url: 'https://developer.apple.com/documentation/security/ksecmatchsubjectendswith'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchsubjectendswith.json'
content_hash: 'sha256:66d6204807da3ac1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchSubjectEndsWith

<sub>Global Variable</sub>

A key whose value is a string to match against the end of a certificate or identity’s subject.

<sub>macOS</sub>

```swift
let kSecMatchSubjectEndsWith: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md). If provided, returned certificates or identities are limited to those whose subject ends with this string.
