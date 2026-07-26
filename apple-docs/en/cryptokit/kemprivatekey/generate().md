---
title: generate()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kemprivatekey/generate()
source_url: 'https://developer.apple.com/documentation/cryptokit/kemprivatekey/generate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kemprivatekey/generate%28%29.json'
content_hash: 'sha256:ee8ee1f1c34d268e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEMPrivateKey](../kemprivatekey.md)

# generate()

<sub>Type Method</sub>

Generates a new random private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func generate() throws -> Self
```

## Return Value

The generated private key.

## Discussion

Give the [publicKey](publickey-swift.property.md) to another person so that they can encapsulate shared secrets that you recover by calling [decapsulate(_:)](<decapsulate(__).md>).
