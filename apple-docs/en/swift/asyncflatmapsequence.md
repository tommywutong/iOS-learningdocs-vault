---
title: AsyncFlatMapSequence
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncflatmapsequence
source_url: 'https://developer.apple.com/documentation/swift/asyncflatmapsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncflatmapsequence.json'
content_hash: 'sha256:932de163df732a7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AsyncFlatMapSequence

<sub>Structure</sub>

An asynchronous sequence that concatenates the results of calling a given transformation with each element of this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncFlatMapSequence<Base, SegmentOfResult> where Base : AsyncSequence, SegmentOfResult : AsyncSequence
```

## Relationships

- **Conforms To**: [AsyncSequence](asyncsequence.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Iterator](asyncflatmapsequence/iterator.md) — The iterator that produces elements of the flat map sequence.

### Type Aliases

- [Failure](asyncflatmapsequence/failure.md) — The type of error produced by this asynchronous sequence.

### Default Implementations

- [AsyncSequence Implementations](asyncflatmapsequence/asyncsequence-implementations.md)

## See Also

### Transforming a Sequence

- [map(_:)](<asyncsequence/map(__)-1q1k3.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [AsyncMapSequence](asyncmapsequence.md) — An asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [map(_:)](<asyncsequence/map(__)-70wgb.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [AsyncThrowingMapSequence](asyncthrowingmapsequence.md) — An asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [compactMap(_:)](<asyncsequence/compactmap(__)-gfdq.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [AsyncCompactMapSequence](asynccompactmapsequence.md) — An asynchronous sequence that maps a given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<asyncsequence/compactmap(__)-1f8zn.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md) — An asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md) — An asynchronous sequence that concatenates the results of calling a given error-throwing transformation with each element of this sequence.
- [reduce(_:_:)](<asyncsequence/reduce(____).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [reduce(into:_:)](<asyncsequence/reduce(into___).md>) — Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
