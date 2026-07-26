---
title: AnyIndex
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyindex
source_url: 'https://developer.apple.com/documentation/swift/anyindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyindex.json'
content_hash: 'sha256:f172f6191d2151b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyIndex

<sub>Structure</sub>

A wrapper over an underlying index that hides the specific underlying type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyIndex
```

## Relationships

- **Conforms To**: [Comparable](comparable.md), [Equatable](equatable.md)

## Topics

### Initializers

- [init(_:)](<anyindex/init(__).md>) — Creates a new index wrapping `base`.

### Default Implementations

- [Comparable Implementations](anyindex/comparable-implementations.md)
- [Equatable Implementations](anyindex/equatable-implementations.md)

## See Also

### Type-Erasing Wrappers

- [AnySequence](anysequence.md) — A type-erased sequence.
- [AnyCollection](anycollection.md) — A type-erased wrapper over any collection with indices that support forward traversal.
- [AnyBidirectionalCollection](anybidirectionalcollection.md) — A type-erased wrapper over any collection with indices that support bidirectional traversal.
- [AnyRandomAccessCollection](anyrandomaccesscollection.md) — A type-erased wrapper over any collection with indices that support random access traversal.
- [AnyIterator](anyiterator.md) — A type-erased iterator of `Element`.
- [AnyHashable](anyhashable.md) — A type-erased hashable value.
