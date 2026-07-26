---
title: Element
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/borrowingsequence/element
source_url: 'https://developer.apple.com/documentation/swift/borrowingsequence/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/borrowingsequence/element.json'
content_hash: 'sha256:b8890324be0c8ac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BorrowingSequence](../borrowingsequence.md)

# Element

<sub>Associated Type</sub>

A type representing the sequence’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Element : ~Copyable where Self.Element == Self.BorrowingIterator.Element
```
