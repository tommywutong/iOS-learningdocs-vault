---
title: 'init(_:rounding:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd8/init(_:rounding:)'
source_url: 'https://developer.apple.com/documentation/swift/simd8/init(_:rounding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/init%28_%3Arounding%3A%29.json'
content_hash: 'sha256:f90968cf0ada9f0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD8](../simd8.md)

# init(_:rounding:)

<sub>Initializer</sub>

Creates a new vector from the given vector, rounding the given vector’s of elements using the specified rounding rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Other>(_ other: SIMD8<Other>, rounding rule: FloatingPointRoundingRule = .towardZero) where Other : BinaryFloatingPoint, Other : SIMDScalar
```

## Parameters

- `other` — The vector to convert.

- `rule` — The round rule to use when converting elements of `other.` The default is `.towardZero`.
