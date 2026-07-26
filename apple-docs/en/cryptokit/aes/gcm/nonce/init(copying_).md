---
title: 'init(copying:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/aes/gcm/nonce/init(copying:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/nonce/init(copying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/nonce/init%28copying%3A%29.json'
content_hash: 'sha256:58c36676d228fe11'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [AES](../../../aes.md) · [GCM](../../gcm.md) · [Nonce](../nonce.md)

# init(copying:)

<sub>Initializer</sub>

Creates a nonce from the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(copying bytes: RawSpan) throws
```

## Parameters

- `bytes` — The bytes that represent the nonce. The initializer throws an error if the data has a length smaller than 12 bytes.

## Discussion

Unless your use case calls for a nonce with a specific value, use the [init()](<init().md>) method to instead create a random nonce.
