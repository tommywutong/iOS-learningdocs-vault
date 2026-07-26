---
title: nextSpan()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/borrowingiteratorprotocol/nextspan()
source_url: 'https://developer.apple.com/documentation/swift/borrowingiteratorprotocol/nextspan()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/borrowingiteratorprotocol/nextspan%28%29.json'
content_hash: 'sha256:bcb4260ae3637de4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BorrowingIteratorProtocol](../borrowingiteratorprotocol.md)

# nextSpan()

<sub>Instance Method</sub>

Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nextSpan() -> Span<Self.Element>
```
