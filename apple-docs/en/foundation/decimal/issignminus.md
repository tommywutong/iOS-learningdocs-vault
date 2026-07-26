---
title: isSignMinus
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal/issignminus
source_url: 'https://developer.apple.com/documentation/foundation/decimal/issignminus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/issignminus.json'
content_hash: 'sha256:9296455e6b17e655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# isSignMinus

<sub>Instance Property</sub>

A Boolean value indicating whether this decimal has a negative sign.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSignMinus: Bool { get }
```

## Discussion

This property is `true` when the value is negative or `-0.0`; otherwise, `false`.

## See Also

### Getting a decimal’s characteristics

- [sign](sign.md) — The sign of the decimal.
- [exponent](exponent.md) — The exponent of the decimal.
- [significand](significand.md) — The significand of the decimal.
- [magnitude](magnitude.md) — The magnitude of this decimal.
- [floatingPointClass](floatingpointclass.md) — The IEEE 754 class of this type.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the representation of this decimal is canonical.
- [isFinite](isfinite.md) — A Boolean value indicating whether this decimal is zero, subnormal, or normal (not infinity or NaN).
- [isInfinite](isinfinite.md) — A Boolean value indicating whether this decimal is infinity.
- [isNaN](isnan.md) — A Boolean value indicating whether this decimal is NaN.
- [isNormal](isnormal.md) — A Boolean value indicating whether this decimal is normal (not zero, subnormal, infinity, or NaN).
- [isSignaling](issignaling.md) — A Boolean value indicating whether this decimal is a signaling NaN.``
- [isSignalingNaN](issignalingnan.md) — A Boolean value indicating whether this decimal is a signaling NaN.
- [isSubnormal](issubnormal.md) — A Boolean value indicating whether this decimal is subnormal.
- [isZero](iszero.md) — A Boolean value indicating whether this value is zero.
- [nextDown](nextdown.md) — The greatest representable value that is less than this decimal.
