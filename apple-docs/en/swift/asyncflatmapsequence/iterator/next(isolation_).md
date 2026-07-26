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
doc_path: '/documentation/swift/asyncflatmapsequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncflatmapsequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncflatmapsequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:9f30c1387c60f469'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncFlatMapSequence](../../asyncflatmapsequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the flat map sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncFlatMapSequence<Base, SegmentOfResult>.Failure) -> SegmentOfResult.Element?
```

## Discussion

This iterator calls `next(isolation:)` on its base iterator; if this call returns `nil`, `next(isolation:)` returns `nil`. Otherwise, `next(isolation:)` calls the transforming closure on the received element, takes the resulting asynchronous sequence, and creates an asynchronous iterator from it.  `next(isolation:)` then consumes values from this iterator until it terminates.  At this point, `next(isolation:)` is ready to receive the next value from the base sequence.
