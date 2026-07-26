---
title: isInfinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/isinfinite
source_url: 'https://developer.apple.com/documentation/swift/float16/isinfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/isinfinite.json'
content_hash: 'sha256:bdf705bc40e5ae6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# isInfinite

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is infinite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isInfinite: Bool { get }
```

## Discussion

For NaN, both `isFinite` and `isInfinite` are false.
