---
title: AsyncFilterSequence.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncfiltersequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence/iterator.json'
content_hash: 'sha256:ce15d3aaeaea21ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncFilterSequence](../asyncfiltersequence.md)

# AsyncFilterSequence.Iterator

<sub>Structure</sub>

The iterator that produces elements of the filter sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Iterator
```

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../asynciteratorprotocol.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Instance Methods

- [next()](<iterator/next().md>) — Produces the next element in the filter sequence.
- [next(isolation:)](<iterator/next(isolation_).md>) — Produces the next element in the filter sequence.

### Type Aliases

- [Element](iterator/element.md)

### Default Implementations

- [AsyncIteratorProtocol Implementations](iterator/asynciteratorprotocol-implementations.md)
