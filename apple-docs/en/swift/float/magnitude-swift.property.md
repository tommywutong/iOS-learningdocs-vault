---
title: magnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/magnitude-swift.property
source_url: 'https://developer.apple.com/documentation/swift/float/magnitude-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/magnitude-swift.property.json'
content_hash: 'sha256:f14e0ddb595fff5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# magnitude

<sub>Instance Property</sub>

The magnitude of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var magnitude: Float { get }
```

## Discussion

For any numeric value `x`, `x.magnitude` is the absolute value of `x`. You can use the `magnitude` property in operations that are simpler to implement in terms of unsigned values, such as printing the value of an integer, which is just printing a ‘-’ character in front of an absolute value.

```swift
let x = -200
// x.magnitude == 200
```

The global `abs(_:)` function provides more familiar syntax when you need to find an absolute value. In addition, because `abs(_:)` always returns a value of the same type, even in a generic context, using the function instead of the `magnitude` property is encouraged.

## See Also

### Finding the Sign and Magnitude

- [sign](sign.md) — The sign of the floating-point value.
- [Magnitude](magnitude-swift.typealias.md) — A type that can represent the absolute value of any possible value of the conforming type.
