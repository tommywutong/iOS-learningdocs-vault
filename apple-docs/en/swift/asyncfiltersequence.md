---
title: AsyncFilterSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncfiltersequence
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence.json'
content_hash: 'sha256:231001c7eff04552'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncFilterSequence

<sub>Structure</sub>

An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncFilterSequence<Base> where Base : AsyncSequence
```

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Iterator](asyncfiltersequence/iterator.md) — The iterator that produces elements of the filter sequence.

### Type Aliases

- [Failure](asyncfiltersequence/failure.md) — The type of the error that can be produced by the sequence.

### Default Implementations

- [AsyncSequence Implementations](asyncfiltersequence/asyncsequence-implementations.md)

## See Also

### Excluding Elements

- [dropFirst(_:)](<asyncsequence/dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [AsyncDropFirstSequence](asyncdropfirstsequence.md) — An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [drop(while:)](<asyncsequence/drop(while_)-9sp3b.md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [AsyncDropWhileSequence](asyncdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [drop(while:)](<asyncsequence/drop(while_)-67kgo.md>) — Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [filter(_:)](<asyncsequence/filter(__)-435af.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [filter(_:)](<asyncsequence/filter(__)-2cc0l.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
