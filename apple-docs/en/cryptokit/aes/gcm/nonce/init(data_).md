---
title: 'init(data:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/aes/gcm/nonce/init(data:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/nonce/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/nonce/init%28data%3A%29.json'
content_hash: 'sha256:c7f2a586c984c9bb'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [AES](../../../aes.md) · [GCM](../../gcm.md) · [Nonce](../nonce.md)

# init(data:)

<sub>Initializer</sub>

Creates a nonce from the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(data: D) throws where D : DataProtocol
```

## Parameters

- `data` — A data representation of the nonce. The initializer throws an error if the data has a length smaller than 12 bytes.

## Discussion

Unless your use case calls for a nonce with a specific value, use the [init()](<init().md>) method to instead create a random nonce.

## See Also

### Creating a nonce

- [init()](<init().md>) — Creates a new random nonce.
