---
title: tag
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/chachapoly/sealedbox/tag
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/tag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly/sealedbox/tag.json'
content_hash: 'sha256:d57c113444152c9a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [ChaChaPoly](../../chachapoly.md) · [SealedBox](../sealedbox.md)

# tag

<sub>Instance Property</sub>

An authentication tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tag: Data { get }
```

## Discussion

The authentication tag has a length of 16 bytes.

## See Also

### Inspecting the component elements

- [nonce](nonce.md) — The nonce used to encrypt the data.
- [ciphertext](ciphertext.md) — The encrypted data.
