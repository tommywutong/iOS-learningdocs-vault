---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd3/init(_:)-6xfbj'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(_:)-6xfbj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28_%3A%29-6xfbj.json'
content_hash: 'sha256:a1ee3ae79e8ae485'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(_:)

<sub>Initializer</sub>

Returns a new vector from a Spatial point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ point: Point3D)
```

## Discussion

Values rounded to a representable value, if necessary.

> [!note] Note
> This function is provided as a convenience. All Spatial storage and calculations are double-precision.
