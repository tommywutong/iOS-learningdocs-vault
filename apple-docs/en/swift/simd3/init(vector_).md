---
title: 'init(vector:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd3/init(vector:)'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(vector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28vector%3A%29.json'
content_hash: 'sha256:0e3c2f673d5e4cb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(vector:)

<sub>Initializer</sub>

Returns a new vector from a Spatial point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(vector: Vector3D)
```

## Discussion

Values rounded to a representable value, if necessary.

> [!note] Note
> This function is provided as a convenience. All Spatial storage and calculations are double-precision.
