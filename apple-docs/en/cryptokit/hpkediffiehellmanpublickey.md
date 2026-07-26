---
title: HPKEDiffieHellmanPublicKey
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkediffiehellmanpublickey
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanpublickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkediffiehellmanpublickey.json'
content_hash: 'sha256:17fa2c772273ef30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEDiffieHellmanPublicKey

<sub>Protocol</sub>

A type that represents the public key in a Diffie-Hellman key exchange.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEDiffieHellmanPublicKey : HPKEPublicKeySerialization
```

## Relationships

- **Inherits From**: [HPKEPublicKeySerialization](hpkepublickeyserialization.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [PublicKey](curve25519/keyagreement/publickey.md), [PublicKey](p256/keyagreement/publickey.md), [PublicKey](p384/keyagreement/publickey.md), [PublicKey](p521/keyagreement/publickey.md)

## Topics

### Associated Types

- [EphemeralPrivateKey](hpkediffiehellmanpublickey/ephemeralprivatekey.md) — The type of the ephemeral private key.
