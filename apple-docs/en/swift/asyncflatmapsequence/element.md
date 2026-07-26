---
title: AsyncFlatMapSequence.Element
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncflatmapsequence/element
source_url: 'https://developer.apple.com/documentation/swift/asyncflatmapsequence/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncflatmapsequence/element.json'
content_hash: 'sha256:e8ead44b0454f49e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncFlatMapSequence](../asyncflatmapsequence.md)

# AsyncFlatMapSequence.Element

<sub>Type Alias</sub>

The type of element produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Element = SegmentOfResult.Element
```

## Discussion

The flat map sequence produces the type of element in the asynchronous sequence produced by the `transform` closure.
