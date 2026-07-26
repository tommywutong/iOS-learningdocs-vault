---
title: 'withContiguousStorageIfAvailable(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/withcontiguousstorageifavailable(_:)-7e6xh'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/withcontiguousstorageifavailable(_:)-7e6xh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/withcontiguousstorageifavailable%28_%3A%29-7e6xh.json'
content_hash: 'sha256:8195834fdc667011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# withContiguousStorageIfAvailable(_:)

<sub>Instance Method</sub>

Executes a closure on the sequence’s contiguous storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withContiguousStorageIfAvailable<R>(_ body: (UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?
```

## Parameters

- `body` — A closure that receives an `UnsafeBufferPointer` to the sequence’s contiguous storage.

## Return Value

The value returned from `body`, unless the sequence doesn’t support contiguous storage, in which case the method ignores `body` and returns `nil`.

## Discussion

This method calls `body(buffer)`, where `buffer` is a pointer to the collection’s contiguous storage. If the contiguous storage doesn’t exist, the collection creates it. If the collection doesn’t support an internal representation in a form of contiguous storage, the method doesn’t call `body` — it immediately returns `nil`.

The optimizer can often eliminate bounds- and uniqueness-checking within an algorithm. When that fails, however, invoking the same algorithm on the `buffer` argument may let you trade safety for speed.

Successive calls to this method may provide a different pointer on each call. Don’t store `buffer` outside of this method.

A `Collection` that provides its own implementation of this method must provide contiguous storage to its elements in the same order as they appear in the collection. This guarantees that it’s possible to generate contiguous mutable storage to any of its subsequences by slicing `buffer` with a range formed from the distances to the subsequence’s `startIndex` and `endIndex`, respectively.
