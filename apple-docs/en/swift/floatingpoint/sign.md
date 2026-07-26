---
title: sign
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/sign
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/sign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/sign.json'
content_hash: 'sha256:edabb1062e96342c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# sign

<sub>Instance Property</sub>

The sign of the floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sign: FloatingPointSign { get }
```

## Discussion

The `sign` property is `.minus` if the value’s signbit is set, and `.plus` otherwise. For example:

```swift
let x = -33.375
// x.sign == .minus
```

Don’t use this property to check whether a floating point value is negative. For a value `x`, the comparison `x.sign == .minus` is not necessarily the same as `x < 0`. In particular, `x.sign == .minus` if `x` is -0, and while `x < 0` is always `false` if `x` is NaN, `x.sign` could be either `.plus` or `.minus`.
