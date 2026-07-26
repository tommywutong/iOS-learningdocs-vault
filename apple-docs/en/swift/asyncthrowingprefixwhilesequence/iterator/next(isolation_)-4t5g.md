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
doc_path: '/documentation/swift/asyncthrowingprefixwhilesequence/iterator/next(isolation:)-4t5g'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence/iterator/next(isolation:)-4t5g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingprefixwhilesequence/iterator/next%28isolation%3A%29-4t5g.json'
content_hash: 'sha256:a9a1df221d8c5715'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncThrowingPrefixWhileSequence](../../asyncthrowingprefixwhilesequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?
```
