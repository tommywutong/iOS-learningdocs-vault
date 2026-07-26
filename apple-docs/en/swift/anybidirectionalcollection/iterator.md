---
title: AnyBidirectionalCollection.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anybidirectionalcollection/iterator
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/iterator.json'
content_hash: 'sha256:da10ac622ee8a79c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# AnyBidirectionalCollection.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = AnyIterator<Element>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
