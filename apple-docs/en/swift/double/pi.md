---
title: pi
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/pi
source_url: 'https://developer.apple.com/documentation/swift/double/pi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/pi.json'
content_hash: 'sha256:47548c6c689b5aa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# pi

<sub>Type Property</sub>

The mathematical constant pi (π), approximately equal to 3.14159.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var pi: Double { get }
```

## Discussion

When measuring an angle in radians, π is equivalent to a half-turn.

This value is rounded toward zero to keep user computations with angles from inadvertently ending up in the wrong quadrant. A type that conforms to the `FloatingPoint` protocol provides the value for `pi` at its best possible precision.

```swift
print(Double.pi)
// Prints "3.14159265358979"
```

## See Also

### Accessing Numeric Constants

- [infinity](infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [zero](zero.md) — The zero value.
