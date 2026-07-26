---
title: LazyCollection
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazycollection
source_url: 'https://developer.apple.com/documentation/swift/lazycollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazycollection.json'
content_hash: 'sha256:e83836a1ddfba28e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# LazyCollection

<sub>Type Alias</sub>

A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias LazyCollection<T> = LazySequence<T> where T : Collection
```

## Discussion

- See also: `LazySequenceProtocol`, `LazyCollection`

## See Also

### Lazy Wrappers

- [LazySequence](lazysequence.md) — A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyMapSequence](lazymapsequence.md) — A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyFilterSequence](lazyfiltersequence.md) — A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md) — A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyDropWhileSequence](lazydropwhilesequence.md) — A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyDropWhileCollection](lazydropwhilecollection.md) — A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.
- [LazyFilterCollection](lazyfiltercollection.md) — A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [LazyMapCollection](lazymapcollection.md) — A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyPrefixWhileCollection](lazyprefixwhilecollection.md) — A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.
