---
title: ulpOfOne
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/ulpofone
source_url: 'https://developer.apple.com/documentation/swift/double/ulpofone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/ulpofone.json'
content_hash: 'sha256:c5eb290a465fc002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# ulpOfOne

<sub>Type Property</sub>

The unit in the last place of 1.0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var ulpOfOne: Double { get }
```

## Discussion

The positive difference between 1.0 and the next greater representable number. The `ulpOfOne` constant corresponds to the C macros `FLT_EPSILON`, `DBL_EPSILON`, and others with a similar purpose.

## See Also

### Accessing Numeric Constants

- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [infinity](infinity.md) — Positive infinity.
- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [zero](zero.md) — The zero value.
