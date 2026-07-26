---
title: leastNonzeroMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/leastnonzeromagnitude
source_url: 'https://developer.apple.com/documentation/swift/double/leastnonzeromagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/leastnonzeromagnitude.json'
content_hash: 'sha256:62b8d76ff8fb921b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# leastNonzeroMagnitude

<sub>Type Property</sub>

The least positive number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var leastNonzeroMagnitude: Double { get }
```

## Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [zero](zero.md) — The zero value.
