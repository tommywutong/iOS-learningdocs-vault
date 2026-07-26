---
title: isFinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/isfinite
source_url: 'https://developer.apple.com/documentation/swift/float16/isfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/isfinite.json'
content_hash: 'sha256:28212b398de0f420'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# isFinite

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is finite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFinite: Bool { get }
```

## Discussion

All values other than NaN and infinity are considered finite, whether normal or subnormal.  For NaN, both `isFinite` and `isInfinite` are false.
