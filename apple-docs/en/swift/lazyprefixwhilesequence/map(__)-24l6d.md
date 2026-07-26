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
doc_path: '/documentation/swift/lazyprefixwhilesequence/map(_:)-24l6d'
source_url: 'https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/map(_:)-24l6d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyprefixwhilesequence/map%28_%3A%29-24l6d.json'
content_hash: 'sha256:99e956346832ff1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyPrefixWhileSequence](../lazyprefixwhilesequence.md)

# map(_:)

<sub>Instance Method</sub>

Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<U>(_ transform: @escaping (Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>
```
