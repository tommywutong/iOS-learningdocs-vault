---
title: SecureEnclave.P256.KeyAgreement
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/p256/keyagreement
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/keyagreement.json'
content_hash: 'sha256:458e037e7e01e983'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [SecureEnclave](../../secureenclave.md) · [P256](../p256.md)

# SecureEnclave.P256.KeyAgreement

<sub>Enumeration</sub>

A mechanism used to create a shared secret between two users by performing NIST P-256 elliptic curve Diffie Hellman (ECDH) key exchange within the Secure Enclave.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KeyAgreement
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Using keys

- [PrivateKey](keyagreement/privatekey.md) — A P-256 private key used for key agreement.

## See Also

### Performing operations

- [Signing](signing.md) — A mechanism used to create or verify a cryptographic signature using the NIST P-256 elliptic curve digital signature algorithm (ECDSA) within the Secure Enclave.
