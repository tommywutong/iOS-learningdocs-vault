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
doc_path: '/documentation/swift/unsaferawbufferpointer/assumingmemorybound(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/assumingmemorybound(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/assumingmemorybound%28to%3A%29.json'
content_hash: 'sha256:9d36a9278234f3e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# assumingMemoryBound(to:)

<sub>Instance Method</sub>

Returns a typed buffer to the memory referenced by this buffer, assuming that the memory is already bound to the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assumingMemoryBound<T>(to: T.Type) -> UnsafeBufferPointer<T> where T : ~Copyable
```

## Parameters

- `to` — The type `T` that the memory has already been bound to.

## Return Value

A typed pointer to the same memory as this raw pointer.

## Discussion

Use this method when you have a raw buffer to memory that has already been bound to the specified type. The memory starting at this pointer must be bound to the type `T`. Accessing memory through the returned pointer is undefined if the memory has not been bound to `T`. To bind memory to `T`, use `bindMemory(to:capacity:)` instead of this method.

> [!note] Note
> The buffer’s base address must match the alignment of `T` (as reported by `MemoryLayout<T>.alignment`). That is, `Int(bitPattern: self.baseAddress) % MemoryLayout<T>.alignment` must equal zero.
