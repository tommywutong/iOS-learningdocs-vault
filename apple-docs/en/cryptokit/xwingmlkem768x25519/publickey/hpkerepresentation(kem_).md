---
title: 'hpkeRepresentation(kem:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/xwingmlkem768x25519/publickey/hpkerepresentation(kem:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey/hpkerepresentation(kem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/xwingmlkem768x25519/publickey/hpkerepresentation%28kem%3A%29.json'
content_hash: 'sha256:b453674130eaef89'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [XWingMLKEM768X25519](../../xwingmlkem768x25519.md) · [PublicKey](../publickey.md)

# hpkeRepresentation(kem:)

<sub>Instance Method</sub>

Creates a serialized representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hpkeRepresentation(kem: HPKE.KEM) throws -> Data
```

## Return Value

The serialized representation of the public key.

## Discussion

- kem: The Key Encapsulation Mechanism to use with the public key.

> [!danger] Throws
> [HPKE.Errors.inconsistentCiphersuiteAndKey](../../hpke/errors/inconsistentciphersuiteandkey.md) if the key encapsulation mechanism requested is incompatible with this public key.
