---
title: 'expand(pseudoRandomKey:info:into:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/hkdf/expand(pseudorandomkey:info:into:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf/expand(pseudorandomkey:info:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf/expand%28pseudorandomkey%3Ainfo%3Ainto%3A%29.json'
content_hash: 'sha256:55bbaa91363ae216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HKDF](../hkdf.md)

# expand(pseudoRandomKey:info:into:)

<sub>Type Method</sub>

Expands cryptographically strong key material into a derived symmetric key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func expand(pseudoRandomKey prk: RawSpan, info: RawSpan?, into output: inout OutputRawSpan)
```

## Parameters

- `prk` — A pseudorandom, cryptographically strong key generated from the `extract(inputKeyMaterial:salt:)` function.

- `info` — The shared information to use for key derivation.

## Discussion

Generate cryptographically strong key material to use with this function by calling `extract(inputKeyMaterial:salt:)`.
