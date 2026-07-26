---
title: P384.Signing.ECDSASignature
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/p384/signing/ecdsasignature
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing/ecdsasignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing/ecdsasignature.json'
content_hash: 'sha256:de70709b2e8e2539'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [P384](../../p384.md) · [Signing](../signing.md)

# P384.Signing.ECDSASignature

<sub>Structure</sub>

A P-384 elliptic curve digital signature algorithm (ECDSA) signature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ECDSASignature
```

## Relationships

- **Conforms To**: [ContiguousBytes](../../../foundation/contiguousbytes.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a signature

- [init(derRepresentation:)](<ecdsasignature/init(derrepresentation_).md>) — Creates a P-384 digital signature from a Distinguished Encoding Rules (DER) encoded representation.
- [init(rawRepresentation:)](<ecdsasignature/init(rawrepresentation_).md>) — Creates a P-384 digital signature from a raw representation.

### Representing the signature

- [derRepresentation](ecdsasignature/derrepresentation.md) — A Distinguished Encoding Rules (DER) encoded representation of a P-384 digital signature.
- [rawRepresentation](ecdsasignature/rawrepresentation.md) — A raw data representation of a P-384 digital signature.

## See Also

### Creating a signature

- [signature(for:)](<privatekey/signature(for_)-8nncg.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-384 elliptic curve, using SHA-384 as the hash function.
- [signature(for:)](<privatekey/signature(for_)-wrsj.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-384 elliptic curve.
