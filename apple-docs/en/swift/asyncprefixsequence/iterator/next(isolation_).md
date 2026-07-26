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
doc_path: '/documentation/swift/asyncprefixsequence/iterator/next(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncprefixsequence/iterator/next(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncprefixsequence/iterator/next%28isolation%3A%29.json'
content_hash: 'sha256:a66303125d57a702'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncPrefixSequence](../../asyncprefixsequence.md) · [Iterator](../iterator.md)

# next(isolation:)

<sub>Instance Method</sub>

Produces the next element in the prefix sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncPrefixSequence<Base>.Failure) -> Base.Element?
```

## Discussion

Until reaching the number of elements to include, this iterator calls `next(isolation:)` on its base iterator and passes through the result. After reaching the maximum number of elements, subsequent calls to `next(isolation:)` return `nil`.
