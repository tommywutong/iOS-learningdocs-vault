---
title: aead
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/ciphersuite/aead
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/ciphersuite/aead'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/ciphersuite/aead.json'
content_hash: 'sha256:958989ecf64273a4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Ciphersuite](../ciphersuite.md)

# aead

<sub>Instance Property</sub>

The authenticated encryption with additional data (AEAD) algorithm for encrypting and decrypting messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let aead: HPKE.AEAD
```

## See Also

### Inspecting a cipher suite

- [kdf](kdf.md) — The key derivation function (KDF) for deriving the symmetric key.
- [kem](kem.md) — The key encapsulation mechanism (KEM) for encapsulating the symmetric key.
