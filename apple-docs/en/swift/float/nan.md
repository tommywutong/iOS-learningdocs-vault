---
title: nan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/nan
source_url: 'https://developer.apple.com/documentation/swift/float/nan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/nan.json'
content_hash: 'sha256:eb0b37e92154f32e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# nan

<sub>Type Property</sub>

A quiet NaN (“not a number”).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var nan: Float { get }
```

## Discussion

A NaN compares not equal, not greater than, and not less than every value, including itself. Passing a NaN to an operation generally results in NaN.

```swift
let x = 1.21
// x > Double.nan == false
// x < Double.nan == false
// x == Double.nan == false
```

Because a NaN always compares not equal to itself, to test whether a floating-point value is NaN, use its `isNaN` property instead of the equal-to operator (`==`). In the following example, `y` is NaN.

```swift
let y = x + Double.nan
print(y == Double.nan)
// Prints "false"
print(y.isNaN)
// Prints "true"
```

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [zero](zero.md) — The zero value.
