---
title: HPKE.AEAD
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/aead
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/aead'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/aead.json'
content_hash: 'sha256:0fc4dd38e1fd240f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKE](../hpke.md)

# HPKE.AEAD

<sub>Enumeration</sub>

The authenticated encryption with associated data (AEAD) algorithms to use in HPKE.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AEAD
```

## Relationships

- **Conforms To**: [CaseIterable](../../swift/caseiterable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [HPKE.AEAD.AES_GCM_128](aead/aes_gcm_128.md) — An Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 128 bits.
- [HPKE.AEAD.AES_GCM_256](aead/aes_gcm_256.md) — An Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [HPKE.AEAD.chaChaPoly](aead/chachapoly.md) — A ChaCha20 stream cipher with the Poly1305 message authentication code.
- [HPKE.AEAD.exportOnly](aead/exportonly.md) — An export-only mode.

## See Also

### Choosing cryptographic algorithms

- [Ciphersuite](ciphersuite.md) — Cipher suites to use in hybrid public key encryption (HPKE).
- [KDF](kdf.md) — The key derivation functions to use in HPKE.
- [KEM](kem.md) — The key encapsulation mechanisms to use in HPKE.
- [DHKEM](dhkem.md) — A container for Diffie-Hellman key encapsulation mechanisms (KEMs).
