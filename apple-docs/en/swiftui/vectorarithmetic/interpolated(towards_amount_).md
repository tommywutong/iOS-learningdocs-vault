---
title: 'interpolated(towards:amount:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/vectorarithmetic/interpolated(towards:amount:)'
source_url: 'https://developer.apple.com/documentation/swiftui/vectorarithmetic/interpolated(towards:amount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/vectorarithmetic/interpolated%28towards%3Aamount%3A%29.json'
content_hash: 'sha256:ebc9a285634ea466'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VectorArithmetic](../vectorarithmetic.md)

# interpolated(towards:amount:)

<sub>Instance Method</sub>

Returns this value interpolated with `other` by the specified `amount`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) func interpolated(towards other: Self, amount: Double) -> Self
```

## Discussion

This result is equivalent to `self + (other - self) * amount`.

## See Also

### Manipulating values

- [magnitudeSquared](magnitudesquared.md) — Returns the dot-product of this vector arithmetic instance with itself.
- [scale(by:)](<scale(by_).md>) — Multiplies each component of this value by the given value.
- [scaled(by:)](<scaled(by_).md>) — Returns a value with each component of this value multiplied by the given value.
- [interpolate(towards:amount:)](<interpolate(towards_amount_).md>) — Interpolates this value with `other` by the specified `amount`.
