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
doc_path: /documentation/swift/asyncprefixsequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/asyncprefixsequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncprefixsequence/iterator/next%28%29.json'
content_hash: 'sha256:a750a3b33f045048'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncPrefixSequence](../../asyncprefixsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Produces the next element in the prefix sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async rethrows -> Base.Element?
```

## Discussion

Until reaching the number of elements to include, this iterator calls `next()` on its base iterator and passes through the result. After reaching the maximum number of elements, subsequent calls to `next()` return `nil`.
