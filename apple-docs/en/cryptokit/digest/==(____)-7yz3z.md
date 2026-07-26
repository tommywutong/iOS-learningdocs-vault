---
title: '==(_:_:)'
framework: Apple CryptoKit
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/digest/==(_:_:)-7yz3z'
source_url: 'https://developer.apple.com/documentation/cryptokit/digest/==(_:_:)-7yz3z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/digest/%3D%3D%28_%3A_%3A%29-7yz3z.json'
content_hash: 'sha256:7bf558ac961ad560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [Digest](../digest.md)

# ==(_:_:)

<sub>Operator</sub>

Determines whether a digest is equivalent to a collection of contiguous bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == <D>(lhs: Self, rhs: D) -> Bool where D : DataProtocol
```

## Parameters

- `lhs` — A digest to compare.

- `rhs` — A collection of contiguous bytes to compare.

## Return Value

A Boolean value that’s `true` if the digest is equivalent to the collection of binary data.

## See Also

### Comparing digests

- [==(_:_:)](<==(____)-6m59k.md>) — Determines whether two digests are equal.
