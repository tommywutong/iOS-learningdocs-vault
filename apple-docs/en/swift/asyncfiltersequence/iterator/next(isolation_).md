---
title: 'next(isolation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncfiltersequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:000e5607ab2b9b46'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncFilterSequence](../../asyncfiltersequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the filter sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncFilterSequence<Base>.Failure) -> Base.Element?
```

## Discussion

This iterator calls `next(isolation:)` on its base iterator; if this call returns `nil`, `next(isolation:)` returns nil. Otherwise, `next(isolation:)` evaluates the result with the `predicate` closure. If the closure returns `true`, `next(isolation:)` returns the received element; otherwise it awaits the next element from the base iterator.
