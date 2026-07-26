---
title: Curve25519.Signing
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/curve25519/signing
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/signing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/signing.json'
content_hash: 'sha256:2d3f651baf572bfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Curve25519](../curve25519.md)

# Curve25519.Signing

<sub>Enumeration</sub>

A mechanism used to create or verify a cryptographic signature using Ed25519.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Signing
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Using keys

- [PrivateKey](signing/privatekey.md) — A Curve25519 private key used to create cryptographic signatures.
- [PublicKey](signing/publickey.md) — A Curve25519 public key used to verify cryptographic signatures.

## See Also

### Performing operations

- [KeyAgreement](keyagreement.md) — A mechanism used to create a shared secret between two users by performing X25519 key agreement.
