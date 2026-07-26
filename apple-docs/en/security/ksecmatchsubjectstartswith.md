---
title: kSecMatchSubjectStartsWith
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchsubjectstartswith
source_url: 'https://developer.apple.com/documentation/security/ksecmatchsubjectstartswith'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchsubjectstartswith.json'
content_hash: 'sha256:1269fba03fa602b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchSubjectStartsWith

<sub>Global Variable</sub>

A key whose value is a string to match against the beginning of a certificate or identity’s subject.

<sub>macOS</sub>

```swift
let kSecMatchSubjectStartsWith: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md). If provided, returned certificates or identities are limited to those whose subject starts with this string.
