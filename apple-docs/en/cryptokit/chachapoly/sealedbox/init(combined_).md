---
title: 'init(combined:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/chachapoly/sealedbox/init(combined:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox/init(combined:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly/sealedbox/init%28combined%3A%29.json'
content_hash: 'sha256:43bb4bdab5117052'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [ChaChaPoly](../../chachapoly.md) · [SealedBox](../sealedbox.md)

# init(combined:)

<sub>Initializer</sub>

Creates a sealed box from the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(combined: D) throws where D : DataProtocol
```

## Parameters

- `combined` — The combined bytes of the tag and ciphertext.

## See Also

### Creating the sealed box

- [init(nonce:ciphertext:tag:)](<init(nonce_ciphertext_tag_).md>) — Creates a sealed box from the given tag, nonce, and ciphertext.
