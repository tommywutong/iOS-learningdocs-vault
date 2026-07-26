---
title: SharedSecret
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sharedsecret
source_url: 'https://developer.apple.com/documentation/cryptokit/sharedsecret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sharedsecret.json'
content_hash: 'sha256:adb1d3b32851c955'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# SharedSecret

<sub>Structure</sub>

A key agreement result from which you can derive a symmetric cryptographic key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SharedSecret
```

## Overview

Generate a shared secret by calling your private key’s `sharedSecretFromKeyAgreement(publicKeyShare:)` method with the public key from another party. The other party computes the same secret by passing your public key to the the equivalent method on their own private key.

The shared secret isn’t suitable as a symmetric cryptographic key ([SymmetricKey](symmetrickey.md)) by itself. However, you use it to generate a key by calling either the [hkdfDerivedSymmetricKey(using:salt:sharedInfo:outputByteCount:)](<sharedsecret/hkdfderivedsymmetrickey(using_salt_sharedinfo_outputbytecount_).md>) or [x963DerivedSymmetricKey(using:sharedInfo:outputByteCount:)](<sharedsecret/x963derivedsymmetrickey(using_sharedinfo_outputbytecount_).md>) method of the shared secret. After the other party does the same, then you both share a symmetric key suitable for creating a message authentication code like [HMAC](hmac.md), or for opening and closing a sealed box with a cipher like [ChaChaPoly](chachapoly.md) or [AES](aes.md).

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Deriving keys

- [hkdfDerivedSymmetricKey(using:salt:sharedInfo:outputByteCount:)](<sharedsecret/hkdfderivedsymmetrickey(using_salt_sharedinfo_outputbytecount_).md>) — Derives a symmetric encryption key from the secret using HKDF key derivation.
- [x963DerivedSymmetricKey(using:sharedInfo:outputByteCount:)](<sharedsecret/x963derivedsymmetrickey(using_sharedinfo_outputbytecount_).md>) — Derives a symmetric encryption key from the secret using x9.63 key derivation.

### Comparing shared secrets

- [==(_:_:)](<sharedsecret/==(____).md>) — Determines whether a shared secret is equivalent to a collection of contiguous bytes.

## See Also

### Public key cryptography

- [Curve25519](curve25519.md) — An elliptic curve that enables X25519 key agreement and Ed25519 signatures.
- [P521](p521.md) — An elliptic curve that enables NIST P-521 signatures and key agreement.
- [P384](p384.md) — An elliptic curve that enables NIST P-384 signatures and key agreement.
- [P256](p256.md) — An elliptic curve that enables NIST P-256 signatures and key agreement.
- [SecureEnclave](secureenclave.md) — A representation of a device’s hardware-based key manager.
- [HPKE](hpke.md) — A container for hybrid public key encryption (HPKE) operations.
