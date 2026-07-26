---
title: Curve25519.KeyAgreement
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/curve25519/keyagreement
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/keyagreement.json'
content_hash: 'sha256:4962f31aaecbf991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Curve25519](../curve25519.md)

# Curve25519.KeyAgreement

<sub>Enumeration</sub>

A mechanism used to create a shared secret between two users by performing X25519 key agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KeyAgreement
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Using keys

- [PrivateKey](keyagreement/privatekey.md) — A Curve25519 private key used for key agreement.
- [PublicKey](keyagreement/publickey.md) — A Curve25519 public key used for key agreement.

## See Also

### Performing operations

- [Signing](signing.md) — A mechanism used to create or verify a cryptographic signature using Ed25519.
