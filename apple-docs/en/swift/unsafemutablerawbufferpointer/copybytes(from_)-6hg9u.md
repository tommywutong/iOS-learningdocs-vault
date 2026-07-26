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
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/copybytes(from:)-6hg9u'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/copybytes(from:)-6hg9u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/copybytes%28from%3A%29-6hg9u.json'
content_hash: 'sha256:e9f95e6354981d1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# copyBytes(from:)

<sub>Instance Method</sub>

Copies from a collection of `UInt8` into this buffer’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyBytes<C>(from source: C) where C : Collection, C.Element == UInt8
```

## Parameters

- `source` — A collection of `UInt8` elements. `source.count` must be less than or equal to this buffer’s `count`.

## Discussion

If the first `source.count` bytes of memory referenced by this buffer are bound to a type `T`, then `T` must be a trivial type, the underlying pointer must be properly aligned for accessing `T`, and `source.count` must be a multiple of `MemoryLayout<T>.stride`.

After calling `copyBytes(from:)`, the first `source.count` bytes of memory referenced by this buffer are initialized to raw bytes. If the memory is bound to type `T`, then it contains values of type `T`.
