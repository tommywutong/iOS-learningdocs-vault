---
title: P384.Signing
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p384/signing
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing.json'
content_hash: 'sha256:8fdbc21700aeebce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [P384](../p384.md)

# P384.Signing

<sub>Enumeration</sub>

A mechanism used to create or verify a cryptographic signature using the NIST P-384 elliptic curve digital signature algorithm (ECDSA).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Signing
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Using keys

- [PrivateKey](signing/privatekey.md) — A P-384 private key used to create cryptographic signatures.
- [PublicKey](signing/publickey.md) — A P-384 public key used to verify cryptographic signatures.

### Structures

- [ECDSASignature](signing/ecdsasignature.md) — A P-384 elliptic curve digital signature algorithm (ECDSA) signature.

## See Also

### Performing operations

- [KeyAgreement](keyagreement.md) — A mechanism used to create a shared secret between two users by performing NIST P-384 elliptic curve Diffie Hellman (ECDH) key exchange.
