---
title: Supporting Types
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/supporting-types
source_url: 'https://developer.apple.com/documentation/swift/supporting-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/supporting-types.json'
content_hash: 'sha256:0cf9790e18d0c612'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Collections](collections.md)

# Supporting Types

<sub>API Collection</sub>

Use wrappers, indices, and iterators in operations like slicing, flattening, and reversing a collection.

## Topics

### Slices

- [Slice](slice.md) — A view into a subsequence of elements of another collection.

### Range Expressions

- [PartialRangeUpTo](partialrangeupto.md) — A partial half-open interval up to, but not including, an upper bound.
- [PartialRangeThrough](partialrangethrough.md) — A partial interval up to, and including, an upper bound.
- [PartialRangeFrom](partialrangefrom.md) — A partial interval extending upward from a lower bound.
- [RangeExpression](rangeexpression.md) — A type that can be used to slice a collection.
- [UnboundedRange_](unboundedrange_.md) — A range expression that represents the entire range of a collection.

### Type-Erasing Wrappers

- [AnySequence](anysequence.md) — A type-erased sequence.
- [AnyCollection](anycollection.md) — A type-erased wrapper over any collection with indices that support forward traversal.
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — A type-erased wrapper over any collection with indices that support random access traversal.
- [AnyIterator](anyiterator.md) — A type-erased iterator of `Element`.
- [AnyIndex](anyindex.md) — A wrapper over an underlying index that hides the specific underlying type.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.

### Lazy Wrappers

- [LazySequence](lazysequence.md) — A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyMapSequence](lazymapsequence.md) — A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyFilterSequence](lazyfiltersequence.md) — A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md) — A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyDropWhileSequence](lazydropwhilesequence.md) — A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyCollection](lazycollection.md) — A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyDropWhileCollection](lazydropwhilecollection.md) — A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.
- [LazyFilterCollection](lazyfiltercollection.md) — A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [LazyMapCollection](lazymapcollection.md) — A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyPrefixWhileCollection](lazyprefixwhilecollection.md) — A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.

### Wrappers for Algorithms

- [CollectionDifference](collectiondifference.md) — A collection of insertions and removals that describe the difference between two ordered collection states.
- [DropFirstSequence](dropfirstsequence.md) — A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [DropWhileSequence](dropwhilesequence.md) — A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [EnumeratedSequence](enumeratedsequence.md) — An enumeration of the elements of a sequence or collection.
- [FlattenCollection](flattencollection.md)
- [FlattenSequence](flattensequence.md) — A sequence consisting of all the elements contained in each segment contained in some `Base` sequence.
- [JoinedSequence](joinedsequence.md) — A sequence that presents the elements of a base sequence of sequences concatenated using a given separator.
- [PrefixSequence](prefixsequence.md) — A sequence that only consumes up to `n` elements from an underlying `Base` iterator.
- [Repeated](repeated.md) — A collection whose elements are all identical.
- [ReversedCollection](reversedcollection.md) — A collection that presents the elements of its base collection in reverse order.
- [StrideTo](strideto.md) — A sequence of values formed by striding over a half-open interval.
- [StrideThrough](stridethrough.md) — A sequence of values formed by striding over a closed interval.
- [UnfoldSequence](unfoldsequence.md) — A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [Zip2Sequence](zip2sequence.md) — A sequence of pairs built out of two underlying sequences.

### Collections of Indices

- [DefaultIndices](defaultindices.md) — A collection of indices for an arbitrary collection

### Indices and Iterators

- [IteratorSequence](iteratorsequence.md) — A sequence built around an iterator of type `Base`.
- [IndexingIterator](indexingiterator.md) — A type that iterates over a collection using its indices.
- [EnumeratedIterator](enumeratediterator.md)
- [SetIterator](setiterator.md)
- [StrideThroughIterator](stridethroughiterator.md) — An iterator for a `StrideThrough` instance.
- [StrideToIterator](stridetoiterator.md) — An iterator for a `StrideTo` instance.

### Deprecated

- [DictionaryIndex](dictionaryindex.md)
- [SetIndex](setindex.md)
- [CountableClosedRange](countableclosedrange.md)
- [CountablePartialRangeFrom](countablepartialrangefrom.md)
- [CountableRange](countablerange.md)

## See Also

### Advanced Collection Topics

- [Sequence and Collection Protocols](sequence-and-collection-protocols.md) — Write generic code that works with any collection, or build your own collection types.
- [Managed Buffers](managed-buffers.md) — Build your own buffer-backed collection types.
