---
title: LazyMapCollection
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazymapcollection
source_url: 'https://developer.apple.com/documentation/swift/lazymapcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapcollection.json'
content_hash: 'sha256:980bfabfd438db4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# LazyMapCollection

<sub>Type Alias</sub>

A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias LazyMapCollection<T, U> = LazyMapSequence<T, U> where T : Collection
```

## See Also

### Lazy Wrappers

- [LazySequence](lazysequence.md) — A sequence containing the same elements as a `Base` sequence, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyMapSequence](lazymapsequence.md) — A `Sequence` whose elements consist of those in a `Base` `Sequence` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
- [LazyFilterSequence](lazyfiltersequence.md) — A sequence whose elements consist of the elements of some base sequence that also satisfy a given predicate.
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md) — A sequence whose elements consist of the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyDropWhileSequence](lazydropwhilesequence.md) — A sequence whose elements consist of the elements that follow the initial consecutive elements of some base sequence that satisfy a given predicate.
- [LazyCollection](lazycollection.md) — A collection containing the same elements as a `Base` collection, but on which some operations such as `map` and `filter` are implemented lazily.
- [LazyDropWhileCollection](lazydropwhilecollection.md) — A lazy wrapper that includes the elements of an underlying collection after any initial consecutive elements that satisfy a predicate.
- [LazyFilterCollection](lazyfiltercollection.md) — A lazy `Collection` wrapper that includes the elements of an underlying collection that satisfy a predicate.
- [LazyPrefixWhileCollection](lazyprefixwhilecollection.md) — A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.
