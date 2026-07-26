---
title: magnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/numeric/magnitude-1v49u
source_url: 'https://developer.apple.com/documentation/swift/numeric/magnitude-1v49u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/numeric/magnitude-1v49u.json'
content_hash: 'sha256:65f400fd4be11600'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Numeric](../numeric.md)

# magnitude

<sub>Instance Property</sub>

The magnitude of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var magnitude: Self.Magnitude { get }
```

## Discussion

For any numeric value `x`, `x.magnitude` is the absolute value of `x`. You can use the `magnitude` property in operations that are simpler to implement in terms of unsigned values, such as printing the value of an integer, which is just printing a ‘-’ character in front of an absolute value.

```swift
let x = -200
// x.magnitude == 200
```

The global `abs(_:)` function provides more familiar syntax when you need to find an absolute value. In addition, because `abs(_:)` always returns a value of the same type, even in a generic context, using the function instead of the `magnitude` property is encouraged.

## Default Implementations

### Numeric Implementations

- [magnitude](magnitude-5ma51.md) — The magnitude of this value.
