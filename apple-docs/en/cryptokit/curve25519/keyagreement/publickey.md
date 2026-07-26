---
title: Curve25519.KeyAgreement.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/curve25519/keyagreement/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/keyagreement/publickey.json'
content_hash: 'sha256:0e6a896e6fa75ac9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [Curve25519](../../curve25519.md) · [KeyAgreement](../keyagreement.md)

# Curve25519.KeyAgreement.PublicKey

<sub>Structure</sub>

A Curve25519 public key used for key agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Escapable](../../../swift/escapable.md), [HPKEDiffieHellmanPublicKey](../../hpkediffiehellmanpublickey.md), [HPKEPublicKeySerialization](../../hpkepublickeyserialization.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a public key

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>) — Creates a Curve25519 public key for key agreement from a collection of bytes.

### Representing the key

- [rawRepresentation](publickey/rawrepresentation.md) — A representation of the Curve25519 public key as a collection of bytes.

### Type Aliases

- [HPKEEphemeralPrivateKey](publickey/hpkeephemeralprivatekey.md) — The type of the ephemeral private key associated with this public key.

### Default Implementations

- [HPKEDiffieHellmanPublicKey Implementations](publickey/hpkediffiehellmanpublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](publickey/hpkepublickeyserialization-implementations.md)

## See Also

### Using keys

- [PrivateKey](privatekey.md) — A Curve25519 private key used for key agreement.
