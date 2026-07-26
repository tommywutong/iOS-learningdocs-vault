---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd3/init(_:)-irjs'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(_:)-irjs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28_%3A%29-irjs.json'
content_hash: 'sha256:201e73fda262ce28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(_:)

<sub>Initializer</sub>

Returns a new vector from a Spatial rotation axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ rotationAxis: RotationAxis3DFloat)
```

## Discussion

Values rounded to a representable value, if necessary.

> [!note] Note
> This function is provided as a convenience. All Spatial storage and calculations are single-precision.
