---
title: 'hash(data:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hashfunction/hash(data:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hashfunction/hash(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hashfunction/hash%28data%3A%29.json'
content_hash: 'sha256:b2b22f4115465b18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HashFunction](../hashfunction.md)

# hash(data:)

<sub>Type Method</sub>

Computes the digest of the bytes in the given data instance and returns the computed digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func hash<D>(data: D) -> Self.Digest where D : DataProtocol
```

## Parameters

- `data` — The data whose digest the hash function should compute. This can be any type that conforms to [DataProtocol](../../foundation/dataprotocol.md), like [Data](../../foundation/data.md) or an array of [UInt8](../../swift/uint8.md) instances.

## Return Value

The computed digest of the data.

## Discussion

Use this method if all your data fits into a single data instance. If the data you want to hash is too large, initialize a hash function and use the [update(data:)](<update(data_).md>) and [finalize()](<finalize().md>) methods to compute the digest in blocks.
