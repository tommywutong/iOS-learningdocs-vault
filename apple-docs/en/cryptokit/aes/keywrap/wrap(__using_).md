---
title: 'wrap(_:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/aes/keywrap/wrap(_:using:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/keywrap/wrap(_:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/keywrap/wrap%28_%3Ausing%3A%29.json'
content_hash: 'sha256:b1e190bc30d7518a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [AES](../../aes.md) · [KeyWrap](../keywrap.md)

# wrap(_:using:)

<sub>Type Method</sub>

Wraps a key using the AES wrap algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func wrap(_ keyToWrap: SymmetricKey, using kek: SymmetricKey) throws -> Data
```

## Parameters

- `keyToWrap` — The key to wrap.

- `kek` — The key encryption key.

## Return Value

The wrapped key.

## Discussion

Wrap is an implementation of the AES key wrap algorithm as specified in IETF RFC 3394.
