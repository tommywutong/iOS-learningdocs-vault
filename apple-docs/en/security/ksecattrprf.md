---
title: kSecAttrPRF
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrprf
source_url: 'https://developer.apple.com/documentation/security/ksecattrprf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrprf.json'
content_hash: 'sha256:c5ba485a68b3e186'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrPRF

<sub>Global Variable</sub>

A key whose value indicates the item’s pseudorandom function.

<sub>macOS</sub>

```swift
let kSecAttrPRF: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and indicates the pseudorandom function associated with this cryptographic key. See [Pseudorandom Function Values](item-attribute-keys-and-values.md#Pseudorandom-Function-Values) for a list of valid values.
