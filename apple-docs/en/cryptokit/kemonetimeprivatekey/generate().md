---
title: generate()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/cryptokit/kemonetimeprivatekey/generate()
source_url: 'https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey/generate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kemonetimeprivatekey/generate%28%29.json'
content_hash: 'sha256:bdf270d632683558'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEMOneTimePrivateKey](../kemonetimeprivatekey.md)

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
