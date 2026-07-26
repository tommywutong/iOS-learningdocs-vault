---
title: greatestFiniteMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/greatestfinitemagnitude
source_url: 'https://developer.apple.com/documentation/swift/float/greatestfinitemagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/greatestfinitemagnitude.json'
content_hash: 'sha256:b6174640b62c045a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# greatestFiniteMagnitude

<sub>Type Property</sub>

The greatest finite number representable by this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var greatestFiniteMagnitude: Float { get }
```

## Discussion

This value compares greater than or equal to all finite numbers, but less than `infinity`.

This value corresponds to type-specific C macros such as `FLT_MAX` and `DBL_MAX`. The naming of those macros is slightly misleading, because `infinity` is greater than this value.

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](infinity.md) — Positive infinity.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [zero](zero.md) — The zero value.
