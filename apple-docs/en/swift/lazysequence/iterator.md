---
title: LazySequence.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/iterator.json'
content_hash: 'sha256:10368962908c3f35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# LazySequence.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = Base.Iterator
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
