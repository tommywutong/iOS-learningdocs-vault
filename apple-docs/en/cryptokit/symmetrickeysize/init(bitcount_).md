---
title: 'init(bitCount:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/symmetrickeysize/init(bitcount:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickeysize/init(bitcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickeysize/init%28bitcount%3A%29.json'
content_hash: 'sha256:856c9a2ab506aee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SymmetricKeySize](../symmetrickeysize.md)

# init(bitCount:)

<sub>Initializer</sub>

Creates a new key size of the given length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitCount: Int)
```

## Parameters

- `bitCount` — The number of bits in the key size.

## Discussion

In most cases, you can use one of the standard key sizes, like bits256. If instead you need a key with a non-standard size, use the [init(bitCount:)](<init(bitcount_).md>) initializer to create a custom key size.
