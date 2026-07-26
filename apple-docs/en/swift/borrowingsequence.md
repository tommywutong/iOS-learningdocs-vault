---
title: BorrowingSequence
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/borrowingsequence
source_url: 'https://developer.apple.com/documentation/swift/borrowingsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/borrowingsequence.json'
content_hash: 'sha256:cf03e94e17fa252c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# BorrowingSequence

<sub>Protocol</sub>

A type that provides sequential, borrowing access to its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol BorrowingSequence<Element> : ~Copyable, ~Escapable
```

## Relationships

- **Conforming Types**: [InlineArray](inlinearray.md), [MutableRawSpan](mutablerawspan.md), [MutableSpan](mutablespan.md), [RawSpan](rawspan.md), [Span](span.md)

## Topics

### Associated Types

- [BorrowingIterator](borrowingsequence/borrowingiterator.md) — A type that provides the sequence’s iteration interface and encapsulates its iteration state. _(beta)_
- [Element](borrowingsequence/element.md) — A type representing the sequence’s elements. _(beta)_

### Instance Properties

- [underestimatedCount](borrowingsequence/underestimatedcount.md) — A value less than or equal to the number of elements in the sequence, calculated nondestructively. _(beta)_

### Instance Methods

- [makeBorrowingIterator()](<borrowingsequence/makeborrowingiterator().md>) — Returns a borrowing iterator over the elements of this sequence. _(beta)_

## See Also

### Manual Iteration

- [IteratorProtocol](iteratorprotocol.md) — A type that supplies the values of a sequence one at a time.
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md) — A type that provides borrowed access to the values of a borrowing sequence. _(beta)_
- [BorrowingIteratorAdapter](borrowingiteratoradapter.md) _(beta)_
