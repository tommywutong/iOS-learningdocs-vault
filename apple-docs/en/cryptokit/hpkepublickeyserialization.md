---
title: HPKEPublicKeySerialization
framework: Apple CryptoKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpkepublickeyserialization
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkepublickeyserialization.json'
content_hash: 'sha256:9b6d015aa5b058ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HPKEPublicKeySerialization

<sub>Protocol</sub>

A type that [HPKE](hpke.md) uses to encode the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol HPKEPublicKeySerialization : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [HPKEDiffieHellmanPublicKey](hpkediffiehellmanpublickey.md), [HPKEKEMPublicKey](hpkekempublickey.md)

- **Conforming Types**: [PublicKey](curve25519/keyagreement/publickey.md), [PublicKey](p256/keyagreement/publickey.md), [PublicKey](p384/keyagreement/publickey.md), [PublicKey](p521/keyagreement/publickey.md), [PublicKey](xwingmlkem768x25519/publickey.md)

## Topics

### Initializers

- [init(_:kem:)](<hpkepublickeyserialization/init(__kem_).md>) — Creates a public key from an encoded representation.

### Instance Methods

- [hpkeRepresentation(kem:)](<hpkepublickeyserialization/hpkerepresentation(kem_).md>) — Creates an encoded representation of the public key.
