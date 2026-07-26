---
title: LazyPrefixWhileCollection
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyprefixwhilecollection
source_url: 'https://developer.apple.com/documentation/swift/lazyprefixwhilecollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyprefixwhilecollection.json'
content_hash: 'sha256:95fe401723edc4c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# LazyPrefixWhileCollection

<sub>Type Alias</sub>

A lazy collection wrapper that includes the initial consecutive elements of an underlying collection that satisfy a predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias LazyPrefixWhileCollection<T> = LazyPrefixWhileSequence<T> where T : Collection
```

## Discussion

> [!note] Note
> The performance of accessing `endIndex` depends on how many elements satisfy the predicate at the start of the collection, and might not offer the usual performance given by the `Collection` protocol. Accessing `endIndex`, the `last` property, or calling methods that depend on moving indices might not have the documented complexity.

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
- [LazyMapCollection](lazymapcollection.md) — A `Collection` whose elements consist of those in a `Base` `Collection` passed through a transform function returning `Element`. These elements are computed lazily, each time they’re read, by calling the transform function on a base element.
