---
title: RandomAccessCollection
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/randomaccesscollection
source_url: 'https://developer.apple.com/documentation/swift/randomaccesscollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/randomaccesscollection.json'
content_hash: 'sha256:d0db16de7956d934'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RandomAccessCollection

<sub>Protocol</sub>

A collection that supports efficient random-access index traversal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RandomAccessCollection<Element> : BidirectionalCollection where Self.Indices : RandomAccessCollection, Self.SubSequence : RandomAccessCollection
```

## Overview

Random-access collections can move indices any distance and measure the distance between indices in O(1) time. Therefore, the fundamental difference between random-access and bidirectional collections is that operations that depend on index movement or distance measurement offer significantly improved efficiency. For example, a random-access collection’s `count` property is calculated in O(1) instead of requiring iteration of an entire collection.

## Conforming to the RandomAccessCollection Protocol

The `RandomAccessCollection` protocol adds further constraints on the associated `Indices` and `SubSequence` types, but otherwise imposes no additional requirements over the `BidirectionalCollection` protocol. However, in order to meet the complexity guarantees of a random-access collection, either the index for your custom type must conform to the `Strideable` protocol or you must implement the `index(_:offsetBy:)` and `distance(from:to:)` methods with O(1) efficiency.

## Relationships

- **Inherits From**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Sequence](sequence.md)

- **Conforming Types**: [AnyRandomAccessCollection](anyrandomaccesscollection.md), [AnyRegexOutput](anyregexoutput.md), [Array](array.md), [ArraySlice](arrayslice.md), [ClosedRange](closedrange.md), [CollectionOfOne](collectionofone.md), [ContiguousArray](contiguousarray.md), [DefaultIndices](defaultindices.md), [EmptyCollection](emptycollection.md), [EnumeratedSequence](enumeratedsequence.md), [Words](int/words-swift.struct.md), [Words](int16/words-swift.struct.md), [Words](int32/words-swift.struct.md), [Words](int64/words-swift.struct.md), [Words](int8/words-swift.struct.md), [KeyValuePairs](keyvaluepairs.md), [LazyMapSequence](lazymapsequence.md), [LazySequence](lazysequence.md), [Range](range.md), [Ranges](rangeset/ranges-swift.struct.md), [Repeated](repeated.md), [ReversedCollection](reversedcollection.md), [Slice](slice.md), [Words](uint/words-swift.struct.md), [Words](uint128/words-swift.struct.md), [Words](uint16/words-swift.struct.md), [Words](uint32/words-swift.struct.md), [Words](uint64/words-swift.struct.md), [Words](uint8/words-swift.struct.md), [UTF16View](unicode/scalar/utf16view.md), [UTF8View](unicode/scalar/utf8view.md), [UnsafeBufferPointer](unsafebufferpointer.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md), [UnsafeRawBufferPointer](unsaferawbufferpointer.md)

## Topics

### Associated Types

- [Element](randomaccesscollection/element.md) — A type representing the sequence’s elements.
- [Index](randomaccesscollection/index.md) — A type that represents a position in the collection.
- [Indices](randomaccesscollection/indices-swift.associatedtype.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [SubSequence](randomaccesscollection/subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

### Instance Properties

- [endIndex](randomaccesscollection/endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](randomaccesscollection/indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](randomaccesscollection/startindex.md) — The position of the first element in a nonempty collection.

### Instance Methods

- [distance(from:to:)](<randomaccesscollection/distance(from_to_).md>) — Returns the distance between two indices.
- [formIndex(after:)](<randomaccesscollection/formindex(after_).md>) — Replaces the given index with its successor.
- [formIndex(before:)](<randomaccesscollection/formindex(before_).md>) — Replaces the given index with its predecessor.
- [index(_:offsetBy:)](<randomaccesscollection/index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<randomaccesscollection/index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<randomaccesscollection/index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<randomaccesscollection/index(before_).md>) — Returns the position immediately before the given index.

### Subscripts

- [subscript(_:)](<randomaccesscollection/subscript(__)-2mluu.md>) — Accesses the element at the specified position.
- [subscript(_:)](<randomaccesscollection/subscript(__)-3fc50.md>) — Accesses a contiguous subrange of the collection’s elements.

## See Also

### Collection Traversal

- [BidirectionalCollection](bidirectionalcollection.md) — A collection that supports backward as well as forward traversal.
