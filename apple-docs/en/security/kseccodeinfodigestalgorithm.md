---
title: kSecCodeInfoDigestAlgorithm
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfodigestalgorithm
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfodigestalgorithm.json'
content_hash: 'sha256:ee44834aa0a1d6bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoDigestAlgorithm

<sub>Global Variable</sub>

A key whose value is a number indicating the cryptographic hash function.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoDigestAlgorithm: CFString
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md) indicating the kind of cryptographic hash function used within the signature to seal its pieces together. See [SecCSDigestAlgorithm](seccsdigestalgorithm.md) for possible value.
