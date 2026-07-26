---
title: kSecCodeInfoCdHashes
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfocdhashes
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfocdhashes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfocdhashes.json'
content_hash: 'sha256:cb74a369169388a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoCdHashes

<sub>Global Variable</sub>

A key whose value is an array containing the unique binary identifier for every digest algorithm supported in the signature.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoCdHashes: CFString
```

## Discussion

The corresponding [CFArray](../corefoundation/cfarray.md) contains the values of the [kSecCodeInfoUnique](kseccodeinfounique.md) binary identifier for every digest algorithm supported in the signature in the same order as in the [kSecCodeInfoDigestAlgorithms](kseccodeinfodigestalgorithms.md) array. The [kSecCodeInfoUnique](kseccodeinfounique.md) value contained in this array corresponds to the [kSecCodeInfoDigestAlgorithm](kseccodeinfodigestalgorithm.md) value.
