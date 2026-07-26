---
title: AsyncPrefixWhileSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncprefixwhilesequence
source_url: 'https://developer.apple.com/documentation/swift/asyncprefixwhilesequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncprefixwhilesequence.json'
content_hash: 'sha256:3049e9885f2eeb53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncPrefixWhileSequence

<sub>Structure</sub>

An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncPrefixWhileSequence<Base> where Base : AsyncSequence
```

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Iterator](asyncprefixwhilesequence/iterator.md) — The iterator that produces elements of the prefix-while sequence.

### Type Aliases

- [Failure](asyncprefixwhilesequence/failure.md) — The type of the error that can be produced by the sequence.

### Default Implementations

- [AsyncSequence Implementations](asyncprefixwhilesequence/asyncsequence-implementations.md)

## See Also

### Selecting Elements

- [prefix(_:)](<asyncsequence/prefix(__).md>) — Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [AsyncPrefixSequence](asyncprefixsequence.md) — An asynchronous sequence, up to a specified maximum length, containing the initial elements of a base asynchronous sequence.
- [prefix(while:)](<asyncsequence/prefix(while_)-2xy95.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
- [prefix(while:)](<asyncsequence/prefix(while_)-6yp5n.md>) — Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
- [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md) — An asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given error-throwing predicate.
