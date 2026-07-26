---
title: PartialRangeFrom.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/partialrangefrom/iterator
source_url: 'https://developer.apple.com/documentation/swift/partialrangefrom/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/partialrangefrom/iterator.json'
content_hash: 'sha256:ead6b518c6fb5c65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [PartialRangeFrom](../partialrangefrom.md)

# PartialRangeFrom.Iterator

<sub>Structure</sub>

The iterator for a `PartialRangeFrom` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [ConvertibleFromBytes](../convertiblefrombytes.md), [ConvertibleToBytes](../convertibletobytes.md), [Copyable](../copyable.md), [Escapable](../escapable.md), [IteratorProtocol](../iteratorprotocol.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Instance Methods

- [next()](<iterator/next().md>) — Advances to the next element and returns it, or `nil` if no next element exists.

### Type Aliases

- [Element](iterator/element.md) — The type of element traversed by the iterator.
