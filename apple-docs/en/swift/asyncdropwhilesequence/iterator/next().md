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
doc_path: /documentation/swift/asyncdropwhilesequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncdropwhilesequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdropwhilesequence/iterator/next%28%29.json'
content_hash: 'sha256:80cdb7eb0a3145af'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncDropWhileSequence](../../asyncdropwhilesequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the drop-while sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> Base.Element?
```

## Discussion

This iterator calls `next()` on its base iterator and evaluates the result with the `predicate` closure. As long as the predicate returns `true`, this method returns `nil`. After the predicate returns `false`, for a value received from the base iterator, this method returns that value. After that, the iterator returns values received from its base iterator as-is, and never executes the predicate closure again.
