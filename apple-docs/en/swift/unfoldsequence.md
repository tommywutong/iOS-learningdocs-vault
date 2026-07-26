---
title: UnfoldSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unfoldsequence
source_url: 'https://developer.apple.com/documentation/swift/unfoldsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unfoldsequence.json'
content_hash: 'sha256:8ee0ad1000f7a087'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnfoldSequence

<sub>Structure</sub>

A sequence whose elements are produced via repeated applications of a closure to some mutable state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnfoldSequence<Element, State>
```

## Overview

The elements of the sequence are computed lazily and the sequence may potentially be infinite in length.

Instances of `UnfoldSequence` are created with the functions `sequence(first:next:)` and `sequence(state:next:)`.

## Relationships

- **Conforms To**: [IteratorProtocol](iteratorprotocol.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Type Aliases

- [UnfoldFirstSequence](unfoldfirstsequence.md) — The return type of `sequence(first:next:)`.
- [Iterator](unfoldsequence/iterator.md) — A type that provides the sequence’s iteration interface and encapsulates its iteration state.

### Instance Methods

- [next()](<unfoldsequence/next().md>) — Advances to the next element and returns it, or `nil` if no next element exists.

### Default Implementations

- [Sequence Implementations](unfoldsequence/sequence-implementations.md)

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
- [ReversedCollection](reversedcollection.md) — A collection that presents the elements of its base collection in reverse order.
- [StrideTo](strideto.md) — A sequence of values formed by striding over a half-open interval.
- [StrideThrough](stridethrough.md) — A sequence of values formed by striding over a closed interval.
- [Zip2Sequence](zip2sequence.md) — A sequence of pairs built out of two underlying sequences.
