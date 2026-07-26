---
title: AnyIterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyiterator
source_url: 'https://developer.apple.com/documentation/swift/anyiterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyiterator.json'
content_hash: 'sha256:542491319b3d0783'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyIterator

<sub>Structure</sub>

A type-erased iterator of `Element`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyIterator<Element>
```

## Overview

This iterator forwards its `next()` method to an arbitrary underlying iterator having the same `Element` type, hiding the specifics of the underlying `IteratorProtocol`.

## Relationships

- **Conforms To**: [Copyable](copyable.md), [Escapable](escapable.md), [IteratorProtocol](iteratorprotocol.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<anyiterator/init(__)-3m1u6.md>) — Creates an iterator that wraps a base iterator but whose type depends only on the base iterator’s element type.
- [init(_:)](<anyiterator/init(__)-5l6js.md>) — Creates an iterator that wraps the given closure in its `next()` method.

### Default Implementations

- [IteratorProtocol Implementations](anyiterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](anyiterator/sequence-implementations.md)

## See Also

### Type-Erasing Wrappers

- [AnySequence](anysequence.md) — A type-erased sequence.
- [AnyCollection](anycollection.md) — A type-erased wrapper over any collection with indices that support forward traversal.
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — A type-erased wrapper over any collection with indices that support random access traversal.
- [AnyIndex](anyindex.md) — A wrapper over an underlying index that hides the specific underlying type.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.
