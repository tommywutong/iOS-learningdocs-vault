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
doc_path: '/documentation/swift/asyncdropfirstsequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncdropfirstsequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdropfirstsequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:0c4b3869d27766c6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncDropFirstSequence](../../asyncdropfirstsequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the drop-first sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncDropFirstSequence<Base>.Failure) -> Base.Element?
```

## Discussion

Until reaching the number of elements to drop, this iterator calls `next(isolation:)` on its base iterator and discards the result. If the base iterator returns `nil`, indicating the end of the sequence, this iterator returns `nil`. After reaching the number of elements to drop, this iterator passes along the result of calling `next(isolation:)` on the base iterator.
