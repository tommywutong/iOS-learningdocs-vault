---
title: EnumeratedIterator
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swift/enumeratediterator
source_url: 'https://developer.apple.com/documentation/swift/enumeratediterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratediterator.json'
content_hash: 'sha256:101ba427c1230e9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# EnumeratedIterator

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias EnumeratedIterator<T> = EnumeratedSequence<T>.Iterator where T : Sequence
```

## See Also

### Indices and Iterators

- [IteratorSequence](iteratorsequence.md) — A sequence built around an iterator of type `Base`.
- [IndexingIterator](indexingiterator.md) — A type that iterates over a collection using its indices.
- [SetIterator](setiterator.md)
- [StrideThroughIterator](stridethroughiterator.md) — An iterator for a `StrideThrough` instance.
- [StrideToIterator](stridetoiterator.md) — An iterator for a `StrideTo` instance.
