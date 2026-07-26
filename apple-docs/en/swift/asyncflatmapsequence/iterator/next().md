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
doc_path: /documentation/swift/asyncflatmapsequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncflatmapsequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncflatmapsequence/iterator/next%28%29.json'
content_hash: 'sha256:435f08f32e8f0609'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncFlatMapSequence](../../asyncflatmapsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the flat map sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> SegmentOfResult.Element?
```

## Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns `nil`. Otherwise, `next()` calls the transforming closure on the received element, takes the resulting asynchronous sequence, and creates an asynchronous iterator from it. `next()` then consumes values from this iterator until it terminates. At this point, `next()` is ready to receive the next value from the base sequence.
