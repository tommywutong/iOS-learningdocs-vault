---
title: tls_ciphersuite_t
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/tls_ciphersuite_t
source_url: 'https://developer.apple.com/documentation/security/tls_ciphersuite_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/tls_ciphersuite_t.json'
content_hash: 'sha256:6b8c44de9d7fd027'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# tls_ciphersuite_t

<sub>Enumeration</sub>

The collection of valid ciphersuites.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum tls_ciphersuite_t
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### AES

- [tls_ciphersuite_AES_128_GCM_SHA256](tls_ciphersuite_t/aes_128_gcm_sha256.md)
- [tls_ciphersuite_AES_256_GCM_SHA384](tls_ciphersuite_t/aes_256_gcm_sha384.md)

### Cha Cha Poly

- [tls_ciphersuite_CHACHA20_POLY1305_SHA256](tls_ciphersuite_t/chacha20_poly1305_sha256.md)

### Elliptic Curve

- [tls_ciphersuite_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA](tls_ciphersuite_t/ecdhe_ecdsa_with_3des_ede_cbc_sha.md) _(deprecated)_
- [tls_ciphersuite_ECDHE_ECDSA_WITH_AES_128_CBC_SHA](tls_ciphersuite_t/ecdhe_ecdsa_with_aes_128_cbc_sha.md)
- [tls_ciphersuite_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256](tls_ciphersuite_t/ecdhe_ecdsa_with_aes_128_cbc_sha256.md)
- [tls_ciphersuite_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256](tls_ciphersuite_t/ecdhe_ecdsa_with_aes_128_gcm_sha256.md)
- [tls_ciphersuite_ECDHE_ECDSA_WITH_AES_256_CBC_SHA](tls_ciphersuite_t/ecdhe_ecdsa_with_aes_256_cbc_sha.md)
- [tls_ciphersuite_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384](tls_ciphersuite_t/ecdhe_ecdsa_with_aes_256_cbc_sha384.md)
- [tls_ciphersuite_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384](tls_ciphersuite_t/ecdhe_ecdsa_with_aes_256_gcm_sha384.md)
- [tls_ciphersuite_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256](tls_ciphersuite_t/ecdhe_ecdsa_with_chacha20_poly1305_sha256.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA](tls_ciphersuite_t/ecdhe_rsa_with_3des_ede_cbc_sha.md) _(deprecated)_
- [tls_ciphersuite_ECDHE_RSA_WITH_AES_128_CBC_SHA](tls_ciphersuite_t/ecdhe_rsa_with_aes_128_cbc_sha.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_AES_128_CBC_SHA256](tls_ciphersuite_t/ecdhe_rsa_with_aes_128_cbc_sha256.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_AES_128_GCM_SHA256](tls_ciphersuite_t/ecdhe_rsa_with_aes_128_gcm_sha256.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_AES_256_CBC_SHA](tls_ciphersuite_t/ecdhe_rsa_with_aes_256_cbc_sha.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_AES_256_CBC_SHA384](tls_ciphersuite_t/ecdhe_rsa_with_aes_256_cbc_sha384.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_AES_256_GCM_SHA384](tls_ciphersuite_t/ecdhe_rsa_with_aes_256_gcm_sha384.md)
- [tls_ciphersuite_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256](tls_ciphersuite_t/ecdhe_rsa_with_chacha20_poly1305_sha256.md)

### RSA

- [tls_ciphersuite_RSA_WITH_3DES_EDE_CBC_SHA](tls_ciphersuite_t/rsa_with_3des_ede_cbc_sha.md) _(deprecated)_
- [tls_ciphersuite_RSA_WITH_AES_128_CBC_SHA](tls_ciphersuite_t/rsa_with_aes_128_cbc_sha.md)
- [tls_ciphersuite_RSA_WITH_AES_128_CBC_SHA256](tls_ciphersuite_t/rsa_with_aes_128_cbc_sha256.md)
- [tls_ciphersuite_RSA_WITH_AES_128_GCM_SHA256](tls_ciphersuite_t/rsa_with_aes_128_gcm_sha256.md)
- [tls_ciphersuite_RSA_WITH_AES_256_CBC_SHA](tls_ciphersuite_t/rsa_with_aes_256_cbc_sha.md)
- [tls_ciphersuite_RSA_WITH_AES_256_CBC_SHA256](tls_ciphersuite_t/rsa_with_aes_256_cbc_sha256.md)
- [tls_ciphersuite_RSA_WITH_AES_256_GCM_SHA384](tls_ciphersuite_t/rsa_with_aes_256_gcm_sha384.md)

### Initializers

- [init(rawValue:)](<tls_ciphersuite_t/init(rawvalue_).md>)
