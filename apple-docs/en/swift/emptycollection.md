---
title: EmptyCollection
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/emptycollection
source_url: 'https://developer.apple.com/documentation/swift/emptycollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/emptycollection.json'
content_hash: 'sha256:1d3b4f733ed52782'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# EmptyCollection

<sub>Structure</sub>

A collection whose element type is `Element` but that is always empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct EmptyCollection<Element>
```

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [BitwiseCopyable](bitwisecopyable.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](copyable.md), [DataProtocol](../foundation/dataprotocol.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [MutableCollection](mutablecollection.md), [RandomAccessCollection](randomaccesscollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init()](<emptycollection/init().md>) — Creates an instance.

### Default Implementations

- [BidirectionalCollection Implementations](emptycollection/bidirectionalcollection-implementations.md)
- [Collection Implementations](emptycollection/collection-implementations.md)
- [Equatable Implementations](emptycollection/equatable-implementations.md)
- [Hashable Implementations](emptycollection/hashable-implementations.md)
- [MutableCollection Implementations](emptycollection/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](emptycollection/randomaccesscollection-implementations.md)
- [Sequence Implementations](emptycollection/sequence-implementations.md)

## See Also

### Special-Use Collections

- [repeatElement(_:count:)](<repeatelement(__count_).md>) — Creates a collection containing the specified number of the given element.
- [CollectionOfOne](collectionofone.md) — A collection containing a single element.
- [KeyValuePairs](keyvaluepairs.md) — A lightweight collection of key-value pairs.
- [DictionaryLiteral](dictionaryliteral.md)
