---
title: ReversedCollection.Index
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection/index
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/index.json'
content_hash: 'sha256:8ebf17c3ef23ef3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ReversedCollection](../reversedcollection.md)

# ReversedCollection.Index

<sub>Structure</sub>

An index that traverses the same positions as an underlying index, with inverted traversal direction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Index
```

## Relationships

- **Conforms To**: [Comparable](../comparable.md), [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<index/init(__).md>) — Creates a new index into a reversed collection for the position before the specified index.

### Instance Properties

- [base](index/base.md) — The position after this position in the underlying collection.

### Default Implementations

- [Comparable Implementations](index/comparable-implementations.md)
- [Equatable Implementations](index/equatable-implementations.md)
- [Hashable Implementations](index/hashable-implementations.md)
