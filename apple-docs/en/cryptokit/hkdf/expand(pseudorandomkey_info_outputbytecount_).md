---
title: 'expand(pseudoRandomKey:info:outputByteCount:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hkdf/expand(pseudorandomkey:info:outputbytecount:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf/expand(pseudorandomkey:info:outputbytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf/expand%28pseudorandomkey%3Ainfo%3Aoutputbytecount%3A%29.json'
content_hash: 'sha256:ba62dedb04ce4b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HKDF](../hkdf.md)

# expand(pseudoRandomKey:info:outputByteCount:)

<sub>Type Method</sub>

Expands cryptographically strong key material into a derived symmetric key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func expand<PRK, Info>(pseudoRandomKey prk: PRK, info: Info?, outputByteCount: Int) -> SymmetricKey where PRK : ContiguousBytes, Info : DataProtocol
```

## Parameters

- `prk` — A pseudorandom, cryptographically strong key generated from the `extract(inputKeyMaterial:salt:)` function.

- `info` — The shared information to use for key derivation.

- `outputByteCount` — The length in bytes of the resulting symmetric key.

## Return Value

The derived symmetric key.

## Discussion

Generate cryptographically strong key material to use with this function by calling `extract(inputKeyMaterial:salt:)`.
