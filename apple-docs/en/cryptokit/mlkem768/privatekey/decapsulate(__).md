---
title: 'decapsulate(_:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mlkem768/privatekey/decapsulate(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/decapsulate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/privatekey/decapsulate%28_%3A%29.json'
content_hash: 'sha256:1cba965e93d5e0a5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# decapsulate(_:)

<sub>Instance Method</sub>

Decapsulate a shared secret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

## Parameters

- `encapsulated` — An encapsulated shared secret, that you get by calling [encapsulate()](<../publickey/encapsulate().md>) on the corresponding public key.

## Return Value

The shared secret.
