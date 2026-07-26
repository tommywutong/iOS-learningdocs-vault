---
title: LazyPrefixWhileSequence.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyprefixwhilesequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyprefixwhilesequence/iterator.json'
content_hash: 'sha256:a0ac31a4691d0342'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyPrefixWhileSequence](../lazyprefixwhilesequence.md)

# LazyPrefixWhileSequence.Iterator

<sub>Structure</sub>

An iterator over the initial elements traversed by a base iterator that satisfy a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Overview

This is the associated iterator for the `LazyPrefixWhileSequence`, `LazyPrefixWhileCollection`, and `LazyPrefixWhileBidirectionalCollection` types.

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Escapable](../escapable.md), [IteratorProtocol](../iteratorprotocol.md), [Sequence](../sequence.md)

## Topics

### Type Aliases

- [Element](iterator/element.md) — The type of element traversed by the iterator.

### Default Implementations

- [IteratorProtocol Implementations](iterator/iteratorprotocol-implementations.md)
- [Sequence Implementations](iterator/sequence-implementations.md)
