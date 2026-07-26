---
title: mutableSpan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/inlinearray/mutablespan
source_url: 'https://developer.apple.com/documentation/swift/inlinearray/mutablespan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray/mutablespan.json'
content_hash: 'sha256:65f2b250e10e1681'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [InlineArray](../inlinearray.md)

# mutableSpan

<sub>Instance Property</sub>

A mutable span over the elements of this array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableSpan: MutableSpan<Element> { mutating get }
```

## Return Value

A `MutableSpan` over the elements of this array.

## Discussion

> [!abstract] Complexity
> O(1)
