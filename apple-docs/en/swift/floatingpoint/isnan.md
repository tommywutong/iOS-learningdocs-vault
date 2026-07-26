---
title: isNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/isnan
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/isnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/isnan.json'
content_hash: 'sha256:ee745ceb6a64c637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isNaN

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is NaN (“not a number”).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

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
