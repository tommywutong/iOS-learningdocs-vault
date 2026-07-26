---
title: kSecPropertyKeyValue
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecpropertykeyvalue
source_url: 'https://developer.apple.com/documentation/security/ksecpropertykeyvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecpropertykeyvalue.json'
content_hash: 'sha256:726fac2fffec08dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecPropertyKeyValue

<sub>Global Variable</sub>

A key whose value is the value for a certificate property.

<sub>macOS</sub>

```swift
let kSecPropertyKeyValue: CFString
```

## Discussion

The value is a Core Foundation type, usually a [CFString](../corefoundation/cfstring.md), [CFArray](../corefoundation/cfarray.md), or [CFDictionary](../corefoundation/cfdictionary.md) object.
