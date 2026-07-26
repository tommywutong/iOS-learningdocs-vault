---
title: Collection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazymapsequence/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/collection-implementations.json'
content_hash: 'sha256:63972d8926f143e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [LazyMapSequence](../lazymapsequence.md)

# Collection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [count](count.md) — The number of elements in the collection.
- [count](count-5qqod.md) — The number of elements in the collection.
- [endIndex](endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [isEmpty](isempty.md) — A Boolean value indicating whether the collection is empty.
- [isEmpty](isempty-75pes.md) — A Boolean value indicating whether the collection is empty.
- [startIndex](startindex.md) — The position of the first element in a nonempty collection.

### Instance Methods

- [distance(from:to:)](<distance(from_to_).md>) — Returns the distance between two indices.
- [distance(from:to:)](<distance(from_to_)-3i820.md>) — Returns the distance between two indices.
- [firstIndex(of:)](<firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [formIndex(_:offsetBy:)](<formindex(__offsetby_).md>) — Offsets the given index by the specified distance.
- [formIndex(_:offsetBy:limitedBy:)](<formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [formIndex(after:)](<formindex(after_).md>) — Replaces the given index with its successor.
- [formIndex(after:)](<formindex(after_)-6932e.md>) — Replaces the given index with its successor.
- [index(_:offsetBy:)](<index(__offsetby_).md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:)](<index(__offsetby_)-78pdz.md>) — Returns an index that is the specified distance from the given index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_).md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(_:offsetBy:limitedBy:)](<index(__offsetby_limitedby_)-5uiel.md>) — Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [index(after:)](<index(after_).md>) — Returns the position immediately after the given index.
- [index(of:)](<index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [indices(of:)](<indices(of_).md>) — Returns the indices of all the elements that are equal to the given element.
- [indices(where:)](<indices(where_).md>) — Returns the indices of all the elements that match the given predicate.
- [map(_:)](<map(__)-8qb3x.md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
- [removingSubranges(_:)](<removingsubranges(__).md>) — Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-5eafc.md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](<subscript(__)-36b2w.md>) — Accesses the element at `position`.
- [subscript(_:)](<subscript(__)-3hxz5.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-4qmx0.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-4tv8v.md>) — Accesses a view of this collection with the elements at the given indices.
- [subscript(_:)](<subscript(__)-88114.md>)

### Type Aliases

- [Index](index.md) — A type that represents a position in the collection.
- [Indices](indices-swift.typealias.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [SubSequence](subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
