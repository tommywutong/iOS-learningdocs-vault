---
title: AsyncThrowingFlatMapSequence.Element
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingflatmapsequence/element
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingflatmapsequence/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingflatmapsequence/element.json'
content_hash: 'sha256:7e43a10dbe3a5faf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingFlatMapSequence](../asyncthrowingflatmapsequence.md)

# AsyncThrowingFlatMapSequence.Element

<sub>Type Alias</sub>

The type of element produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Element = SegmentOfResult.Element
```

## Discussion

The flat map sequence produces the type of element in the asynchronous sequence produced by the `transform` closure.
