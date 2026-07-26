---
title: sign
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/sign
source_url: 'https://developer.apple.com/documentation/swift/float80/sign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/sign.json'
content_hash: 'sha256:8141fa88dd439e20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# sign

<sub>Instance Property</sub>

The sign of the floating-point value.

<sub>macOS</sub>

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
