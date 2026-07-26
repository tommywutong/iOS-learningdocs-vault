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
doc_path: /documentation/swift/anybidirectionalcollection/collection-implementations
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/collection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/collection-implementations.json'
content_hash: 'sha256:de0bea19e073c946'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# Collection Implementations

<sub>API Collection</sub>

## Topics

### Instance Properties

- [count](count.md) — The number of elements.
- [first](first.md) — The first element of the collection.
- [indices](indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [isEmpty](isempty.md) — A Boolean value indicating whether the collection is empty.

### Instance Methods

- [firstIndex(of:)](<firstindex(of_).md>) — Returns the first index where the specified value appears in the collection.
- [firstIndex(where:)](<firstindex(where_).md>) — Returns the first index in which an element of the collection satisfies the given predicate.
- [index(of:)](<index(of_).md>) — Returns the first index where the specified value appears in the collection.
- [indices(of:)](<indices(of_).md>) — Returns the indices of all the elements that are equal to the given element.
- [indices(where:)](<indices(where_).md>) — Returns the indices of all the elements that match the given predicate.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this collection.
- [map(_:)](<map(__)-4xfvs.md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [popFirst()](<popfirst().md>) — Removes and returns the first element of the collection.
- [prefix(through:)](<prefix(through_).md>) — Returns a subsequence from the start of the collection through the specified position.
- [prefix(upTo:)](<prefix(upto_).md>) — Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
- [removeFirst()](<removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removingSubranges(_:)](<removingsubranges(__).md>) — Returns a collection of the elements in this collection that are not represented by the given range set.
- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-5dxmc.md>) — Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [suffix(from:)](<suffix(from_).md>) — Returns a subsequence from the specified position to the end of the collection.

### Subscripts

- [subscript(_:)](<subscript(__)-34ify.md>)
- [subscript(_:)](<subscript(__)-8f134.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-93ijp.md>) — Accesses a view of this collection with the elements at the given indices.

### Type Aliases

- [Index](index.md) — A type that represents a position in the collection.
- [Indices](indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Iterator](iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [SubSequence](subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
