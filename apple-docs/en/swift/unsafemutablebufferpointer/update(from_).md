---
title: 'update(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/update(from:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/update(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/update%28from%3A%29.json'
content_hash: 'sha256:e30988b89ad015e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# update(from:)

<sub>Instance Method</sub>

Updates the buffer’s initialized memory with the given elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update<S>(from source: S) -> (unwritten: S.Iterator, index: UnsafeMutableBufferPointer<Element>.Index) where Element == S.Element, S : Sequence
```

## Parameters

- `source` — A sequence of elements to be used to update the buffer’s contents.

## Return Value

An iterator to any elements of `source` that didn’t fit in the buffer, and the index one past the last updated element in the buffer.

## Discussion

The buffer’s memory must be initialized or its `Element` type must be a trivial type.
