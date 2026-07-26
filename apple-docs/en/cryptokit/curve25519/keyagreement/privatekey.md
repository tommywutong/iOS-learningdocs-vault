---
title: Curve25519.KeyAgreement.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/curve25519/keyagreement/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/keyagreement/privatekey.json'
content_hash: 'sha256:d87142432197fca4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [Curve25519](../../curve25519.md) · [KeyAgreement](../keyagreement.md)

# Curve25519.KeyAgreement.PrivateKey

<sub>Structure</sub>

A Curve25519 private key used for key agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [DiffieHellmanKeyAgreement](../../diffiehellmankeyagreement.md), [Escapable](../../../swift/escapable.md), [HPKEDiffieHellmanPrivateKey](../../hpkediffiehellmanprivatekey.md), [HPKEDiffieHellmanPrivateKeyGeneration](../../hpkediffiehellmanprivatekeygeneration.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [init()](<privatekey/init().md>) — Creates a random Curve25519 private key for key agreement.
- [init(rawRepresentation:)](<privatekey/init(rawrepresentation_).md>) — Creates a Curve25519 private key for key agreement from a collection of bytes.

### Reporting the private key

- [rawRepresentation](privatekey/rawrepresentation.md) — The raw representation of the key as a collection of contiguous bytes.

### Finding the public key

- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Creating a shared secret

- [sharedSecretFromKeyAgreement(with:)](<privatekey/sharedsecretfromkeyagreement(with_).md>) — Computes a shared secret with the provided public key from another party.
- [SharedSecret](../../sharedsecret.md) — A key agreement result from which you can derive a symmetric cryptographic key.

## See Also

### Using keys

- [PublicKey](publickey.md) — A Curve25519 public key used for key agreement.
