---
title: BorrowingIteratorAdapter
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/borrowingiteratoradapter
source_url: 'https://developer.apple.com/documentation/swift/borrowingiteratoradapter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/borrowingiteratoradapter.json'
content_hash: 'sha256:537c9d37d1fb5dcf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# BorrowingIteratorAdapter

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct BorrowingIteratorAdapter<Iterator> where Iterator : IteratorProtocol
```

## Relationships

- **Conforms To**: [BorrowingIteratorProtocol](borrowingiteratorprotocol.md)

## Topics

### Initializers

- [init(iterator:)](<borrowingiteratoradapter/init(iterator_).md>) _(beta)_

### Instance Methods

- [nextSpan(maximumCount:)](<borrowingiteratoradapter/nextspan(maximumcount_).md>) — Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum. _(beta)_

### Type Aliases

- [Element](borrowingiteratoradapter/element.md) _(beta)_

### Default Implementations

- [BorrowingIteratorProtocol Implementations](borrowingiteratoradapter/borrowingiteratorprotocol-implementations.md)

## See Also

### Manual Iteration

- [IteratorProtocol](iteratorprotocol.md) — A type that supplies the values of a sequence one at a time.
- [BorrowingIteratorProtocol](borrowingiteratorprotocol.md) — A type that provides borrowed access to the values of a borrowing sequence. _(beta)_
- [BorrowingSequence](borrowingsequence.md) — A type that provides sequential, borrowing access to its elements. _(beta)_
