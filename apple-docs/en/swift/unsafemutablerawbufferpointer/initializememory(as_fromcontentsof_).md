---
title: 'initializeMemory(as:fromContentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/initializememory(as:fromcontentsof:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/initializememory(as:fromcontentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/initializememory%28as%3Afromcontentsof%3A%29.json'
content_hash: 'sha256:e3c323e34ecb04d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# initializeMemory(as:fromContentsOf:)

<sub>Instance Method</sub>

Initializes the buffer’s memory with every element of the source, binding the initialized memory to the elements’ type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initializeMemory<C>(as type: C.Element.Type, fromContentsOf source: C) -> UnsafeMutableBufferPointer<C.Element> where C : Collection
```

## Parameters

- `type` — The type of element to which this buffer’s memory will be bound.

- `source` — A collection of elements to be used to initialize the buffer’s storage.

## Return Value

A typed buffer referencing the initialized elements. The returned buffer references memory starting at the same base address as this buffer, and its count is equal to `source.count`

## Discussion

When calling the `initializeMemory(as:fromContentsOf:)` method, the memory referenced by the buffer must be uninitialized, or initialized to a trivial type. The buffer must reference enough memory to store `source.count` elements, and its `baseAddress` must be properly aligned for accessing `C.Element`.

This method initializes the buffer with the contents of `source` until `source` is exhausted. After calling `initializeMemory(as:fromContentsOf:)`, the memory referenced by the returned `UnsafeMutableBufferPointer` instance is bound to the type `C.Element` and is initialized. This method does not change the binding state of the unused portion of the buffer, if any.

> [!note] Note
> The memory regions referenced by `source` and this buffer must not overlap.
