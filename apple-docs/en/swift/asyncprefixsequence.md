---
title: AsyncPrefixSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncprefixsequence
source_url: 'https://developer.apple.com/documentation/swift/asyncprefixsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncprefixsequence.json'
content_hash: 'sha256:815bd7ccf7d55890'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncPrefixSequence

<sub>Structure</sub>

An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncPrefixSequence<Base> where Base : AsyncSequence
```

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Iterator](asyncprefixsequence/iterator.md) — The iterator that produces elements of the prefix sequence.

### Type Aliases

- [Failure](asyncprefixsequence/failure.md) — The type of the error that can be produced by the sequence.

### Default Implementations

- [AsyncSequence Implementations](asyncprefixsequence/asyncsequence-implementations.md)

## See Also

### Selecting Elements

- [prefix(_:)](<asyncsequence/prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [prefix(while:)](<asyncsequence/prefix(while_)-2xy95.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.
- [prefix(while:)](<asyncsequence/prefix(while_)-6yp5n.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
