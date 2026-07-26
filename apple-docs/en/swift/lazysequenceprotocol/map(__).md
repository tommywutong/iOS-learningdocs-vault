---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazysequenceprotocol/map(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazysequenceprotocol/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequenceprotocol/map%28_%3A%29.json'
content_hash: 'sha256:0edc42b1a5e8d02d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequenceProtocol](../lazysequenceprotocol.md)

# map(_:)

<sub>Instance Method</sub>

Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<U>(_ transform: @escaping (Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>
```
