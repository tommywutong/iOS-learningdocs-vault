---
title: Sequence Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection/sequence-implementations
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/sequence-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/sequence-implementations.json'
content_hash: 'sha256:ae5c0a7a2214e1c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Collections](../collections.md) · [Supporting Types](../supporting-types.md) · [ReversedCollection](../reversedcollection.md)

# Sequence Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [Iterator](iterator.md) — A type that provides the sequence’s iteration interface and encapsulates its iteration state.

### Instance Properties

- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

### Instance Methods

- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [compactMap(_:)](<compactmap(__)-2ra13.md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value indicating whether the sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [count(where:)](<count(where_).md>) — Returns the number of elements in the sequence that satisfy the given predicate.
- [elementsEqual(_:)](<elementsequal(__).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [filter(_:)](<filter(__)-9g9gk.md>) — Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [flatMap(_:)](<flatmap(__)-17mz1.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-9kclv.md>)
- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [joined()](<joined()-448f.md>) — Returns the elements of this sequence of sequences, concatenated.
- [joined(separator:)](<joined(separator_)-1ijrz.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [joined(separator:)](<joined(separator_)-xipx.md>) — Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this sequence.
- [map(_:)](<map(__)-6gkpm.md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in the sequence.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in the sequence.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_)-59vb5.md>) — Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [starts(with:)](<starts(with_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](<starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [withContiguousStorageIfAvailable(_:)](<withcontiguousstorageifavailable(__).md>) — Executes a closure on the sequence’s contiguous storage.

### Type Aliases

- [Element](element.md) — A type that represents a valid position in the collection.
