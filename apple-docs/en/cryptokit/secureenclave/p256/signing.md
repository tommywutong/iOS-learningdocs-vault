---
title: SecureEnclave.P256.Signing
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/p256/signing
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/signing.json'
content_hash: 'sha256:aec39b6af400c2f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [SecureEnclave](../../secureenclave.md) · [P256](../p256.md)

# SecureEnclave.P256.Signing

<sub>Enumeration</sub>

A mechanism used to create or verify a cryptographic signature using the NIST P-256 elliptic curve digital signature algorithm (ECDSA) within the Secure Enclave.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Signing
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Using keys

- [PrivateKey](signing/privatekey.md) — A P-256 private key used for signing.

## See Also

### Performing operations

- [KeyAgreement](keyagreement.md) — A mechanism used to create a shared secret between two users by performing NIST P-256 elliptic curve Diffie Hellman (ECDH) key exchange within the Secure Enclave.
