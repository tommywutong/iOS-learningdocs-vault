---
title: Substring.UTF8View.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/utf8view/iterator
source_url: 'https://developer.apple.com/documentation/swift/substring/utf8view/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf8view/iterator.json'
content_hash: 'sha256:0af3fadee2ed1b14'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UTF8View](../utf8view.md)

# Substring.UTF8View.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = IndexingIterator<Substring.UTF8View>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
