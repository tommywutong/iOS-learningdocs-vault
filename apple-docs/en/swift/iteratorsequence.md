---
title: IteratorSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/iteratorsequence
source_url: 'https://developer.apple.com/documentation/swift/iteratorsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/iteratorsequence.json'
content_hash: 'sha256:7e29fe49d571ed9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# IteratorSequence

<sub>Structure</sub>

A sequence built around an iterator of type `Base`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct IteratorSequence<Base> where Base : IteratorProtocol
```

## Overview

Useful mostly to recover the ability to use `for`…`in`, given just an iterator `i`:

```swift
for x in IteratorSequence(i) { ... }
```

## Relationships

- **Conforms To**: [Copyable](copyable.md), [Escapable](escapable.md), [IteratorProtocol](iteratorprotocol.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<iteratorsequence/init(__).md>) — Creates an instance whose iterator is a copy of `base`.

### Default Implementations

- [IteratorProtocol Implementations](iteratorsequence/iteratorprotocol-implementations.md)
- [Sequence Implementations](iteratorsequence/sequence-implementations.md)

## See Also

### Indices and Iterators

- [IndexingIterator](indexingiterator.md) — A type that iterates over a collection using its indices.
- [EnumeratedIterator](enumeratediterator.md)
- [SetIterator](setiterator.md)
- [StrideThroughIterator](stridethroughiterator.md) — An iterator for a `StrideThrough` instance.
- [StrideToIterator](stridetoiterator.md) — An iterator for a `StrideTo` instance.
