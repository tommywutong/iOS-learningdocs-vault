---
title: Array.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/subsequence
source_url: 'https://developer.apple.com/documentation/swift/array/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/subsequence.json'
content_hash: 'sha256:c3a22f4ae90345ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# Array.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = ArraySlice<Element>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

## See Also

### Supporting Types

- [Index](index.md) — The index type for arrays, `Int`.
- [Indices](indices.md) — The type that represents the indices that are valid for subscripting an array, in ascending order.
- [Iterator](iterator.md) — The type that allows iteration over an array’s elements.
- [ArrayLiteralElement](arrayliteralelement.md) — The type of the elements of an array literal.
