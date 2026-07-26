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
doc_path: '/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey/decapsulate(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey/decapsulate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey/decapsulate%28_%3A%29.json'
content_hash: 'sha256:93da508864287d12'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [XWingMLKEM768X25519](../../xwingmlkem768x25519.md) · [OneTimePrivateKey](../onetimeprivatekey.md)

# decapsulate(_:)

<sub>Instance Method</sub>

Decapsulate a shared secret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func decapsulate(_ encapsulated: Data) throws -> SymmetricKey
```

## Parameters

- `encapsulated` — An encapsulated shared secret, that you get by calling `XWingMLKEM768X25519/PublicKey/encapsulate()` on the corresponding public key.

## Return Value

The shared secret.
