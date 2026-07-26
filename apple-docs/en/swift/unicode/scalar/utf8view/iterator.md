---
title: Unicode.Scalar.UTF8View.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/utf8view/iterator
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf8view/iterator.json'
content_hash: 'sha256:434976beceb5926f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF8View](../utf8view.md)

# Unicode.Scalar.UTF8View.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = IndexingIterator<Unicode.Scalar.UTF8View>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
