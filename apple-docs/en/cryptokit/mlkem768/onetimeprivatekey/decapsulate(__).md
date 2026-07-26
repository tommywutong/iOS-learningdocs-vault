---
title: 'decapsulate(_:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/mlkem768/onetimeprivatekey/decapsulate(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/onetimeprivatekey/decapsulate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/onetimeprivatekey/decapsulate%28_%3A%29.json'
content_hash: 'sha256:8489ea00515d2aa8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM768](../../mlkem768.md) · [OneTimePrivateKey](../onetimeprivatekey.md)

# decapsulate(_:)

<sub>Instance Method</sub>

Decapsulate a shared secret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

## Parameters

- `encapsulated` — An encapsulated shared secret, that you get by calling [encapsulate()](<../publickey/encapsulate().md>) on the corresponding public key.

## Return Value

The shared secret.
