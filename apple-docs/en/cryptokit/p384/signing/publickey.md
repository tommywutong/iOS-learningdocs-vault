---
title: P384.Signing.PublicKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p384/signing/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing/publickey.json'
content_hash: 'sha256:e89b13dc8a469233'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [P384](../../p384.md) · [Signing](../signing.md)

# P384.Signing.PublicKey

<sub>Structure</sub>

A P-384 public key used to verify cryptographic signatures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PublicKey
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a key

- [init(rawRepresentation:)](<publickey/init(rawrepresentation_).md>) — Creates a P-384 public key for signing from a collection of bytes.
- [init(compactRepresentation:)](<publickey/init(compactrepresentation_).md>) — Creates a P-384 public key for signing from a compact representation of the key.
- [init(compressedRepresentation:)](<publickey/init(compressedrepresentation_).md>) — Creates a P-384 public key for signing from a compressed representation of the key.
- [init(derRepresentation:)](<publickey/init(derrepresentation_).md>) — Creates a P-384 public key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation:)](<publickey/init(pemrepresentation_).md>) — Creates a P-384 public key for signing from a Privacy-Enhanced Mail (PEM) representation.
- [init(x963Representation:)](<publickey/init(x963representation_).md>) — Creates a P-384 public key for signing from an ANSI x9.63 representation.

### Representing the key

- [rawRepresentation](publickey/rawrepresentation.md) — A full representation of the public key.
- [compactRepresentation](publickey/compactrepresentation.md) — A compact representation of the public key.
- [compressedRepresentation](publickey/compressedrepresentation.md) — A compressed representation of the public key.
- [derRepresentation](publickey/derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [pemRepresentation](publickey/pemrepresentation.md) — A Privacy-Enhanced Mail (PEM) representation of the public key.
- [x963Representation](publickey/x963representation.md) — An ANSI x9.63 representation of the public key.

### Verifying a signature

- [isValidSignature(_:for:)](<publickey/isvalidsignature(__for_)-2zf75.md>) — Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a block of data over the P-384 elliptic curve.
- [isValidSignature(_:for:)](<publickey/isvalidsignature(__for_)-1hrtv.md>) — Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a digest over the P-384 elliptic curve.
- [ECDSASignature](ecdsasignature.md) — A P-384 elliptic curve digital signature algorithm (ECDSA) signature.

## See Also

### Using keys

- [PrivateKey](privatekey.md) — A P-384 private key used to create cryptographic signatures.
