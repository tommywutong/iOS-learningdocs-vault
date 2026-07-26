---
title: Dictionary.Keys.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/keys-swift.struct/iterator
source_url: 'https://developer.apple.com/documentation/swift/dictionary/keys-swift.struct/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/keys-swift.struct/iterator.json'
content_hash: 'sha256:80047e96ea4f7852'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Keys](../keys-swift.struct.md)

# Dictionary.Keys.Iterator

<sub>Structure</sub>

A type that provides the collection’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Overview

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## Relationships

- **Conforms To**: [IteratorProtocol](../../iteratorprotocol.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Instance Methods

- [next()](<iterator/next().md>) — Advances to the next element and returns it, or `nil` if no next element exists.

### Type Aliases

- [Element](iterator/element.md) — The type of element traversed by the iterator.
