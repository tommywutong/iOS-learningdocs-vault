---
title: kSecAttrKeySizeInBits
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrkeysizeinbits
source_url: 'https://developer.apple.com/documentation/security/ksecattrkeysizeinbits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrkeysizeinbits.json'
content_hash: 'sha256:497c1d7ddf59061d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrKeySizeInBits

<sub>Global Variable</sub>

A key whose value indicates the number of bits in a cryptographic key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrKeySizeInBits: CFString
```

## Discussion

The corresponding value is of type [CFNumber](../corefoundation/cfnumber.md) and indicates the total number of bits in this cryptographic key.
