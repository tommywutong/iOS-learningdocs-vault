---
title: BorrowingIterator
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/borrowingsequence/borrowingiterator
source_url: 'https://developer.apple.com/documentation/swift/borrowingsequence/borrowingiterator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/borrowingsequence/borrowingiterator.json'
content_hash: 'sha256:337d7f1951b56fc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BorrowingSequence](../borrowingsequence.md)

# BorrowingIterator

<sub>Associated Type</sub>

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype BorrowingIterator : BorrowingIteratorProtocol, ~Copyable, ~Escapable
```
