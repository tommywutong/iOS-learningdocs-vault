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
doc_path: '/documentation/cryptokit/kemonetimeprivatekey/decapsulate(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey/decapsulate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kemonetimeprivatekey/decapsulate%28_%3A%29.json'
content_hash: 'sha256:e9144cf2130d5991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEMOneTimePrivateKey](../kemonetimeprivatekey.md)

# decapsulate(_:)

<sub>Instance Method</sub>

Recovers a shared secret from an encapsulated representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func decapsulate(_ encapsulated: Data) throws -> SymmetricKey
```

## Parameters

- `encapsulated` — The encapsulated shared secret that someone created using this key’s [publicKey](publickey-swift.property.md).

## Return Value

The decapsulated shared secret.
