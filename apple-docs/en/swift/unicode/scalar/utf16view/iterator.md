---
title: Unicode.Scalar.UTF16View.Iterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/utf16view/iterator
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf16view/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf16view/iterator.json'
content_hash: 'sha256:b4b7f5e209d16017'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF16View](../utf16view.md)

# Unicode.Scalar.UTF16View.Iterator

<sub>Type Alias</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Iterator = IndexingIterator<Unicode.Scalar.UTF16View>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.
