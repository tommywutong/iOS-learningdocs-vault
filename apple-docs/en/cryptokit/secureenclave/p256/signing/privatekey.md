---
title: SecureEnclave.P256.Signing.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/p256/signing/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/signing/privatekey.json'
content_hash: 'sha256:5b8f2e356377324f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [P256](../../p256.md) · [Signing](../signing.md)

# SecureEnclave.P256.Signing.PrivateKey

<sub>Structure</sub>

A P-256 private key used for signing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [init(dataRepresentation:authenticationContext:)](<privatekey/init(datarepresentation_authenticationcontext_).md>) — Creates a P-256 private key for signing from a data representation of the key with the given authentication context.
- [init(compactRepresentable:accessControl:authenticationContext:)](<privatekey/init(compactrepresentable_accesscontrol_authenticationcontext_).md>) — Creates a P-256 private key for signing with the specified access control.

### Representing the key

- [dataRepresentation](privatekey/datarepresentation.md) — A data representation of the private key.

### Getting the public key

- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Generating a signature

- [signature(for:)](<privatekey/signature(for_)-3xogs.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.
- [signature(for:)](<privatekey/signature(for_)-76j0u.md>) — Generates an elliptic curve digital signature algorithm (ECDSA) signature of the given data over the P-256 elliptic curve, using SHA-256 as the hash function.

### Initializers

- [init(compactRepresentable:accessControl:)](<privatekey/init(compactrepresentable_accesscontrol_).md>) — Creates a P-256 private key for signing with the specified access control.
- [init(dataRepresentation:)](<privatekey/init(datarepresentation_).md>) — Creates a P-256 private key for signing from the specified data representation.
