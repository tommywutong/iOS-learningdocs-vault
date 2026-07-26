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
doc_path: '/documentation/swift/slice/update(from:)'
source_url: 'https://developer.apple.com/documentation/swift/slice/update(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/update%28from%3A%29.json'
content_hash: 'sha256:15654cbe5891d0b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# update(from:)

<sub>Instance Method</sub>

Updates the buffer slice’s initialized memory with the given elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update<S>(from source: S) -> (unwritten: S.Iterator, index: Slice<Base>.Index) where Base == UnsafeMutableBufferPointer<S.Element>, S : Sequence
```

## Parameters

- `source` — A sequence of elements to be used to update the contents of the buffer slice.

## Return Value

An iterator to any elements of `source` that didn’t fit in the buffer slice, and the index one past the last updated element.

## Discussion

The buffer slice’s memory must be initialized or its `Element` type must be a trivial type.
