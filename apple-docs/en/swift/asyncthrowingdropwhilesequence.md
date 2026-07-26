---
title: AsyncThrowingDropWhileSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingdropwhilesequence
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingdropwhilesequence.json'
content_hash: 'sha256:a90f56b353664088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncThrowingDropWhileSequence

<sub>Structure</sub>

An asynchronous sequence which omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncThrowingDropWhileSequence<Base> where Base : AsyncSequence
```

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Iterator](asyncthrowingdropwhilesequence/iterator.md) — The iterator that produces elements of the drop-while sequence.

### Type Aliases

- [Failure](asyncthrowingdropwhilesequence/failure.md) — The type of element produced by this asynchronous sequence.

### Default Implementations

- [AsyncSequence Implementations](asyncthrowingdropwhilesequence/asyncsequence-implementations.md)

## See Also

### Excluding Elements

- [dropFirst(_:)](<asyncsequence/dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [AsyncDropFirstSequence](asyncdropfirstsequence.md) — An asynchronous sequence which omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [drop(while:)](<asyncsequence/drop(while_)-9sp3b.md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [AsyncDropWhileSequence](asyncdropwhilesequence.md) — An asynchronous sequence which omits elements from the base sequence until a given closure returns false, after which it passes through all remaining elements.
- [drop(while:)](<asyncsequence/drop(while_)-67kgo.md>) — Omits elements from the base sequence until a given error-throwing closure returns false, after which it passes through all remaining elements.
- [filter(_:)](<asyncsequence/filter(__)-435af.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [AsyncFilterSequence](asyncfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy a given predicate.
- [filter(_:)](<asyncsequence/filter(__)-2cc0l.md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md) — An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given error-throwing predicate.
