---
title: 'init(copying:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/symmetrickey/init(copying:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickey/init(copying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickey/init%28copying%3A%29.json'
content_hash: 'sha256:638bb4e4fd8670a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SymmetricKey](../symmetrickey.md)

# init(copying:)

<sub>Initializer</sub>

Creates a key from the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(copying bytes: RawSpan)
```

## Parameters

- `bytes` — The span of bytes from which to create the key.
