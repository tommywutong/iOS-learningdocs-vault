---
title: SpanIterator
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/spaniterator
source_url: 'https://developer.apple.com/documentation/swift/spaniterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/spaniterator.json'
content_hash: 'sha256:d9ed98f17742944e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SpanIterator

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SpanIterator<Element> where Element : ~Copyable
```

## Relationships

- **Conforms To**: [BorrowingIteratorProtocol](borrowingiteratorprotocol.md)

## Topics

### Initializers

- [init(_:)](<spaniterator/init(__).md>) _(beta)_

### Instance Methods

- [nextSpan(maximumCount:)](<spaniterator/nextspan(maximumcount_).md>) — Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum. _(beta)_
- [skip(by:)](<spaniterator/skip(by_).md>) — Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements. _(beta)_

### Default Implementations

- [BorrowingIteratorProtocol Implementations](spaniterator/borrowingiteratorprotocol-implementations.md)

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
