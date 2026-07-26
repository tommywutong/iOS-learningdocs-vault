---
title: LazySequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequence
source_url: 'https://developer.apple.com/documentation/swift/lazysequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence.json'
content_hash: 'sha256:a2e2f3612c17956e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# LazySequence

<sub>Structure</sub>

A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct LazySequence<Base> where Base : Sequence
```

## Overview

- See also: `LazySequenceProtocol`

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [LazyCollectionProtocol](lazycollectionprotocol.md), [LazySequenceProtocol](lazysequenceprotocol.md), [RandomAccessCollection](randomaccesscollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Instance Methods

- [mapAnnotations(_:)](<lazysequence/mapannotations(__).md>) — Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the annotation of an annotated feature.
- [mapFeatures(_:)](<lazysequence/mapfeatures(__).md>) — Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the feature of an annotated feature.

### Default Implementations

- [BidirectionalCollection Implementations](lazysequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](lazysequence/collection-implementations.md)
- [LazySequenceProtocol Implementations](lazysequence/lazysequenceprotocol-implementations.md)
- [RandomAccessCollection Implementations](lazysequence/randomaccesscollection-implementations.md)
- [Sequence Implementations](lazysequence/sequence-implementations.md)

## See Also

### Lazy Wrappers

- [LazyMapSequence](lazymapsequence.md) — A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyFilterSequence](lazyfiltersequence.md) — A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md) — A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyDropWhileSequence](lazydropwhilesequence.md) — A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyCollection](lazycollection.md) — A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyDropWhileCollection](lazydropwhilecollection.md) — A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.
- [LazyFilterCollection](lazyfiltercollection.md) — A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [LazyMapCollection](lazymapcollection.md) — A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyPrefixWhileCollection](lazyprefixwhilecollection.md) — A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.
