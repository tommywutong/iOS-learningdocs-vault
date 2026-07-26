---
title: 'copyMemory(from:byteCount:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/copymemory(from:bytecount:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/copymemory(from:bytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/copymemory%28from%3Abytecount%3A%29.json'
content_hash: 'sha256:2e25ac8e79bfbe86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# copyMemory(from:byteCount:)

<sub>Instance Method</sub>

Copies the specified number of bytes from the given raw pointer’s memory into this pointer’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyMemory(from source: UnsafeRawPointer, byteCount: Int)
```

## Parameters

- `source` — A pointer to the memory to copy bytes from. The memory in the region `source..<(source + byteCount)` must be initialized to a trivial type.

- `byteCount` — The number of bytes to copy. `byteCount` must not be negative.

## Discussion

If the `byteCount` bytes of memory referenced by this pointer are bound to a type `T`, then `T` must be a trivial type, this pointer and `source` must be properly aligned for accessing `T`, and `byteCount` must be a multiple of `MemoryLayout<T>.stride`.

The memory in the region `source..<(source + byteCount)` may overlap with the memory referenced by this pointer.

After calling `copyMemory(from:byteCount:)`, the `byteCount` bytes of memory referenced by this pointer are initialized to raw bytes. If the memory is bound to type `T`, then it contains values of type `T`.
