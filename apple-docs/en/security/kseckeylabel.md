---
title: kSecKeyLabel
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/kseckeylabel
source_url: 'https://developer.apple.com/documentation/security/kseckeylabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseckeylabel.json'
content_hash: 'sha256:e73ef626daedefc0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecKeyLabel

<sub>Global Variable</sub>

<sub>macOS</sub>

```swift
var kSecKeyLabel: Int32 { get }
```

## Discussion

Type blob; for private and public keys this contains the hash of the public key.  This is used to associate certificates and keys.  Its value matches the value of the `kSecPublicKeyHashItemAttr` attribute of a certificate and it’s used to construct an identity from a certificate and a key. For symmetric keys this is whatever the creator of the key passed in when they generated the key.
