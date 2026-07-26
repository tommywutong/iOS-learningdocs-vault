---
title: P256.KeyAgreement.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p256/keyagreement/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/keyagreement/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/keyagreement/privatekey.json'
content_hash: 'sha256:f8479a6aa76e2123'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [P256](../../p256.md) · [KeyAgreement](../keyagreement.md)

# P256.KeyAgreement.PrivateKey

<sub>Structure</sub>

A P-256 private key used for key agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [DiffieHellmanKeyAgreement](../../diffiehellmankeyagreement.md), [Escapable](../../../swift/escapable.md), [HPKEDiffieHellmanPrivateKey](../../hpkediffiehellmanprivatekey.md), [HPKEDiffieHellmanPrivateKeyGeneration](../../hpkediffiehellmanprivatekeygeneration.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [init(rawRepresentation:)](<privatekey/init(rawrepresentation_).md>) — Creates a P-256 private key for key agreement from a collection of bytes.
- [init(compactRepresentable:)](<privatekey/init(compactrepresentable_).md>) — Creates a random P-256 private key for key agreement.
- [init(derRepresentation:)](<privatekey/init(derrepresentation_).md>) — Creates a P-256 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<privatekey/init(pemrepresentation_).md>) — Creates a P-256 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.
- [init(x963Representation:)](<privatekey/init(x963representation_).md>) — Creates a P-256 private key for key agreement from an ANSI x9.63 representation.

### Representing the key

- [rawRepresentation](privatekey/rawrepresentation.md) — A data representation of the private key.
- [derRepresentation](privatekey/derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [pemRepresentation](privatekey/pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the private key.
- [x963Representation](privatekey/x963representation.md) — An ANSI x9.63 representation of the private key.

### Finding the public key

- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Creating a shared secret

- [sharedSecretFromKeyAgreement(with:)](<privatekey/sharedsecretfromkeyagreement(with_).md>) — Computes a shared secret with the provided public key from another party.
- [SharedSecret](../../sharedsecret.md) — A key agreement result from which you can derive a symmetric cryptographic key.

### Default Implementations

- [DiffieHellmanKeyAgreement Implementations](privatekey/diffiehellmankeyagreement-implementations.md)
- [HPKEDiffieHellmanPrivateKeyGeneration Implementations](privatekey/hpkediffiehellmanprivatekeygeneration-implementations.md)

## See Also

### Using keys

- [PublicKey](publickey.md) — A P-256 public key used for key agreement.
