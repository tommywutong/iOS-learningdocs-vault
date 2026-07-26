---
title: finalize()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hmac/finalize()
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/finalize%28%29.json'
content_hash: 'sha256:163b1f4d311e9437'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# finalize()

<sub>Instance Method</sub>

Finalizes the message authentication computation and returns the computed code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize() -> HMAC<H>.MAC
```

## Return Value

The message authentication code.

## See Also

### Creating an authentication code iteratively

- [init(key:)](<init(key_).md>) — Creates a message authentication code generator.
- [update(data:)](<update(data_).md>) — Updates the message authentication code computation with a block of data.
