---
title: 'initialize(fromContentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/initialize(fromcontentsof:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/initialize(fromcontentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/initialize%28fromcontentsof%3A%29.json'
content_hash: 'sha256:4c7a3178076fa565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# initialize(fromContentsOf:)

<sub>Instance Method</sub>

Initializes the buffer’s memory with every element of the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize(fromContentsOf source: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index
```

## Parameters

- `source` — A collection of elements to be used to initialize the buffer’s storage.

## Return Value

The index one past the last element of the buffer initialized by this function.

## Discussion

Prior to calling the `initialize(fromContentsOf:)` method on a buffer, the memory referenced by the buffer must be uninitialized, or the `Element` type must be a trivial type. After the call, the memory referenced by the buffer up to, but not including, the returned index is initialized. The buffer must reference enough memory to accommodate `source.count` elements.

The returned index is the position of the next uninitialized element in the buffer, one past the index of the last element written. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer can hold, the returned index is equal to the buffer’s `endIndex`.

> [!info] Precondition
> `self.count` \>= `source.count`

> [!note] Note
> The memory regions referenced by `source` and this buffer must not overlap.
