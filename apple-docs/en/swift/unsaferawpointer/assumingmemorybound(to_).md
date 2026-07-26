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
doc_path: '/documentation/swift/unsaferawpointer/assumingmemorybound(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/assumingmemorybound(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/assumingmemorybound%28to%3A%29.json'
content_hash: 'sha256:6c5a768bb5d60798'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# assumingMemoryBound(to:)

<sub>Instance Method</sub>

Returns a typed pointer to the memory referenced by this pointer, assuming that the memory is already bound to the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func assumingMemoryBound<T>(to: T.Type) -> UnsafePointer<T> where T : ~Copyable
```

## Parameters

- `to` — The type `T` that the memory has already been bound to.

## Return Value

A typed pointer to the same memory as this raw pointer.

## Discussion

Use this method when you have a raw pointer to memory that has _already_ been bound to the specified type. The memory starting at this pointer must be bound to the type `T`. Accessing memory through the returned pointer is undefined if the memory has not been bound to `T`. To bind memory to `T`, use `bindMemory(to:capacity:)` instead of this method.
