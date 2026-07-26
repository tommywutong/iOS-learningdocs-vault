---
title: mutableBytes
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mutablespan/mutablebytes-7cwoq
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/mutablebytes-7cwoq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/mutablebytes-7cwoq.json'
content_hash: 'sha256:eb77ab4677f56f9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# mutableBytes

<sub>Instance Property</sub>

Construct a mutable raw span over the memory represented by this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableBytes: MutableRawSpan { mutating get }
```

## Return Value

A `MutableRawSpan` over the memory represented by this span.

## Discussion

Mutating `self` through this property is unsafe because it is possible to mutate a byte so as to produce an invalid bit pattern in the corresponding instance of `Element`.
