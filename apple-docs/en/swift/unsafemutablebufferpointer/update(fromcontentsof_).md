---
title: 'update(fromContentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/update(fromcontentsof:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/update(fromcontentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/update%28fromcontentsof%3A%29.json'
content_hash: 'sha256:1b459e1a7a212371'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# update(fromContentsOf:)

<sub>Instance Method</sub>

Updates the buffer’s initialized memory with every element of the source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update(fromContentsOf source: some Collection<Element>) -> UnsafeMutableBufferPointer<Element>.Index
```

## Parameters

- `source` — A collection of elements to be used to update the buffer’s contents.

## Return Value

An index one past the index of the last element updated.

## Discussion

Prior to calling the `update(fromContentsOf:)` method on a buffer, the first `source.count` elements of the buffer’s memory must be initialized, or the buffer’s `Element` type must be a trivial type. The buffer must reference enough initialized memory to accommodate `source.count` elements.

The returned index is one past the index of the last element updated. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer can hold, the returned index is equal to the buffer’s `endIndex`.

> [!note] Note
> The memory regions referenced by `source` and this buffer may overlap.

> [!info] Precondition
> `self.count` \>= `source.count`
