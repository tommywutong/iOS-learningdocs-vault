---
title: StrideThroughIterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/stridethroughiterator
source_url: 'https://developer.apple.com/documentation/swift/stridethroughiterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stridethroughiterator.json'
content_hash: 'sha256:edaf9c37146c9aab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# StrideThroughIterator

<sub>Structure</sub>

An iterator for a `StrideThrough` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct StrideThroughIterator<Element> where Element : Strideable
```

## Relationships

- **Conforms To**: [Copyable](copyable.md), [Escapable](escapable.md), [IteratorProtocol](iteratorprotocol.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Default Implementations

- [IteratorProtocol Implementations](stridethroughiterator/iteratorprotocol-implementations.md)

## See Also

### Indices and Iterators

- [IteratorSequence](iteratorsequence.md) — A sequence built around an iterator of type `Base`.
- [IndexingIterator](indexingiterator.md) — A type that iterates over a collection using its indices.
- [EnumeratedIterator](enumeratediterator.md)
- [SetIterator](setiterator.md)
- [StrideToIterator](stridetoiterator.md) — An iterator for a `StrideTo` instance.
