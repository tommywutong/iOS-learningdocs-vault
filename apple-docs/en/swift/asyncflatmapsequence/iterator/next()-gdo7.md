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
doc_path: /documentation/swift/asyncflatmapsequence/iterator/next()-gdo7
source_url: 'https://developer.apple.com/documentation/swift/asyncflatmapsequence/iterator/next()-gdo7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncflatmapsequence/iterator/next%28%29-gdo7.json'
content_hash: 'sha256:f3ce7a116566b49b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [AsyncFlatMapSequence](../../asyncflatmapsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() async throws(Self.Failure) -> Self.Element?
```
