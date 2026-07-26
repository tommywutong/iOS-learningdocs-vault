---
title: 'assumingMemoryBound(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/assumingmemorybound(to:)-7a4sa'
source_url: 'https://developer.apple.com/documentation/swift/slice/assumingmemorybound(to:)-7a4sa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/assumingmemorybound%28to%3A%29-7a4sa.json'
content_hash: 'sha256:0f09c89f6a9c2566'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# assumingMemoryBound(to:)

<sub>Instance Method</sub>

Returns a typed buffer to the memory referenced by this buffer slice, assuming that the memory is already bound to the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assumingMemoryBound<T>(to type: T.Type) -> UnsafeBufferPointer<T> where T : ~Copyable
```

## Return Value

A typed pointer to the same memory as this raw pointer.

## Discussion

Use this method when you have a raw buffer to memory that has already been bound to the specified type. The memory starting at this pointer must be bound to the type `T`. Accessing memory through the returned pointer is undefined if the memory has not been bound to `T`. To bind memory to `T`, use `bindMemory(to:capacity:)` instead of this method.

> [!note] Note
> The buffer slice’s start address must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: base.baseAddress+startIndex) % MemoryLayout<T>.alignment` must equal zero.
