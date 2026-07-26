---
title: DiscontiguousSlice
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/discontiguousslice
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice.json'
content_hash: 'sha256:5ecaf9752516108c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# DiscontiguousSlice

<sub>Structure</sub>

A collection wrapper that provides access to the elements of a collection, indexed by a set of indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DiscontiguousSlice<Base> where Base : Collection
```

## Relationships

- **Conforms To**: [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [Copyable](copyable.md), [CustomStringConvertible](customstringconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Instance Properties

- [base](discontiguousslice/base.md) — The collection that the indexed collection wraps.
- [subranges](discontiguousslice/subranges.md) — The set of subranges that are available through this discontiguous slice.

### Subscripts

- [subscript(_:)](<discontiguousslice/subscript(__)-1j7n7.md>) — Accesses the element at the specified position.

### Default Implementations

- [BidirectionalCollection Implementations](discontiguousslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](discontiguousslice/collection-implementations.md)
- [CustomStringConvertible Implementations](discontiguousslice/customstringconvertible-implementations.md)
- [Equatable Implementations](discontiguousslice/equatable-implementations.md)
- [Hashable Implementations](discontiguousslice/hashable-implementations.md)
- [Sequence Implementations](discontiguousslice/sequence-implementations.md)
