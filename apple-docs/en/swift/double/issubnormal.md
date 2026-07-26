---
title: isSubnormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/issubnormal
source_url: 'https://developer.apple.com/documentation/swift/double/issubnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/issubnormal.json'
content_hash: 'sha256:ca1afe0ad07bc8aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# isSubnormal

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is subnormal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSubnormal: Bool { get }
```

## Discussion

A _subnormal_ value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values don’t use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called _denormal_ or _denormalized_—these are different names for the same concept.

## See Also

### Querying a Double’s State

- [isZero](iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isFinite](isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isNormal](isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](floatingpointclass.md) — The classification of this value.
