---
title: nextUp
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/nextup
source_url: 'https://developer.apple.com/documentation/swift/double/nextup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/nextup.json'
content_hash: 'sha256:c68e43ac3ed2f15a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# nextUp

<sub>Instance Property</sub>

The least representable value that compares greater than this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nextUp: Double { get }
```

## Discussion

For any finite value `x`, `x.nextUp` is greater than `x`. For `nan` or `infinity`, `x.nextUp` is `x` itself. The following special cases also apply:

- If `x` is `-infinity`, then `x.nextUp` is `-greatestFiniteMagnitude`.
- If `x` is `-leastNonzeroMagnitude`, then `x.nextUp` is `-0.0`.
- If `x` is zero, then `x.nextUp` is `leastNonzeroMagnitude`.
- If `x` is `greatestFiniteMagnitude`, then `x.nextUp` is `infinity`.

## See Also

### Querying a Double

- [ulp](ulp.md) — The unit in the last place of this value.
- [significand](significand.md) — The significand of the floating-point value.
- [exponent](exponent-swift.property.md) — The exponent of the floating-point value.
- [nextDown](nextdown.md) — The greatest representable value that compares less than this value.
- [binade](binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
