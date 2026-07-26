---
title: kSecCodeInfoDigestAlgorithms
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfodigestalgorithms
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfodigestalgorithms.json'
content_hash: 'sha256:241c871ad5bcbc86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoDigestAlgorithms

<sub>Global Variable</sub>

A key whose value is a list of the kinds of cryptographic hash functions available within the signature.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoDigestAlgorithms: CFString
```

## Discussion

The value is a [CFArray](../corefoundation/cfarray.md) of [CFNumber](../corefoundation/cfnumber.md) objects indicating the kinds of cryptographic hash functions available within the signature. The ordering of the items in the array has no significance in terms of priority, but determines the order in which the hashes appear in [kSecCodeInfoCdHashes](kseccodeinfocdhashes.md).
