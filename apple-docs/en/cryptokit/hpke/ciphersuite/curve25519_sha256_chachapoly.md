---
title: Curve25519_SHA256_ChachaPoly
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/ciphersuite/curve25519_sha256_chachapoly
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/ciphersuite/curve25519_sha256_chachapoly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/ciphersuite/curve25519_sha256_chachapoly.json'
content_hash: 'sha256:0c1db7e5cef68ffa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Ciphersuite](../ciphersuite.md)

# Curve25519_SHA256_ChachaPoly

<sub>Type Property</sub>

A cipher suite for HPKE that uses X25519 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the ChaCha20 stream cipher with the Poly1305 message authentication code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let Curve25519_SHA256_ChachaPoly: HPKE.Ciphersuite
```

## See Also

### Using elliptic curve cipher suites

- [P256_SHA256_AES_GCM_256](p256_sha256_aes_gcm_256.md) — A cipher suite for HPKE that uses NIST P-256 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [P384_SHA384_AES_GCM_256](p384_sha384_aes_gcm_256.md) — A cipher suite that you use for HPKE using NIST P-384 elliptic curve key agreement, SHA-2 key derivation with a 384-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [P521_SHA512_AES_GCM_256](p521_sha512_aes_gcm_256.md) — A cipher suite for HPKE that uses NIST P-521 elliptic curve key agreement, SHA-2 key derivation with a 512-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
