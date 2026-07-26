---
title: MutableCollection
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mutablecollection
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection.json'
content_hash: 'sha256:25edd085f4f48a10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MutableCollection

<sub>Protocol</sub>

A collection that supports subscript assignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MutableCollection<Element> : Collection where Self.SubSequence : MutableCollection
```

## Overview

Collections that conform to `MutableCollection` gain the ability to change the value of their elements. This example shows how you can modify one of the names in an array of students.

```swift
var students = ["Ben", "Ivy", "Jordell", "Maxime"]
if let i = students.firstIndex(of: "Maxime") {
    students[i] = "Max"
}
print(students)
// Prints "["Ben", "Ivy", "Jordell", "Max"]"
```

In addition to changing the value of an individual element, you can also change the values of a slice of elements in a mutable collection. For example, you can sort _part_ of a mutable collection by calling the mutable `sort()` method on a subscripted subsequence. Here’s an example that sorts the first half of an array of integers:

```swift
var numbers = [15, 40, 10, 30, 60, 25, 5, 100]
numbers[0..<4].sort()
print(numbers)
// Prints "[10, 15, 30, 40, 60, 25, 5, 100]"
```

The `MutableCollection` protocol allows changing the values of a collection’s elements but not the length of the collection itself. For operations that require adding or removing elements, see the `RangeReplaceableCollection` protocol instead.

## Conforming to the MutableCollection Protocol

To add conformance to the `MutableCollection` protocol to your own custom collection, upgrade your type’s subscript to support both read and write access.

A value stored into a subscript of a `MutableCollection` instance must subsequently be accessible at that same position. That is, for a mutable collection instance `a`, index `i`, and value `x`, the two sets of assignments in the following code sample must be equivalent:

```swift
a[i] = x
let y = a[i]

// Must be equivalent to:
a[i] = x
let y = x
```

## Relationships

- **Inherits From**: [Collection](collection.md), [Sequence](sequence.md)

- **Conforming Types**: [Array](array.md), [ArraySlice](arrayslice.md), [CollectionOfOne](collectionofone.md), [ContiguousArray](contiguousarray.md), [Values](dictionary/values-swift.struct.md), [EmptyCollection](emptycollection.md), [Slice](slice.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)

## Topics

### Associated Types

- [Element](mutablecollection/element.md) — A type representing the sequence’s elements.
- [Index](mutablecollection/index.md) — A type that represents a position in the collection.
- [SubSequence](mutablecollection/subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

### Instance Methods

- [move(fromOffsets:toOffset:)](<mutablecollection/move(fromoffsets_tooffset_).md>) — Moves all the elements at the specified offsets to the specified destination offset, preserving ordering.
- [moveSubranges(_:to:)](<mutablecollection/movesubranges(__to_).md>) — Moves the elements in the given subranges to just before the element at the specified index.
- [partition(by:)](<mutablecollection/partition(by_).md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [removeSubranges(_:)](<mutablecollection/removesubranges(__).md>) — Removes the elements at the given indices.
- [reverse()](<mutablecollection/reverse().md>) — Reverses the elements of the collection in place.
- [shuffle()](<mutablecollection/shuffle().md>) — Shuffles the collection in place.
- [shuffle(using:)](<mutablecollection/shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [sort()](<mutablecollection/sort().md>) — Sorts the collection in place.
- [sort(by:)](<mutablecollection/sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [sort(using:)](<mutablecollection/sort(using_)-694fo.md>) — Sorts the collection using the given comparator to compare elements.
- [sort(using:)](<mutablecollection/sort(using_)-9a05g.md>) — Sorts the collection using the given array of `SortComparator`s to compare elements.
- [swapAt(_:_:)](<mutablecollection/swapat(____).md>) — Exchanges the values at the specified indices of the collection.
- [withContiguousMutableStorageIfAvailable(_:)](<mutablecollection/withcontiguousmutablestorageifavailable(__).md>) — Executes a closure on the collection’s contiguous storage.

### Subscripts

- [subscript(_:)](<mutablecollection/subscript(__)-31dgt.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<mutablecollection/subscript(__)-7tq68.md>) — Accesses the element at the specified position.

## See Also

### Collection Mutability

- [RangeReplaceableCollection](rangereplaceablecollection.md) — A collection that supports replacement of an arbitrary subrange of elements with the elements of another collection.
