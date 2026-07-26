---
title: P521_SHA512_AES_GCM_256
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/ciphersuite/p521_sha512_aes_gcm_256
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/ciphersuite/p521_sha512_aes_gcm_256'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/ciphersuite/p521_sha512_aes_gcm_256.json'
content_hash: 'sha256:0151b7da41fb5eba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Ciphersuite](../ciphersuite.md)

# P521_SHA512_AES_GCM_256

<sub>Type Property</sub>

A cipher suite for HPKE that uses NIST P-521 elliptic curve key agreement, SHA-2 key derivation with a 512-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let P521_SHA512_AES_GCM_256: HPKE.Ciphersuite
```

## See Also

### Using elliptic curve cipher suites

- [Curve25519_SHA256_ChachaPoly](curve25519_sha256_chachapoly.md) — A cipher suite for HPKE that uses X25519 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the ChaCha20 stream cipher with the Poly1305 message authentication code.
- [P256_SHA256_AES_GCM_256](p256_sha256_aes_gcm_256.md) — A cipher suite for HPKE that uses NIST P-256 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [P384_SHA384_AES_GCM_256](p384_sha384_aes_gcm_256.md) — A cipher suite that you use for HPKE using NIST P-384 elliptic curve key agreement, SHA-2 key derivation with a 384-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
