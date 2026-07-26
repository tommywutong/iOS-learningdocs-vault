---
title: LazyFilterSequence.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyfiltersequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/iterator.json'
content_hash: 'sha256:0321b3e7b5d6f0ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# LazyFilterSequence.Iterator

<sub>Structure</sub>

An iterator over the elements traversed by some base iterator that also satisfy a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Overview

> [!note] Note
> This is the associated `Iterator` of `LazyFilterSequence` and `LazyFilterCollection`.

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Escapable](../escapable.md), [IteratorProtocol](../iteratorprotocol.md), [Sequence](../sequence.md)

## Topics

### Instance Properties

- [base](iterator/base.md) — The underlying iterator whose elements are being filtered.

### Default Implementations

- [IteratorProtocol Implementations](iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](iterator/sequence-implementations.md)
