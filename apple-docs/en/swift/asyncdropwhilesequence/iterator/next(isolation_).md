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
doc_path: '/documentation/swift/asyncdropwhilesequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncdropwhilesequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdropwhilesequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:81a07736b98cadaf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncDropWhileSequence](../../asyncdropwhilesequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the drop-while sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncDropWhileSequence<Base>.Failure) -> Base.Element?
```

## Discussion

This iterator calls `next(isolation:)` on its base iterator and evaluates the result with the `predicate` closure. As long as the predicate returns `true`, this method returns `nil`. After the predicate returns `false`, for a value received from the base iterator, this method returns that value. After that, the iterator returns values received from its base iterator as-is, and never executes the predicate closure again.
