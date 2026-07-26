---
title: 'authenticationCode(for:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hmac/authenticationcode(for:using:)-737ab'
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/authenticationcode(for:using:)-737ab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/authenticationcode%28for%3Ausing%3A%29-737ab.json'
content_hash: 'sha256:e812868e9b0ef0c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# authenticationCode(for:using:)

<sub>Type Method</sub>

Computes a message authentication code for the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func authenticationCode<D>(for data: D, using key: SymmetricKey) -> HMAC<H>.MAC where D : DataProtocol
```

## Parameters

- `data` — The data for which to compute the authentication code.

- `key` — The symmetric key used to secure the computation.

## Return Value

The message authentication code.
