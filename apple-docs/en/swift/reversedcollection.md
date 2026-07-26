---
title: ReversedCollection
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection.json'
content_hash: 'sha256:397ca994d43a64c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ReversedCollection

<sub>Structure</sub>

A collection that presents the elements of its base collection in reverse order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ReversedCollection<Base> where Base : BidirectionalCollection
```

## Overview

> [!note] Note
> This type is the result of `x.reversed()` where `x` is a collection having bidirectional indices.

The `reversed()` method is always lazy when applied to a collection with bidirectional indices, but does not implicitly confer laziness on algorithms applied to its result.  In other words, for ordinary collections `c` having bidirectional indices:

- `c.reversed()` does not create new storage
- `c.reversed().map(f)` maps eagerly and returns a new array
- `c.lazy.reversed().map(f)` maps lazily and returns a `LazyMapCollection`

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [LazySequenceProtocol](lazysequenceprotocol.md), [RandomAccessCollection](randomaccesscollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Instance Methods

- [reversed()](<reversedcollection/reversed().md>) — Reversing a reversed collection returns the original collection.

### Default Implementations

- [BidirectionalCollection Implementations](reversedcollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](reversedcollection/collection-implementations.md)
- [LazySequenceProtocol Implementations](reversedcollection/lazysequenceprotocol-implementations.md)
- [Sequence Implementations](reversedcollection/sequence-implementations.md)

## See Also

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
- [StrideTo](strideto.md) — A sequence of values formed by striding over a half-open interval.
- [StrideThrough](stridethrough.md) — A sequence of values formed by striding over a closed interval.
- [UnfoldSequence](unfoldsequence.md) — A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [Zip2Sequence](zip2sequence.md) — A sequence of pairs built out of two underlying sequences.
