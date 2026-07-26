---
title: kSecAttrPublicKeyHash
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrpublickeyhash
source_url: 'https://developer.apple.com/documentation/security/ksecattrpublickeyhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrpublickeyhash.json'
content_hash: 'sha256:eb7ee75081c42bbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrPublicKeyHash

<sub>Global Variable</sub>

A key whose value indicates the item’s public key hash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrPublicKeyHash: CFString
```

## Discussion

The corresponding value is of type [CFData](../corefoundation/cfdata.md) and contains the hash of a certificate’s public key. Items of class [kSecClassCertificate](ksecclasscertificate.md) have this attribute. Read only.
