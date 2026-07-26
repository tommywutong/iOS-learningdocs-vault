---
title: 'init(kem:kdf:aead:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/ciphersuite/init(kem:kdf:aead:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/ciphersuite/init(kem:kdf:aead:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/ciphersuite/init%28kem%3Akdf%3Aaead%3A%29.json'
content_hash: 'sha256:e4e57b7a415f68a7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Ciphersuite](../ciphersuite.md)

# init(kem:kdf:aead:)

<sub>Initializer</sub>

Creates an HPKE cipher suite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(kem: HPKE.KEM, kdf: HPKE.KDF, aead: HPKE.AEAD)
```

## Parameters

- `kem` — The key encapsulation mechanism for encapsulating the symmetric key.

- `kdf` — The key derivation function for deriving the symmetric key.

- `aead` — The authenticated encryption with additional data (AEAD) algorithm for encrypting and decrypting messages.
