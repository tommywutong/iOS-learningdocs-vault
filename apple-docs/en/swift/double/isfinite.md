---
title: isFinite
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/isfinite
source_url: 'https://developer.apple.com/documentation/swift/double/isfinite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/isfinite.json'
content_hash: 'sha256:78637516b581b4cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# isFinite

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is finite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFinite: Bool { get }
```

## Discussion

All values other than NaN and infinity are considered finite, whether normal or subnormal.  For NaN, both `isFinite` and `isInfinite` are false.

## See Also

### Querying a Double’s State

- [isZero](iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isInfinite](isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isNormal](isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isSubnormal](issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](floatingpointclass.md) — The classification of this value.
