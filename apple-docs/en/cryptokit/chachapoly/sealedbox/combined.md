---
title: combined
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/chachapoly/sealedbox/combined
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/combined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly/sealedbox/combined.json'
content_hash: 'sha256:0d7454df011bbbc5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [ChaChaPoly](../../chachapoly.md) · [SealedBox](../sealedbox.md)

# combined

<sub>Instance Property</sub>

A combined element composed of the tag, the nonce, and the ciphertext.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let combined: Data
```

## Discussion

The data layout of the combined representation is: nonce, ciphertext, then tag.
