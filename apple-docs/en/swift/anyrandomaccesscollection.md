---
title: AnyRandomAccessCollection
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyrandomaccesscollection
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection.json'
content_hash: 'sha256:92131efa66daca65'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyRandomAccessCollection

<sub>Structure</sub>

A type-erased wrapper over any collection with indices that support random access traversal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyRandomAccessCollection<Element>
```

## Overview

An `AnyRandomAccessCollection` instance forwards its operations to a base collection having the same `Element` type, hiding the specifics of the underlying collection.

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [Escapable](escapable.md), [RandomAccessCollection](randomaccesscollection.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<anyrandomaccesscollection/init(__)-1qlza.md>) — Creates a type-erased collection that wraps the given collection.
- [init(_:)](<anyrandomaccesscollection/init(__)-2j41k.md>) — Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.
- [init(_:)](<anyrandomaccesscollection/init(__)-60sab.md>) — Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.
- [init(_:)](<anyrandomaccesscollection/init(__)-66pkb.md>) — Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.

### Instance Methods

- [drop(while:)](<anyrandomaccesscollection/drop(while_).md>)
- [dropFirst(_:)](<anyrandomaccesscollection/dropfirst(__).md>)
- [dropLast(_:)](<anyrandomaccesscollection/droplast(__).md>)
- [filter(_:)](<anyrandomaccesscollection/filter(__).md>)
- [forEach(_:)](<anyrandomaccesscollection/foreach(__).md>)
- [formIndex(_:offsetBy:)](<anyrandomaccesscollection/formindex(__offsetby_).md>)
- [formIndex(_:offsetBy:limitedBy:)](<anyrandomaccesscollection/formindex(__offsetby_limitedby_).md>)
- [map(_:)](<anyrandomaccesscollection/map(__).md>)
- [prefix(_:)](<anyrandomaccesscollection/prefix(__).md>)
- [prefix(while:)](<anyrandomaccesscollection/prefix(while_).md>)
- [suffix(_:)](<anyrandomaccesscollection/suffix(__).md>)

### Default Implementations

- [BidirectionalCollection Implementations](anyrandomaccesscollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](anyrandomaccesscollection/collection-implementations.md)
- [RandomAccessCollection Implementations](anyrandomaccesscollection/randomaccesscollection-implementations.md)
- [Sequence Implementations](anyrandomaccesscollection/sequence-implementations.md)

## See Also

### Type-Erasing Wrappers

- [AnySequence](anysequence.md) — A type-erased sequence.
- [AnyCollection](anycollection.md) — A type-erased wrapper over any collection with indices that support forward traversal.
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [AnyIterator](anyiterator.md) — A type-erased iterator of `Element`.
- [AnyIndex](anyindex.md) — A wrapper over an underlying index that hides the specific underlying type.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.
