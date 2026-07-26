---
title: kSecUseKeychain
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecusekeychain
source_url: 'https://developer.apple.com/documentation/security/ksecusekeychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecusekeychain.json'
content_hash: 'sha256:586327b3ce6f111b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseKeychain

<sub>Global Variable</sub>

A key whose value is a keychain to operate on.

<sub>macOS</sub>

```swift
let kSecUseKeychain: CFString
```

## Discussion

Specifies a [SecKeychain](seckeychain.md) object that references the keychain to which [SecItemAdd](<secitemadd(____).md>) should add the provided items.
