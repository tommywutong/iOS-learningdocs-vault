---
title: floatingPointClass
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/floatingpointclass
source_url: 'https://developer.apple.com/documentation/swift/double/floatingpointclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/floatingpointclass.json'
content_hash: 'sha256:3a6db68c75ccb52b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# floatingPointClass

<sub>Instance Property</sub>

The classification of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var floatingPointClass: FloatingPointClassification { get }
```

## Discussion

A value’s `floatingPointClass` property describes its “class” as described by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

### Querying a Double’s State

- [isZero](iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isFinite](isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isSignalingNaN](issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isNormal](isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isSubnormal](issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
