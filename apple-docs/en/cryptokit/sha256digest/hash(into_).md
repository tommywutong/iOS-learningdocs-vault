---
title: 'hash(into:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/sha256digest/hash(into:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/sha256digest/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha256digest/hash%28into%3A%29.json'
content_hash: 'sha256:3674498ebd656219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SHA256Digest](../sha256digest.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of the digest by feeding them into the given hash function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hash function to use when combining the components of the digest.

## Discussion

This method is part of the digest’s conformance to Swift standard library’s [Hashable](../../swift/hashable.md) protocol, making it possible to compare digests. Don’t confuse that hashing with the cryptographically secure hashing that you use to create the digest in the first place by, for example, calling `SHA256/hash(data:)`.
