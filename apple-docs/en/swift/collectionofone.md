---
title: CollectionOfOne
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectionofone
source_url: 'https://developer.apple.com/documentation/swift/collectionofone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone.json'
content_hash: 'sha256:26155c4b2b10b29e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CollectionOfOne

<sub>Structure</sub>

A collection containing a single element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct CollectionOfOne<Element>
```

## Overview

You can use a `CollectionOfOne` instance when you need to efficiently represent a single value as a collection. For example, you can add a single element to an array by using a `CollectionOfOne` instance with the concatenation operator (`+`):

```swift
let a = [1, 2, 3, 4]
let toAdd = 100
let b = a + CollectionOfOne(toAdd)
// b == [1, 2, 3, 4, 100]
```

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [BitwiseCopyable](bitwisecopyable.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [MutableCollection](mutablecollection.md), [RandomAccessCollection](randomaccesscollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<collectionofone/init(__).md>) — Creates an instance containing just the given element.

### Instance Properties

- [mutableSpan](collectionofone/mutablespan.md) — A mutable span over the single element of this collection.
- [span](collectionofone/span.md) — A span over the single element of this collection.

### Default Implementations

- [BidirectionalCollection Implementations](collectionofone/bidirectionalcollection-implementations.md)
- [Collection Implementations](collectionofone/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](collectionofone/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](collectionofone/customreflectable-implementations.md)
- [Equatable Implementations](collectionofone/equatable-implementations.md)
- [Hashable Implementations](collectionofone/hashable-implementations.md)
- [MutableCollection Implementations](collectionofone/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](collectionofone/randomaccesscollection-implementations.md)
- [Sequence Implementations](collectionofone/sequence-implementations.md)

## See Also

### Special-Use Collections

- [repeatElement(_:count:)](<repeatelement(__count_).md>) — Creates a collection containing the specified number of the given element.
- [EmptyCollection](emptycollection.md) — A collection whose element type is `Element` but that is always empty.
- [KeyValuePairs](keyvaluepairs.md) — A lightweight collection of key-value pairs.
- [DictionaryLiteral](dictionaryliteral.md)
