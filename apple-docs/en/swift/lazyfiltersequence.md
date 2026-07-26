---
title: LazyFilterSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyfiltersequence
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence.json'
content_hash: 'sha256:77c46c3066263492'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# LazyFilterSequence

<sub>Structure</sub>

A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct LazyFilterSequence<Base> where Base : Sequence
```

## Overview

> [!note] Note
> `s.lazy.filter { ... }`, for an arbitrary sequence `s`, is a `LazyFilterSequence`.

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [LazyCollectionProtocol](lazycollectionprotocol.md), [LazySequenceProtocol](lazysequenceprotocol.md), [Sequence](sequence.md)

## Topics

### Instance Properties

- [underestimatedCount](lazyfiltersequence/underestimatedcount.md)

### Instance Methods

- [filter(_:)](<lazyfiltersequence/filter(__).md>)
- [formIndex(_:offsetBy:)](<lazyfiltersequence/formindex(__offsetby_).md>)
- [formIndex(_:offsetBy:limitedBy:)](<lazyfiltersequence/formindex(__offsetby_limitedby_).md>)

### Default Implementations

- [BidirectionalCollection Implementations](lazyfiltersequence/bidirectionalcollection-implementations.md)
- [Collection Implementations](lazyfiltersequence/collection-implementations.md)
- [LazySequenceProtocol Implementations](lazyfiltersequence/lazysequenceprotocol-implementations.md)
- [Sequence Implementations](lazyfiltersequence/sequence-implementations.md)

## See Also

### Lazy Wrappers

- [LazySequence](lazysequence.md) — A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyMapSequence](lazymapsequence.md) — A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md) — A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyDropWhileSequence](lazydropwhilesequence.md) — A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyCollection](lazycollection.md) — A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyDropWhileCollection](lazydropwhilecollection.md) — A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.
- [LazyFilterCollection](lazyfiltercollection.md) — A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [LazyMapCollection](lazymapcollection.md) — A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyPrefixWhileCollection](lazyprefixwhilecollection.md) — A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.
