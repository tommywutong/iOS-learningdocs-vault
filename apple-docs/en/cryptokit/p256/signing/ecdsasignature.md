---
title: P256.Signing.ECDSASignature
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p256/signing/ecdsasignature
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/ecdsasignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/ecdsasignature.json'
content_hash: 'sha256:ed11127a2b9f772d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [P256](../../p256.md) · [Signing](../signing.md)

# P256.Signing.ECDSASignature

<sub>Structure</sub>

A P-256 elliptic curve digital signature algorithm (ECDSA) signature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ECDSASignature
```

## Relationships

- **Conforms To**: [ContiguousBytes](../../../foundation/contiguousbytes.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a signature

- [init(derRepresentation:)](<ecdsasignature/init(derrepresentation_).md>) — Creates a P-256 digital signature from a Distinguished Encoding Rules (DER) encoded representation.
- [init(rawRepresentation:)](<ecdsasignature/init(rawrepresentation_).md>) — Creates a P-256 digital signature from a raw representation.

### Representing the signature

- [derRepresentation](ecdsasignature/derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of a P-256 digital signature.
- [rawRepresentation](ecdsasignature/rawrepresentation.md) — A raw data representation of a P-256 digital signature.

## See Also

### Creating a signature

- [signature(for:)](<privatekey/signature(for_)-5h94p.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-256 elliptic curve, using SHA-256 as the hash function.
- [signature(for:)](<privatekey/signature(for_)-1iyzc.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.
