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
doc_path: /documentation/swift/asyncthrowingmapsequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingmapsequence/iterator/next%28%29.json'
content_hash: 'sha256:973960c35ac6c71c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingMapSequence](../../asyncthrowingmapsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the map sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws -> Transformed?
```

## Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns nil. Otherwise, `next()` returns the result of calling the transforming closure on the received element. If calling the closure throws an error, the sequence ends and `next()` rethrows the error.
