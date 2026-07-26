---
title: 'init(size:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/symmetrickey/init(size:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickey/init(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickey/init%28size%3A%29.json'
content_hash: 'sha256:02f8128a3ebc5271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SymmetricKey](../symmetrickey.md)

# init(size:)

<sub>Initializer</sub>

Generates a new random key of the given size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(size: SymmetricKeySize)
```

## Parameters

- `size` — The size of the key to generate. You can use one of the standard sizes, like [bits256](../symmetrickeysize/bits256.md), or you can create a key of custom length by initializing a [SymmetricKeySize](../symmetrickeysize.md) instance with a non-standard value.

## See Also

### Creating a key

- [init(data:)](<init(data_).md>) — Creates a key from the given data.
