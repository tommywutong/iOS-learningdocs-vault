---
title: AnyCollection
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anycollection
source_url: 'https://developer.apple.com/documentation/swift/anycollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anycollection.json'
content_hash: 'sha256:23f06d73999502b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyCollection

<sub>Structure</sub>

A type-erased wrapper over any collection with indices that support forward traversal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyCollection<Element>
```

## Overview

An `AnyCollection` instance forwards its operations to a base collection having the same `Element` type, hiding the specifics of the underlying collection.

## Relationships

- **Conforms To**: [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<anycollection/init(__)-1jdmb.md>) — Creates an `AnyCollection` having the same underlying collection as `other`.
- [init(_:)](<anycollection/init(__)-33dcu.md>) — Creates a type-erased collection that wraps the given collection.
- [init(_:)](<anycollection/init(__)-598x3.md>) — Creates an `AnyCollection` having the same underlying collection as `other`.
- [init(_:)](<anycollection/init(__)-8k2a5.md>) — Creates a type-erased collection that wraps the given collection.
- [init(_:)](<anycollection/init(__)-91xl3.md>) — Creates an `AnyCollection` having the same underlying collection as `other`.
- [init(_:)](<anycollection/init(__)-9mgej.md>) — Creates a type-erased collection that wraps the given collection.

### Instance Methods

- [drop(while:)](<anycollection/drop(while_).md>)
- [dropFirst(_:)](<anycollection/dropfirst(__).md>)
- [dropLast(_:)](<anycollection/droplast(__).md>)
- [filter(_:)](<anycollection/filter(__).md>)
- [forEach(_:)](<anycollection/foreach(__).md>)
- [formIndex(_:offsetBy:)](<anycollection/formindex(__offsetby_).md>)
- [formIndex(_:offsetBy:limitedBy:)](<anycollection/formindex(__offsetby_limitedby_).md>)
- [map(_:)](<anycollection/map(__).md>)
- [prefix(_:)](<anycollection/prefix(__).md>)
- [prefix(while:)](<anycollection/prefix(while_).md>)
- [suffix(_:)](<anycollection/suffix(__).md>)

### Default Implementations

- [Collection Implementations](anycollection/collection-implementations.md)
- [Sequence Implementations](anycollection/sequence-implementations.md)

## See Also

### Type-Erasing Wrappers

- [AnySequence](anysequence.md) — A type-erased sequence.
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — A type-erased wrapper over any collection with indices that support random access traversal.
- [AnyIterator](anyiterator.md) — A type-erased iterator of `Element`.
- [AnyIndex](anyindex.md) — A wrapper over an underlying index that hides the specific underlying type.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.
