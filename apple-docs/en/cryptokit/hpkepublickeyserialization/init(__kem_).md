---
title: 'init(_:kem:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpkepublickeyserialization/init(_:kem:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization/init(_:kem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpkepublickeyserialization/init%28_%3Akem%3A%29.json'
content_hash: 'sha256:be6fe729792e656f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKEPublicKeySerialization](../hpkepublickeyserialization.md)

# init(_:kem:)

<sub>Initializer</sub>

Creates a public key from an encoded representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(_ serialization: D, kem: HPKE.KEM) throws where D : ContiguousBytes
```

## Discussion

- serialization: The serialized key data.
- kem: The key encapsulation mechanism that the sender used to encapsulate the key.
