---
title: EnumeratedSequence.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/enumeratedsequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/iterator.json'
content_hash: 'sha256:cfe7506bbc9a9eb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# EnumeratedSequence.Iterator

<sub>Structure</sub>

The iterator for `EnumeratedSequence`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Overview

An instance of this iterator wraps a base iterator and yields successive `Int` values, starting at zero, along with the elements of the underlying base iterator. The following example enumerates the elements of an array:

```swift
var iterator = ["foo", "bar"].enumerated().makeIterator()
iterator.next() // (0, "foo")
iterator.next() // (1, "bar")
iterator.next() // nil
```

To create an instance, call `enumerated().makeIterator()` on a sequence or collection.

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Escapable](../escapable.md), [IteratorProtocol](../iteratorprotocol.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [Sequence](../sequence.md)

## Topics

### Default Implementations

- [IteratorProtocol Implementations](iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](iterator/sequence-implementations.md)
