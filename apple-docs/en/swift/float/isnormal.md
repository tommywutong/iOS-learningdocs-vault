---
title: isNormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/isnormal
source_url: 'https://developer.apple.com/documentation/swift/float/isnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/isnormal.json'
content_hash: 'sha256:2b7de03475f44232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# isNormal

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is normal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isNormal: Bool { get }
```

## Discussion

A _normal_ value is a finite number that uses the full precision available to values of a type. Zero is neither a normal nor a subnormal number.

## See Also

### Querying a Float’s State

- [isZero](iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isFinite](isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isSubnormal](issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](floatingpointclass.md) — The classification of this value.
