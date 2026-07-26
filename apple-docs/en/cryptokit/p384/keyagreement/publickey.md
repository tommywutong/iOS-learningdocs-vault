---
title: P384.KeyAgreement.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p384/keyagreement/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/keyagreement/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/keyagreement/publickey.json'
content_hash: 'sha256:293773eb84d54370'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [P384](../../p384.md) · [KeyAgreement](../keyagreement.md)

# P384.KeyAgreement.PublicKey

<sub>Structure</sub>

A P-384 public key used for key agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Escapable](../../../swift/escapable.md), [HPKEDiffieHellmanPublicKey](../../hpkediffiehellmanpublickey.md), [HPKEPublicKeySerialization](../../hpkepublickeyserialization.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a public key

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>) — Creates a P-384 public key for key agreement from a collection of bytes.
- [init(compactRepresentation:)](<publickey/init(compactrepresentation_).md>) — Creates a P-384 public key for key agreement from a compact representation of the key.
- [init(derRepresentation:)](<publickey/init(derrepresentation_).md>) — Creates a P-384 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<publickey/init(pemrepresentation_).md>) — Creates a P-384 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init(x963Representation:)](<publickey/init(x963representation_).md>) — Creates a P-384 public key for key agreement from an ANSI x9.63 representation.
- [init(compressedRepresentation:)](<publickey/init(compressedrepresentation_).md>) — Creates a P-384 public key for key agreement from a compressed representation of the key.

### Representing the key

- [rawRepresentation](publickey/rawrepresentation.md) — A full representation of the public key.
- [compactRepresentation](publickey/compactrepresentation.md) — A compact representation of the public key.
- [derRepresentation](publickey/derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [pemRepresentation](publickey/pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the public key.
- [x963Representation](publickey/x963representation.md) — An ANSI x9.63 representation of the public key.
- [compressedRepresentation](publickey/compressedrepresentation.md) — A compressed representation of the public key.

### Default Implementations

- [HPKEDiffieHellmanPublicKey Implementations](publickey/hpkediffiehellmanpublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](publickey/hpkepublickeyserialization-implementations.md)

## See Also

### Using keys

- [PrivateKey](privatekey.md) — A P-384 private key used for key agreement.
