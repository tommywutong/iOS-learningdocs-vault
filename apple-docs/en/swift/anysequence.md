---
title: AnySequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anysequence
source_url: 'https://developer.apple.com/documentation/swift/anysequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anysequence.json'
content_hash: 'sha256:4190bf30764b2c21'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnySequence

<sub>Structure</sub>

A type-erased sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnySequence<Element>
```

## Overview

An instance of `AnySequence` forwards its operations to an underlying base sequence having the same `Element` type, hiding the specifics of the underlying sequence.

## Relationships

- **Conforms To**: [Copyable](copyable.md), [Escapable](escapable.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<anysequence/init(__)-25934.md>) — Creates a sequence whose `makeIterator()` method forwards to `makeUnderlyingIterator`.
- [init(_:)](<anysequence/init(__)-307a9.md>) — Creates a new sequence that wraps and forwards operations to `base`.

### Instance Methods

- [drop(while:)](<anysequence/drop(while_).md>)
- [dropFirst(_:)](<anysequence/dropfirst(__).md>)
- [dropLast(_:)](<anysequence/droplast(__).md>)
- [filter(_:)](<anysequence/filter(__).md>)
- [forEach(_:)](<anysequence/foreach(__).md>)
- [map(_:)](<anysequence/map(__).md>)
- [prefix(_:)](<anysequence/prefix(__).md>)
- [prefix(while:)](<anysequence/prefix(while_).md>)
- [suffix(_:)](<anysequence/suffix(__).md>)

### Default Implementations

- [Sequence Implementations](anysequence/sequence-implementations.md)

## See Also

### Type-Erasing Wrappers

- [AnyCollection](anycollection.md) — A type-erased wrapper over any collection with indices that support forward traversal.
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — A type-erased wrapper over any collection with indices that support random access traversal.
- [AnyIterator](anyiterator.md) — A type-erased iterator of `Element`.
- [AnyIndex](anyindex.md) — A wrapper over an underlying index that hides the specific underlying type.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.
