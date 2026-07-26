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
doc_path: '/documentation/swift/slice/moveupdate(fromcontentsof:)-5i98g'
source_url: 'https://developer.apple.com/documentation/swift/slice/moveupdate(fromcontentsof:)-5i98g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/moveupdate%28fromcontentsof%3A%29-5i98g.json'
content_hash: 'sha256:584874fe2631fb51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# moveUpdate(fromContentsOf:)

<sub>Instance Method</sub>

Updates this buffer slice’s initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func moveUpdate<Element>(fromContentsOf source: UnsafeMutableBufferPointer<Element>) -> Slice<Base>.Index where Base == UnsafeMutableBufferPointer<Element>
```

## Parameters

- `source` — A buffer containing the values to move. The memory region underlying `source` must be initialized.

## Return Value

An index one past the index of the last element updated.

## Discussion

The region of memory starting at the beginning of this buffer slice and covering `source.count` instances of its `Element` type  must be initialized, or its `Element` type must be a trivial type. After calling `moveUpdate(fromContentsOf:)`, the region of memory underlying `source` is uninitialized. The buffer slice must reference enough initialized memory to accommodate `source.count` elements.

The returned index is one past the index of the last element updated. If `source` contains no elements, the returned index is equal to the buffer’s `startIndex`. If `source` contains as many elements as the buffer slice can hold, the returned index is equal to the slice’s `endIndex`.

> [!note] Note
> The memory regions referenced by `source` and this buffer slice must not overlap.

> [!info] Precondition
> `self.count` \>= `source.count`
