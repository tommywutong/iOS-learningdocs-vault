---
title: LazyDropWhileSequence.Iterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazydropwhilesequence/iterator
source_url: 'https://developer.apple.com/documentation/swift/lazydropwhilesequence/iterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazydropwhilesequence/iterator.json'
content_hash: 'sha256:8e6d3b7e65bf11be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyDropWhileSequence](../lazydropwhilesequence.md)

# LazyDropWhileSequence.Iterator

<sub>Structure</sub>

An iterator over the elements traversed by a base iterator that follow the initial consecutive elements that satisfy a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Iterator
```

## Overview

This is the associated iterator for the `LazyDropWhileSequence`, `LazyDropWhileCollection`, and `LazyDropWhileBidirectionalCollection` types.

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Escapable](../escapable.md), [IteratorProtocol](../iteratorprotocol.md)

## Topics

### Type Aliases

- [Element](iterator/element.md) — The type of element traversed by the iterator.

### Default Implementations

- [IteratorProtocol Implementations](iterator/iteratorprotocol-implementations.md)
