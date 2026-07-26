---
title: 'authenticationCode(for:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/hmac/authenticationcode(for:using:)-heea'
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/authenticationcode(for:using:)-heea'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/authenticationcode%28for%3Ausing%3A%29-heea.json'
content_hash: 'sha256:0ade522f57f65460'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# authenticationCode(for:using:)

<sub>Type Method</sub>

Computes a message authentication code for the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func authenticationCode(for data: RawSpan, using key: SymmetricKey) -> HMAC<H>.MAC
```

## Parameters

- `data` — The data for which to compute the authentication code.

- `key` — The symmetric key used to secure the computation.

## Return Value

The message authentication code.
