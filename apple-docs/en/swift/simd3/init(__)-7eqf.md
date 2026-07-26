---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd3/init(_:)-7eqf'
source_url: 'https://developer.apple.com/documentation/swift/simd3/init(_:)-7eqf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd3/init%28_%3A%29-7eqf.json'
content_hash: 'sha256:dd2c783651bfc95f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD3](../simd3.md)

# init(_:)

<sub>Initializer</sub>

Creates a new vector from the given vector of floating-point values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Other>(_ other: SIMD3<Other>) where Other : BinaryFloatingPoint, Other : SIMDScalar
```

## Parameters

- `other` — The vector to convert.
