---
title: PrefixSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/prefixsequence
source_url: 'https://developer.apple.com/documentation/swift/prefixsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/prefixsequence.json'
content_hash: 'sha256:4f51f0fadcb92bd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# PrefixSequence

<sub>Structure</sub>

A sequence that only consumes up to `n` elements from an underlying `Base` iterator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct PrefixSequence<Base> where Base : Sequence
```

## Overview

The underlying iterator’s sequence may be infinite.

## Relationships

- **Conforms To**: [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:maxLength:)](<prefixsequence/init(__maxlength_).md>)

### Instance Methods

- [prefix(_:)](<prefixsequence/prefix(__).md>)

### Default Implementations

- [Sequence Implementations](prefixsequence/sequence-implementations.md)

## See Also

### Wrappers for Algorithms

- [CollectionDifference](collectiondifference.md) — A collection of insertions and removals that describe the difference between two ordered collection states.
- [DropFirstSequence](dropfirstsequence.md) — A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [DropWhileSequence](dropwhilesequence.md) — A sequence that lazily consumes and drops `n` elements from an underlying `Base` iterator before possibly returning the first available element.
- [EnumeratedSequence](enumeratedsequence.md) — An enumeration of the elements of a sequence or collection.
- [FlattenCollection](flattencollection.md)
- [FlattenSequence](flattensequence.md) — A sequence consisting of all the elements contained in each segment contained in some `Base` sequence.
- [JoinedSequence](joinedsequence.md) — A sequence that presents the elements of a base sequence of sequences concatenated using a given separator.
- [Repeated](repeated.md) — A collection whose elements are all identical.
- [ReversedCollection](reversedcollection.md) — A collection that presents the elements of its base collection in reverse order.
- [StrideTo](strideto.md) — A sequence of values formed by striding over a half-open interval.
- [StrideThrough](stridethrough.md) — A sequence of values formed by striding over a closed interval.
- [UnfoldSequence](unfoldsequence.md) — A sequence whose elements are produced via repeated applications of a closure to some mutable state.
- [Zip2Sequence](zip2sequence.md) — A sequence of pairs built out of two underlying sequences.
