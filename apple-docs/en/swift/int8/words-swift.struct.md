---
title: Int8.Words
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int8/words-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/int8/words-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/words-swift.struct.json'
content_hash: 'sha256:c16e0b11b53b8906'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

# Int8.Words

<sub>Structure</sub>

A type that represents the words of this integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Words
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../bidirectionalcollection.md), [BitwiseCopyable](../bitwisecopyable.md), [Collection](../collection.md), [Copyable](../copyable.md), [RandomAccessCollection](../randomaccesscollection.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [Sequence](../sequence.md)

## Topics

### Initializers

- [init(_:)](<words-swift.struct/init(__).md>)

### Instance Properties

- [count](words-swift.struct/count.md) — The number of elements in the collection.
- [endIndex](words-swift.struct/endindex.md) — The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](words-swift.struct/indices-swift.property.md) — The indices that are valid for subscripting the collection, in ascending order.
- [startIndex](words-swift.struct/startindex.md) — The position of the first element in a nonempty collection.

### Instance Methods

- [index(after:)](<words-swift.struct/index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<words-swift.struct/index(before_).md>) — Returns the position immediately before the given index.

### Subscripts

- [subscript(_:)](<words-swift.struct/subscript(__).md>) — Accesses the element at the specified position.

### Type Aliases

- [Element](words-swift.struct/element.md) — A type representing the sequence’s elements.
- [Index](words-swift.struct/index.md) — A type that represents a position in the collection.
- [Indices](words-swift.struct/indices-swift.typealias.md) — A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Iterator](words-swift.struct/iterator.md) — A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [SubSequence](words-swift.struct/subsequence.md) — A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

### Default Implementations

- [BidirectionalCollection Implementations](words-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](words-swift.struct/collection-implementations.md)
- [RandomAccessCollection Implementations](words-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](words-swift.struct/sequence-implementations.md)
