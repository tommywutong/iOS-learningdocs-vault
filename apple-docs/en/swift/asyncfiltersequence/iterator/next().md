---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncfiltersequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence/iterator/next%28%29.json'
content_hash: 'sha256:c03925aca90964aa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncFilterSequence](../../asyncfiltersequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the filter sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> Base.Element?
```

## Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns nil. Otherwise, `next()` evaluates the result with the `predicate` closure. If the closure returns `true`, `next()` returns the received element; otherwise it awaits the next element from the base iterator.
