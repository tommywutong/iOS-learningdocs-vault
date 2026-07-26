---
title: nonce
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/chachapoly/sealedbox/nonce
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/nonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly/sealedbox/nonce.json'
content_hash: 'sha256:a631f0cdee34e9b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [ChaChaPoly](../../chachapoly.md) · [SealedBox](../sealedbox.md)

# nonce

<sub>Instance Property</sub>

The nonce used to encrypt the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nonce: ChaChaPoly.Nonce { get }
```

## See Also

### Inspecting the component elements

- [ciphertext](ciphertext.md) — The encrypted data.
- [tag](tag.md) — An authentication tag.
