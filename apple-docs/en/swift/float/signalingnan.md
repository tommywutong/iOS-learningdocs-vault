---
title: signalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/signalingnan
source_url: 'https://developer.apple.com/documentation/swift/float/signalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/signalingnan.json'
content_hash: 'sha256:2764f0a47d8109cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# signalingNaN

<sub>Type Property</sub>

A signaling NaN (“not a number”).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var signalingNaN: Float { get }
```

## Discussion

The default IEEE 754 behavior of operations involving a signaling NaN is to raise the Invalid flag in the floating-point environment and return a quiet NaN.

Operations on types conforming to the `FloatingPoint` protocol should support this behavior, but they might also support other options. For example, it would be reasonable to implement alternative operations in which operating on a signaling NaN triggers a runtime error or results in a diagnostic for debugging purposes. Types that implement alternative behaviors for a signaling NaN must document the departure.

Other than these signaling operations, a signaling NaN behaves in the same manner as a quiet NaN.

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [zero](zero.md) — The zero value.
