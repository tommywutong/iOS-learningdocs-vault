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
doc_path: '/documentation/cryptokit/secureenclave/mlkem768/privatekey/decapsulate(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey/decapsulate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mlkem768/privatekey/decapsulate%28_%3A%29.json'
content_hash: 'sha256:289472ef219be577'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# decapsulate(_:)

<sub>Instance Method</sub>

Decapsulates the encapsulated shared secret

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

## Parameters

- `encapsulated` — The encapsulated shared secret

## Return Value

The decapsulated shared secret
