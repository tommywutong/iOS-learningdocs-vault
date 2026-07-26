---
title: 'hash(bytes:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hashfunction/hash(bytes:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hashfunction/hash(bytes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hashfunction/hash%28bytes%3A%29.json'
content_hash: 'sha256:addf62a2af50bf76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HashFunction](../hashfunction.md)

# hash(bytes:)

<sub>Type Method</sub>

Computes a digest of a span of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func hash(bytes: RawSpan) -> Self.Digest
```

## Parameters

- `bytes` — The bytes to be hashed.

## Return Value

The computed digest.
