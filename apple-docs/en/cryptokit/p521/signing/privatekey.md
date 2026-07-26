---
title: P521.Signing.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p521/signing/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/signing/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/signing/privatekey.json'
content_hash: 'sha256:ee5f85d359d76282'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [P521](../../p521.md) · [Signing](../signing.md)

# P521.Signing.PrivateKey

<sub>Structure</sub>

A P-521 private key used to create cryptographic signatures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a key

- [init(rawRepresentation:)](<privatekey/init(rawrepresentation_).md>) — Creates a P-521 private key for signing from a collection of bytes.
- [init(compactRepresentable:)](<privatekey/init(compactrepresentable_).md>) — Creates a random P-521 private key for signing.
- [init(derRepresentation:)](<privatekey/init(derrepresentation_).md>) — Creates a P-521 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<privatekey/init(pemrepresentation_).md>) — Creates a P-521 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init(x963Representation:)](<privatekey/init(x963representation_).md>) — Creates a P-521 private key for signing from an ANSI x9.63 representation.

### Representing the key

- [rawRepresentation](privatekey/rawrepresentation.md) — A data representation of the private key.
- [derRepresentation](privatekey/derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [pemRepresentation](privatekey/pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the private key.
- [x963Representation](privatekey/x963representation.md) — An ANSI x9.63 representation of the private key.

### Finding the public key

- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Creating a signature

- [signature(for:)](<privatekey/signature(for_)-34g01.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-521 elliptic curve, using SHA-512 as the hash function.
- [signature(for:)](<privatekey/signature(for_)-7rxva.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-521 elliptic curve.
- [ECDSASignature](ecdsasignature.md) — A P-521 elliptic curve digital signature algorithm (ECDSA) signature.

## See Also

### Using keys

- [PublicKey](publickey.md) — A P-521 public key used to verify cryptographic signatures.
