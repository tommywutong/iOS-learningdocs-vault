---
title: 'init(data:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/symmetrickey/init(data:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickey/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickey/init%28data%3A%29.json'
content_hash: 'sha256:40bccc16f458a556'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SymmetricKey](../symmetrickey.md)

# init(data:)

<sub>Initializer</sub>

Creates a key from the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(data: D) where D : ContiguousBytes
```

## Parameters

- `data` — The contiguous bytes from which to create the key.

## See Also

### Creating a key

- [init(size:)](<init(size_).md>) — Generates a new random key of the given size.
