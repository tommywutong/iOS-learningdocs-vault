---
title: Int8.Words.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/words-swift.struct/iterator
source_url: 'https://developer.apple.com/documentation/swift/int8/words-swift.struct/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/words-swift.struct/iterator.json'
content_hash: 'sha256:9dacdfceb060ddf9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int8](../../int8.md) · [Words](../words-swift.struct.md)

# Int8.Words.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = IndexingIterator<Int8.Words>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
