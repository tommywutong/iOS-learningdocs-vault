---
title: magnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/magnitude-swift.property
source_url: 'https://developer.apple.com/documentation/swift/float80/magnitude-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/magnitude-swift.property.json'
content_hash: 'sha256:4da8ae9463a3476b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# magnitude

<sub>Instance Property</sub>

The magnitude of this value.

<sub>macOS</sub>

```swift
var magnitude: Float80 { get }
```

## Discussion

For any numeric value `x`, `x.magnitude` is the absolute value of `x`. You can use the `magnitude` property in operations that are simpler to implement in terms of unsigned values, such as printing the value of an integer, which is just printing a ‘-’ character in front of an absolute value.

```swift
let x = -200
// x.magnitude == 200
```

The global `abs(_:)` function provides more familiar syntax when you need to find an absolute value. In addition, because `abs(_:)` always returns a value of the same type, even in a generic context, using the function instead of the `magnitude` property is encouraged.
