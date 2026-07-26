---
title: Curve25519.Signing.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/curve25519/signing/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/signing/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/signing/privatekey.json'
content_hash: 'sha256:2d87b4451698b87e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [Curve25519](../../curve25519.md) · [Signing](../signing.md)

# Curve25519.Signing.PrivateKey

<sub>Structure</sub>

A Curve25519 private key used to create cryptographic signatures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [init()](<privatekey/init().md>) — Creates a random Curve25519 private key for signing.
- [init(rawRepresentation:)](<privatekey/init(rawrepresentation_).md>) — Creates a Curve25519 private key for signing from a data representation.

### Reporting the private key

- [rawRepresentation](privatekey/rawrepresentation.md) — The raw representation of the key as a collection of contiguous bytes.

### Finding the public key

- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Creating a signature

- [signature(for:)](<privatekey/signature(for_).md>) — Generates an EdDSA signature over Curve25519.

## See Also

### Using keys

- [PublicKey](publickey.md) — A Curve25519 public key used to verify cryptographic signatures.
