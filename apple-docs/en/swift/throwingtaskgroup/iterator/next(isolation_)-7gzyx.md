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
doc_path: '/documentation/swift/throwingtaskgroup/iterator/next(isolation:)-7gzyx'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/iterator/next(isolation:)-7gzyx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/iterator/next%28isolation%3A%29-7gzyx.json'
content_hash: 'sha256:7e97b688ae1bc600'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [ThrowingTaskGroup](../../throwingtaskgroup.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?
```
