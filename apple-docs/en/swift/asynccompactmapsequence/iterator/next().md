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
doc_path: /documentation/swift/asynccompactmapsequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asynccompactmapsequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynccompactmapsequence/iterator/next%28%29.json'
content_hash: 'sha256:539e699b245fa2a2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncCompactMapSequence](../../asynccompactmapsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the compact map sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> ElementOfResult?
```

## Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns `nil`. Otherwise, `next()` calls the transforming closure on the received element, returning it if the transform returns a non-`nil` value. If the transform returns `nil`, this method continues to wait for further elements until it gets one that transforms to a non-`nil` value.
