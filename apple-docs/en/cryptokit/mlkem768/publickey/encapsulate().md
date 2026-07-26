---
title: encapsulate()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mlkem768/publickey/encapsulate()
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/publickey/encapsulate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/publickey/encapsulate%28%29.json'
content_hash: 'sha256:e46c97176d661876'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM768](../../mlkem768.md) · [PublicKey](../publickey.md)

# encapsulate()

<sub>Instance Method</sub>

Generates and encapsulates a shared secret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encapsulate() throws -> KEM.EncapsulationResult
```

## Return Value

An encapsulated shared secret, that you decapsulate by calling [decapsulate(_:)](<../privatekey/decapsulate(__).md>) on the corresponding private key.
