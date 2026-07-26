---
title: 'moveUpdate(fromContentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/moveupdate(fromcontentsof:)-4bpe7'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/moveupdate(fromcontentsof:)-4bpe7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/moveupdate%28fromcontentsof%3A%29-4bpe7.json'
content_hash: 'sha256:4fe8c93952beabcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# moveUpdate(fromContentsOf:)

<sub>Instance Method</sub>

Updates this buffer’s initialized memory initialized memory by moving every element from the source buffer slice, leaving the source memory uninitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func moveUpdate(fromContentsOf source: Slice<UnsafeMutableBufferPointer<Element>>) -> UnsafeMutableBufferPointer<Element>.Index
```

## Parameters

- `source` — A buffer slice containing the values to move. The memory region underlying `source` must be initialized.

## Return Value

An index one past the index of the last element updated.

## Discussion

Prior to calling the `moveUpdate(fromContentsOf:)` method on a buffer, the first `source.count` elements of the buffer’s memory must be initialized, or the buffer’s `Element` type must be a trivial type. The memory referenced by `source` is uninitialized after the function returns. The buffer must reference enough initialized memory to accommodate `source.count` elements.

The returned index is one past the index of the last element updated. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer can hold, the returned index is equal to the buffer’s `endIndex`.

> [!note] Note
> The memory regions referenced by `source` and this buffer must not overlap.

> [!info] Precondition
> `self.count` \>= `source.count`
