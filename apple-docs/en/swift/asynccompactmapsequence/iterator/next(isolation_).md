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
doc_path: '/documentation/swift/asynccompactmapsequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asynccompactmapsequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynccompactmapsequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:cd1af52e558bcc5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncCompactMapSequence](../../asynccompactmapsequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the compact map sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncCompactMapSequence<Base, ElementOfResult>.Failure) -> ElementOfResult?
```

## Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns `nil`. Otherwise, `next()` calls the transforming closure on the received element, returning it if the transform returns a non-`nil` value. If the transform returns `nil`, this method continues to wait for further elements until it gets one that transforms to a non-`nil` value.
