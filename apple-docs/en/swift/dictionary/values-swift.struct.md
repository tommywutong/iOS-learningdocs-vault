---
title: Dictionary.Values
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/values-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct.json'
content_hash: 'sha256:a471c25100afc202'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# Dictionary.Values

<sub>Structure</sub>

A view of a dictionary’s values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Values
```

## Relationships

- **Conforms To**: [Collection](../collection.md), [Copyable](../copyable.md), [CustomDebugStringConvertible](../customdebugstringconvertible.md), [CustomStringConvertible](../customstringconvertible.md), [Escapable](../escapable.md), [MutableCollection](../mutablecollection.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [Sequence](../sequence.md)

## Topics

### Instance Properties

- [count](values-swift.struct/count.md) — The number of values in the dictionary.
- [endIndex](values-swift.struct/endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [isEmpty](values-swift.struct/isempty.md) — A Boolean value indicating whether the collection is empty.
- [startIndex](values-swift.struct/startindex.md) — The position of the first element in a nonempty collection.

### Instance Methods

- [formIndex(after:)](<values-swift.struct/formindex(after_).md>) — Replaces the given index with its successor.
- [index(after:)](<values-swift.struct/index(after_).md>) — Returns the position immediately after the given index.
- [swapAt(_:_:)](<values-swift.struct/swapat(____).md>) — Exchanges the values at the specified indices of the collection.

### Subscripts

- [subscript(_:)](<values-swift.struct/subscript(__).md>) — Accesses the element at the specified position.

### Type Aliases

- [Element](values-swift.struct/element.md) — A type representing the sequence’s elements.
- [Index](values-swift.struct/index.md) — A type that represents a position in the collection.
- [Indices](values-swift.struct/indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [SubSequence](values-swift.struct/subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

### Default Implementations

- [Collection Implementations](values-swift.struct/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](values-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](values-swift.struct/customstringconvertible-implementations.md)
- [MutableCollection Implementations](values-swift.struct/mutablecollection-implementations.md)
- [Sequence Implementations](values-swift.struct/sequence-implementations.md)

## See Also

### Supporting Types

- [Keys](keys-swift.struct.md) — A view of a dictionary’s keys.
- [Index](index.md) — The position of a key-value pair in a dictionary.
- [Indices](indices.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Iterator](iterator.md) — An iterator over the members of a `Dictionary<Key, Value>`.
