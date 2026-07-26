---
title: 'update(data:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hmac/update(data:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/update(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/update%28data%3A%29.json'
content_hash: 'sha256:58c0937103522239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# update(data:)

<sub>Instance Method</sub>

Updates the message authentication code computation with a block of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func update<D>(data: D) where D : DataProtocol
```

## Parameters

- `data` — The data for which to compute the authentication code.

## See Also

### Creating an authentication code iteratively

- [init(key:)](<init(key_).md>) — Creates a message authentication code generator.
- [finalize()](<finalize().md>) — Finalizes the message authentication computation and returns the computed code.
