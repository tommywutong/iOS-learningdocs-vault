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
doc_path: '/documentation/swift/asyncmapsequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncmapsequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncmapsequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:207373268cf10e4f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncMapSequence](../../asyncmapsequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the map sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncMapSequence<Base, Transformed>.Failure) -> Transformed?
```

## Discussion

This iterator calls `next(isolation:)` on its base iterator; if this call returns `nil`, `next(isolation:)` returns `nil`. Otherwise, `next(isolation:)` returns the result of calling the transforming closure on the received element.
