---
title: kSecAttrEffectiveKeySize
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattreffectivekeysize
source_url: 'https://developer.apple.com/documentation/security/ksecattreffectivekeysize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattreffectivekeysize.json'
content_hash: 'sha256:8f6104c704e94f57'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrEffectiveKeySize

<sub>Global Variable</sub>

A key whose value indicates the effective number of bits in a cryptographic key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrEffectiveKeySize: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and indicates the effective number of bits in this cryptographic key. For example, a DES key has a [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md) of 64, but a [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md) of 56 bits.
