---
title: 'unwrap(_:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/aes/keywrap/unwrap(_:using:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/keywrap/unwrap(_:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/keywrap/unwrap%28_%3Ausing%3A%29.json'
content_hash: 'sha256:daa46470a0c67b67'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [AES](../../aes.md) · [KeyWrap](../keywrap.md)

# unwrap(_:using:)

<sub>Type Method</sub>

Unwraps a key using the AES wrap algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func unwrap<WrappedKey>(_ wrappedKey: WrappedKey, using kek: SymmetricKey) throws -> SymmetricKey where WrappedKey : DataProtocol
```

## Parameters

- `wrappedKey` — The key to unwrap.

- `kek` — The key encryption key.

## Return Value

The unwrapped key.

## Discussion

Wrap is an implementation of the AES key wrap algorithm as specified in IETF RFC 3394. The method throws an error is the key was incorrectly wrapped.
