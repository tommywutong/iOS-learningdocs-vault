---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd32/init(_:)-6afuc'
source_url: 'https://developer.apple.com/documentation/swift/simd32/init(_:)-6afuc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd32/init%28_%3A%29-6afuc.json'
content_hash: 'sha256:989a9084611a73db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD32](../simd32.md)

# init(_:)

<sub>Initializer</sub>

Creates a vector from the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ scalars: S) where S : Sequence, Self.Scalar == S.Element
```

## Parameters

- `scalars` — The elements to use in the vector.

## Discussion

> [!info] Precondition
> `scalars` must have the same number of elements as the vector type.
