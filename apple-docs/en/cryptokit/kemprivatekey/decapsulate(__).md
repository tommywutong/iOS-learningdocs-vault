---
title: 'decapsulate(_:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/kemprivatekey/decapsulate(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/kemprivatekey/decapsulate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kemprivatekey/decapsulate%28_%3A%29.json'
content_hash: 'sha256:ccfa5b93fa4653e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEMPrivateKey](../kemprivatekey.md)

# decapsulate(_:)

<sub>Instance Method</sub>

Recovers a shared secret from an encapsulated representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decapsulate(_ encapsulated: Data) throws -> SymmetricKey
```

## Parameters

- `encapsulated` — The encapsulated shared secret that someone created using this key’s [publicKey](publickey-swift.property.md).

## Return Value

The decapsulated shared secret.
