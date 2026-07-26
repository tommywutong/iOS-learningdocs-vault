---
title: Curve25519.Signing.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/curve25519/signing/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/signing/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/signing/publickey.json'
content_hash: 'sha256:f8a5c29b84bc8553'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [Curve25519](../../curve25519.md) · [Signing](../signing.md)

# Curve25519.Signing.PublicKey

<sub>Structure</sub>

A Curve25519 public key used to verify cryptographic signatures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a public key

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>) — Creates a Curve25519 public key from a data representation.

### Representing the key

- [rawRepresentation](publickey/rawrepresentation.md) — A representation of the public key.

### Verifying a signature

- [isValidSignature(_:for:)](<publickey/isvalidsignature(__for_).md>) — Verifies an EdDSA signature over Curve25519.

## See Also

### Using keys

- [PrivateKey](privatekey.md) — A Curve25519 private key used to create cryptographic signatures.
