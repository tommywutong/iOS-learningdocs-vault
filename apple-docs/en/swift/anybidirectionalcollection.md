---
title: AnyBidirectionalCollection
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anybidirectionalcollection
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection.json'
content_hash: 'sha256:fa4de8c1f4076fa2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyBidirectionalCollection

<sub>Structure</sub>

A type-erased wrapper over any collection with indices that support bidirectional traversal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyBidirectionalCollection<Element>
```

## Overview

An `AnyBidirectionalCollection` instance forwards its operations to a base collection having the same `Element` type, hiding the specifics of the underlying collection.

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<anybidirectionalcollection/init(__)-1hwm5.md>) — Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.
- [init(_:)](<anybidirectionalcollection/init(__)-2kvez.md>) — Creates a type-erased collection that wraps the given collection.
- [init(_:)](<anybidirectionalcollection/init(__)-4hewp.md>) — Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.
- [init(_:)](<anybidirectionalcollection/init(__)-5lybd.md>) — Creates a type-erased collection that wraps the given collection.
- [init(_:)](<anybidirectionalcollection/init(__)-61joz.md>) — Creates an `AnyBidirectionalCollection` having the same underlying collection as `other`.

### Instance Methods

- [drop(while:)](<anybidirectionalcollection/drop(while_).md>)
- [dropFirst(_:)](<anybidirectionalcollection/dropfirst(__).md>)
- [dropLast(_:)](<anybidirectionalcollection/droplast(__).md>)
- [filter(_:)](<anybidirectionalcollection/filter(__).md>)
- [forEach(_:)](<anybidirectionalcollection/foreach(__).md>)
- [formIndex(_:offsetBy:)](<anybidirectionalcollection/formindex(__offsetby_).md>)
- [formIndex(_:offsetBy:limitedBy:)](<anybidirectionalcollection/formindex(__offsetby_limitedby_).md>)
- [map(_:)](<anybidirectionalcollection/map(__).md>)
- [prefix(_:)](<anybidirectionalcollection/prefix(__).md>)
- [prefix(while:)](<anybidirectionalcollection/prefix(while_).md>)
- [suffix(_:)](<anybidirectionalcollection/suffix(__).md>)

### Default Implementations

- [BidirectionalCollection Implementations](anybidirectionalcollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](anybidirectionalcollection/collection-implementations.md)
- [Sequence Implementations](anybidirectionalcollection/sequence-implementations.md)

## See Also

### Type-Erasing Wrappers

- [AnySequence](anysequence.md) — A type-erased sequence.
- [AnyCollection](anycollection.md) — A type-erased wrapper over any collection with indices that support forward traversal.
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — A type-erased wrapper over any collection with indices that support random access traversal.
- [AnyIterator](anyiterator.md) — A type-erased iterator of `Element`.
- [AnyIndex](anyindex.md) — A wrapper over an underlying index that hides the specific underlying type.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.
