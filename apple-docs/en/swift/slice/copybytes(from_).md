---
title: 'copyBytes(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/copybytes(from:)'
source_url: 'https://developer.apple.com/documentation/swift/slice/copybytes(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/copybytes%28from%3A%29.json'
content_hash: 'sha256:1a664f48cb7c76d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# copyBytes(from:)

<sub>Instance Method</sub>

Copies from a collection of `UInt8` into this buffer slice’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyBytes<C>(from source: C) where C : Collection, C.Element == UInt8
```

## Parameters

- `source` — A collection of `UInt8` elements. `source.count` must be less than or equal to this buffer slice’s `count`.

## Discussion

If the first `source.count` bytes of memory referenced by this buffer slice are bound to a type `T`, then `T` must be a trivial type, the underlying pointer must be properly aligned for accessing `T`, and `source.count` must be a multiple of `MemoryLayout<T>.stride`.

After calling `copyBytes(from:)`, the first `source.count` bytes of memory referenced by this buffer slice are initialized to raw bytes. If the memory is bound to type `T`, then it contains values of type `T`.
