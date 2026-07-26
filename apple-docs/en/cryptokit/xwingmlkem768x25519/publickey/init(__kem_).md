---
title: 'init(_:kem:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/xwingmlkem768x25519/publickey/init(_:kem:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey/init(_:kem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/xwingmlkem768x25519/publickey/init%28_%3Akem%3A%29.json'
content_hash: 'sha256:07584b09a60a3d8f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [XWingMLKEM768X25519](../../xwingmlkem768x25519.md) · [PublicKey](../publickey.md)

# init(_:kem:)

<sub>Initializer</sub>

Creates an X-Wing public key for use with HPKE.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(_ serialization: D, kem: HPKE.KEM) throws where D : ContiguousBytes
```

## Discussion

- serialization: The serialized bytes of the public key.
- kem: The key encapsulation mechanism to use with the public key.

> [!danger] Throws
> [HPKE.Errors.inconsistentCiphersuiteAndKey](../../hpke/errors/inconsistentciphersuiteandkey.md) if the key encapsulation mechanism requested is incompatible with this public key.
