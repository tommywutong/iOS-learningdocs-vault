---
title: 'copyMemory(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/copymemory(from:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/copymemory(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/copymemory%28from%3A%29.json'
content_hash: 'sha256:ad40d24489395b4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# copyMemory(from:)

<sub>Instance Method</sub>

Copies the bytes from the given buffer to this buffer’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyMemory(from source: UnsafeRawBufferPointer)
```

## Parameters

- `source` — A buffer of raw bytes. `source.count` must be less than or equal to this buffer’s `count`.

## Discussion

If the `source.count` bytes of memory referenced by this buffer are bound to a type `T`, then `T` must be a trivial type, the underlying pointer must be properly aligned for accessing `T`, and `source.count` must be a multiple of `MemoryLayout<T>.stride`.

The memory referenced by `source` may overlap with the memory referenced by this buffer.

After calling `copyMemory(from:)`, the first `source.count` bytes of memory referenced by this buffer are initialized to raw bytes. If the memory is bound to type `T`, then it contains values of type `T`.
