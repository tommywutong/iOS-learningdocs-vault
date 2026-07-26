---
title: 'init(key:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hmac/init(key:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/init(key:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/init%28key%3A%29.json'
content_hash: 'sha256:623327bfa13290b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# init(key:)

<sub>Initializer</sub>

Creates a message authentication code generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(key: SymmetricKey)
```

## Parameters

- `key` — The symmetric key used to secure the computation.

## See Also

### Creating an authentication code iteratively

- [update(data:)](<update(data_).md>) — Updates the message authentication code computation with a block of data.
- [finalize()](<finalize().md>) — Finalizes the message authentication computation and returns the computed code.
