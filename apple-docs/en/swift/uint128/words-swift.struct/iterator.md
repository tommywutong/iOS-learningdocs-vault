---
title: UInt128.Words.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint128/words-swift.struct/iterator
source_url: 'https://developer.apple.com/documentation/swift/uint128/words-swift.struct/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/words-swift.struct/iterator.json'
content_hash: 'sha256:593654139d9a07b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt128](../../uint128.md) · [Words](../words-swift.struct.md)

# UInt128.Words.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = IndexingIterator<UInt128.Words>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
