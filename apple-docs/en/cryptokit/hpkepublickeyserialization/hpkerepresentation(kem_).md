---
title: 'hpkeRepresentation(kem:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpkepublickeyserialization/hpkerepresentation(kem:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization/hpkerepresentation(kem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkepublickeyserialization/hpkerepresentation%28kem%3A%29.json'
content_hash: 'sha256:308951c3dd700b4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKEPublicKeySerialization](../hpkepublickeyserialization.md)

# hpkeRepresentation(kem:)

<sub>Instance Method</sub>

Creates an encoded representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hpkeRepresentation(kem: HPKE.KEM) throws -> Data
```

## Return Value

The encoded key data.

## Discussion

- kem: The key encapsulation mechanism for encapsulating the key.
