---
title: 'init(_:kem:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p256/keyagreement/publickey/init(_:kem:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/keyagreement/publickey/init(_:kem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/keyagreement/publickey/init%28_%3Akem%3A%29.json'
content_hash: 'sha256:a37f0d4069e48201'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [KeyAgreement](../../keyagreement.md) · [PublicKey](../publickey.md)

# init(_:kem:)

<sub>Initializer</sub>

Creates a NIST P-256 elliptic curve public key for use with Diffie-Hellman key exchange.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(_ serialization: D, kem: HPKE.KEM) throws where D : ContiguousBytes
```

## Discussion

- serialization: The serialized bytes of the public key.
- kem: The key encapsulation mechanism to use with the public key.

> [!danger] Throws
> [HPKE.Errors.inconsistentCiphersuiteAndKey](../../../hpke/errors/inconsistentciphersuiteandkey.md) if the key encapsulation mechanism requested is incompatible with this public key.
