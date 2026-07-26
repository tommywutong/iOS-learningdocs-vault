---
title: isNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/isnan
source_url: 'https://developer.apple.com/documentation/swift/float80/isnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/isnan.json'
content_hash: 'sha256:b662cb072b17df7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isNaN

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is NaN (“not a number”).

<sub>macOS</sub>

```swift
var isNaN: Bool { get }
```

## Discussion

Because NaN is not equal to any value, including NaN, use this property instead of the equal-to operator (`==`) or not-equal-to operator (`!=`) to test whether a value is or is not NaN. For example:

```swift
let x = 0.0
let y = x * .infinity
// y is a NaN

// Comparing with the equal-to operator never returns 'true'
print(x == Double.nan)
// Prints "false"
print(y == Double.nan)
// Prints "false"

// Test with the 'isNaN' property instead
print(x.isNaN)
// Prints "false"
print(y.isNaN)
// Prints "true"
```

This property is `true` for both quiet and signaling NaNs.
