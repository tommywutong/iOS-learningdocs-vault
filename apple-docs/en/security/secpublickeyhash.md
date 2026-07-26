---
title: SecPublicKeyHash
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secpublickeyhash
source_url: 'https://developer.apple.com/documentation/security/secpublickeyhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpublickeyhash.json'
content_hash: 'sha256:e7c20da5ecc5e984'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPublicKeyHash

<sub>Type Alias</sub>

A container for a 20-byte public key hash.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SecPublicKeyHash = (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

## Discussion

The `SecPublicKeyHash` type represents a hash of a public key. You can use the constant `kSecPublicKeyHashItemAttr` as input to functions in the Keychain Services API to set or retrieve a certificate attribute value of this type. See [Keychain services](keychain-services.md) for information about getting and setting attribute values.
