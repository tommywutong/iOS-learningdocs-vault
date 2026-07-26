---
title: HPKE.KDF
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/kdf
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/kdf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/kdf.json'
content_hash: 'sha256:d24cbd8955ea41cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKE](../hpke.md)

# HPKE.KDF

<sub>Enumeration</sub>

The key derivation functions to use in HPKE.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KDF
```

## Relationships

- **Conforms To**: [CaseIterable](../../swift/caseiterable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [HPKE.KDF.HKDF_SHA256](kdf/hkdf_sha256.md) — An HMAC-based key derivation function that uses SHA-2 hashing with a 256-bit digest.
- [HPKE.KDF.HKDF_SHA384](kdf/hkdf_sha384.md) — An HMAC-based key derivation function that uses SHA-2 hashing with a 384-bit digest.
- [HPKE.KDF.HKDF_SHA512](kdf/hkdf_sha512.md) — An HMAC-based key derivation function that uses SHA-2 hashing with a 512-bit digest.

## See Also

### Choosing cryptographic algorithms

- [Ciphersuite](ciphersuite.md) — Cipher suites to use in hybrid public key encryption (HPKE).
- [AEAD](aead.md) — The authenticated encryption with associated data (AEAD) algorithms to use in HPKE.
- [KEM](kem.md) — The key encapsulation mechanisms to use in HPKE.
- [DHKEM](dhkem.md) — A container for Diffie-Hellman key encapsulation mechanisms (KEMs).
