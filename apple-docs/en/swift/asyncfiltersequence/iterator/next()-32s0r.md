---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncfiltersequence/iterator/next()-32s0r
source_url: 'https://developer.apple.com/documentation/swift/asyncfiltersequence/iterator/next()-32s0r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncfiltersequence/iterator/next%28%29-32s0r.json'
content_hash: 'sha256:20e708f6a664a0cd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncFilterSequence](../../asyncfiltersequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws(Self.Failure) -> Self.Element?
```
