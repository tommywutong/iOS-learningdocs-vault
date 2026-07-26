---
title: 'extracting(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafebufferpointer/extracting(_:)-nivx'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/extracting(_:)-nivx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/extracting%28_%3A%29-nivx.json'
content_hash: 'sha256:fbea1e4adf03e00d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# extracting(_:)

<sub>Instance Method</sub>

Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(_ bounds: Range<Int>) -> UnsafeBufferPointer<Element>
```

## Parameters

- `bounds` — A valid range of indices within this buffer.

## Return Value

A new buffer pointer over the items at `bounds`.

## Discussion

The returned buffer’s first item is always at index 0; unlike buffer slices, extracted buffers do not generally share their indices with the original buffer pointer.

```swift
withUnsafeTemporaryAllocation(of: Int.self, capacity: 5) { buffer in
  buffer.initialize(repeating: 0)
  // buffer contains [0, 0, 0, 0, 0]
  let part = buffer.extracting(2 ..< 4)
  part[0] = 1
  part[1] = 2
  // buffer now contains [0, 0, 1, 2, 0]
}
```

When `Element` is copyable, the `extracting` operation is equivalent to slicing the buffer then rebasing the resulting buffer slice:

```swift
let a = buffer.extracting(i ..< j)
let b = UnsafeBufferPointer(rebasing: buffer[i ..< j])
// `a` and `b` are now holding the same buffer
```

However, unlike slicing, the `extracting` operation remains available even if `Element` happens to be noncopyable.
