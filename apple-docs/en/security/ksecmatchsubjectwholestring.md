---
title: kSecMatchSubjectWholeString
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchsubjectwholestring
source_url: 'https://developer.apple.com/documentation/security/ksecmatchsubjectwholestring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchsubjectwholestring.json'
content_hash: 'sha256:77eabc38ff2df426'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchSubjectWholeString

<sub>Global Variable</sub>

A key whose value is a string to exactly match a certificate or identity’s subject.

<sub>macOS</sub>

```swift
let kSecMatchSubjectWholeString: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md). If provided, returned certificates or identities are limited to those whose subject is exactly equal to this string.
