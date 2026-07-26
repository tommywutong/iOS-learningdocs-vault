---
title: 'interpolate(towards:amount:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/vectorarithmetic/interpolate(towards:amount:)'
source_url: 'https://developer.apple.com/documentation/swiftui/vectorarithmetic/interpolate(towards:amount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/vectorarithmetic/interpolate%28towards%3Aamount%3A%29.json'
content_hash: 'sha256:fda10032c6c6253f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VectorArithmetic](../vectorarithmetic.md)

# interpolate(towards:amount:)

<sub>Instance Method</sub>

Interpolates this value with `other` by the specified `amount`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) mutating func interpolate(towards other: Self, amount: Double)
```

## Discussion

This is equivalent to `self = self + (other - self) * amount`.

## See Also

### Manipulating values

- [magnitudeSquared](magnitudesquared.md) — Returns the dot-product of this vector arithmetic instance with itself.
- [scale(by:)](<scale(by_).md>) — Multiplies each component of this value by the given value.
- [scaled(by:)](<scaled(by_).md>) — Returns a value with each component of this value multiplied by the given value.
- [interpolated(towards:amount:)](<interpolated(towards_amount_).md>) — Returns this value interpolated with `other` by the specified `amount`.
