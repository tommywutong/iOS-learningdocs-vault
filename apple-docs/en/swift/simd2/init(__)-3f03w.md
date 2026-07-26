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
doc_path: '/documentation/swift/simd2/init(_:)-3f03w'
source_url: 'https://developer.apple.com/documentation/swift/simd2/init(_:)-3f03w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd2/init%28_%3A%29-3f03w.json'
content_hash: 'sha256:c9804e9dcd735d99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD2](../simd2.md)

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
