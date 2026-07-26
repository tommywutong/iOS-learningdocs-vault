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
doc_path: /documentation/swift/asyncdropfirstsequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncdropfirstsequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdropfirstsequence/iterator/next%28%29.json'
content_hash: 'sha256:23fe829fdb21443d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncDropFirstSequence](../../asyncdropfirstsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the drop-first sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> Base.Element?
```

## Discussion

Until reaching the number of elements to drop, this iterator calls `next()` on its base iterator and discards the result. If the base iterator returns `nil`, indicating the end of the sequence, this iterator returns `nil`. After reaching the number of elements to drop, this iterator passes along the result of calling `next()` on the base iterator.
