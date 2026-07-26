---
title: JoinedSequence.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/joinedsequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/joinedsequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/joinedsequence/iterator.json'
content_hash: 'sha256:cc109d4c9ede8bc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [JoinedSequence](../joinedsequence.md)

# JoinedSequence.Iterator

<sub>Structure</sub>

An iterator that presents the elements of the sequences traversed by a base iterator, concatenated using a given separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Escapable](../escapable.md), [IteratorProtocol](../iteratorprotocol.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init(base:separator:)](<iterator/init(base_separator_).md>) — Creates an iterator that presents the elements of `base` sequences concatenated using `separator`.

### Default Implementations

- [IteratorProtocol Implementations](iterator/iteratorprotocol-implementations.md)
