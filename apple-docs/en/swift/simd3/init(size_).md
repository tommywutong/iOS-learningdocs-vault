---
title: 'init(size:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd3/init(size:)'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28size%3A%29.json'
content_hash: 'sha256:b60ed97571ccc6c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(size:)

<sub>Initializer</sub>

Returns a new vector from a Spatial size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(size: Size3D)
```

## Discussion

Values rounded to a representable value, if necessary.

> [!note] Note
> This function is provided as a convenience. All Spatial storage and calculations are double-precision.
