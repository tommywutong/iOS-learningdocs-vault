---
title: 'moveInitializeMemory(as:fromContentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/moveinitializememory(as:fromcontentsof:)-8gjm9'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/moveinitializememory(as:fromcontentsof:)-8gjm9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/moveinitializememory%28as%3Afromcontentsof%3A%29-8gjm9.json'
content_hash: 'sha256:31953b6fd807f4dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# moveInitializeMemory(as:fromContentsOf:)

<sub>Instance Method</sub>

Moves every element of an initialized source buffer slice into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func moveInitializeMemory<T>(as type: T.Type, fromContentsOf source: Slice<UnsafeMutableBufferPointer<T>>) -> UnsafeMutableBufferPointer<T>
```

## Parameters

- `type` — The type of element to which this buffer’s memory will be bound.

- `source` — A buffer referencing the values to copy. The memory region underlying `source` must be initialized.

## Return Value

A typed buffer referencing the initialized elements. The returned buffer references memory starting at the same base address as this buffer, and its count is equal to `source.count`.

## Discussion

When calling the `moveInitializeMemory(as:fromContentsOf:)` method, the memory referenced by the buffer must be uninitialized, or initialized to a trivial type. The buffer must reference enough memory to store `source.count` elements, and its `baseAddress` must be properly aligned for accessing `C.Element`. After the method returns, the memory referenced by the returned buffer is initialized and the memory region underlying `source` is uninitialized.

This method initializes the buffer with the contents of `source` until `source` is exhausted. After calling `initializeMemory(as:fromContentsOf:)`, the memory referenced by the returned `UnsafeMutableBufferPointer` instance is bound to the type `T` and is initialized. This method does not change the binding state of the unused portion of the buffer, if any.

> [!note] Note
> The memory regions referenced by `source` and this buffer may overlap.
