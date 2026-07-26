---
title: isSignalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/issignalingnan
source_url: 'https://developer.apple.com/documentation/swift/float/issignalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/issignalingnan.json'
content_hash: 'sha256:0e8adbbaea4765d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# isSignalingNaN

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is a signaling NaN.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSignalingNaN: Bool { get }
```

## Discussion

Signaling NaNs typically raise the Invalid flag when used in general computing operations.

## See Also

### Querying a Float’s State

- [isZero](iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [isFinite](isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isNormal](isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isSubnormal](issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [floatingPointClass](floatingpointclass.md) — The classification of this value.
