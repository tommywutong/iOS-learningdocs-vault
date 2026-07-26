---
title: Iterator
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collection/iterator
source_url: 'https://developer.apple.com/documentation/swift/collection/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/iterator.json'
content_hash: 'sha256:76560638362af418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# Iterator

<sub>Associated Type</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Iterator = IndexingIterator<Self>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
