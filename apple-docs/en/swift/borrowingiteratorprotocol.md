---
title: BorrowingIteratorProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/borrowingiteratorprotocol
source_url: 'https://developer.apple.com/documentation/swift/borrowingiteratorprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/borrowingiteratorprotocol.json'
content_hash: 'sha256:13d16e1837beae99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# BorrowingIteratorProtocol

<sub>Protocol</sub>

A type that provides borrowed access to the values of a borrowing sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol BorrowingIteratorProtocol<Element> : ~Copyable, ~Escapable
```

## Relationships

- **Conforming Types**: [BorrowingIteratorAdapter](borrowingiteratoradapter.md), [SpanIterator](spaniterator.md)

## Topics

### Associated Types

- [Element](borrowingiteratorprotocol/element.md) _(beta)_

### Instance Methods

- [nextSpan()](<borrowingiteratorprotocol/nextspan().md>) — Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum. _(beta)_
- [nextSpan(maximumCount:)](<borrowingiteratorprotocol/nextspan(maximumcount_).md>) — Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum. _(beta)_
- [skip(by:)](<borrowingiteratorprotocol/skip(by_).md>) — Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements. _(beta)_

## See Also

### Manual Iteration

- [IteratorProtocol](iteratorprotocol.md) — A type that supplies the values of a sequence one at a time.
- [BorrowingIteratorAdapter](borrowingiteratoradapter.md) _(beta)_
- [BorrowingSequence](borrowingsequence.md) — A type that provides sequential, borrowing access to its elements. _(beta)_
