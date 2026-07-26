---
title: leastNormalMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/leastnormalmagnitude
source_url: 'https://developer.apple.com/documentation/swift/double/leastnormalmagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/leastnormalmagnitude.json'
content_hash: 'sha256:c86bef7dfabc4a8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# leastNormalMagnitude

<sub>Type Property</sub>

The least positive normal number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var leastNormalMagnitude: Double { get }
```

## Discussion

This value compares less than or equal to all positive normal numbers. There may be smaller positive numbers, but they are _subnormal_, meaning that they are represented with less precision than normal numbers.

This value corresponds to type-specific C macros such as `FLT_MIN` and `DBL_MIN`. The naming of those macros is slightly misleading, because subnormals, zeros, and negative numbers are smaller than this value.

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [zero](zero.md) — The zero value.
