---
title: SecureEnclave
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave.json'
content_hash: 'sha256:35fae0913a04ef9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SecureEnclave

<sub>Enumeration</sub>

A representation of a device’s hardware-based key manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SecureEnclave
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Checking availability

- [isAvailable](secureenclave/isavailable.md) — A Boolean value that indicates if the device supports Secure Enclave access.

### Using the secure enclave

- [P256](secureenclave/p256.md) — An elliptic curve that enables NIST P-256 signatures and key agreement within the Secure Enclave.
- [MLKEM1024](secureenclave/mlkem1024.md) — An implementation of the MLKEM1024 key encapsulation mechanism that operates within the Secure Enclave.
- [MLKEM768](secureenclave/mlkem768.md) — An implementation of the MLKEM768 key encapsulation mechanism that operates within the Secure Enclave.

### Enumerations

- [MLDSA65](secureenclave/mldsa65.md)
- [MLDSA87](secureenclave/mldsa87.md)

## See Also

### Public key cryptography

- [Curve25519](curve25519.md) — An elliptic curve that enables X25519 key agreement and Ed25519 signatures.
- [P521](p521.md) — An elliptic curve that enables NIST P-521 signatures and key agreement.
- [P384](p384.md) — An elliptic curve that enables NIST P-384 signatures and key agreement.
- [P256](p256.md) — An elliptic curve that enables NIST P-256 signatures and key agreement.
- [SharedSecret](sharedsecret.md) — A key agreement result from which you can derive a symmetric cryptographic key.
- [HPKE](hpke.md) — A container for hybrid public key encryption (HPKE) operations.
