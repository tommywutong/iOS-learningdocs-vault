---
title: kSecAttrRounds
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrrounds
source_url: 'https://developer.apple.com/documentation/security/ksecattrrounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrrounds.json'
content_hash: 'sha256:361e3fd9960b0b15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrRounds

<sub>Global Variable</sub>

A key whose value indicates the number of rounds to run the pseudorandom function.

<sub>macOS</sub>

```swift
let kSecAttrRounds: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and indicates the number of rounds to run the pseudorandom function specified by [kSecAttrPRF](ksecattrprf.md) for a cryptographic key.
