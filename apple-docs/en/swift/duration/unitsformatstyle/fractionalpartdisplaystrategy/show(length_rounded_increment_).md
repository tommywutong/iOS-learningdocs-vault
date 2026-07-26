---
title: 'show(length:rounded:increment:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/show(length:rounded:increment:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/show(length:rounded:increment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/show%28length%3Arounded%3Aincrement%3A%29.json'
content_hash: 'sha256:ce02cec343458c0e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [FractionalPartDisplayStrategy](../fractionalpartdisplaystrategy.md)

# show(length:rounded:increment:)

<sub>Type Method</sub>

Creates a display strategy that shows a fractional part.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func show(length: Int, rounded rule: FloatingPointRoundingRule = .toNearestOrEven, increment: Double? = nil) -> Duration.UnitsFormatStyle.FractionalPartDisplayStrategy
```

## Parameters

- `length` — The maximum string length of the fractional part.

- `rule` — A rule for rounding fractional values up or down. Defaults to [FloatingPointRoundingRule.toNearestOrEven](../../../floatingpointroundingrule/tonearestoreven.md).

- `increment` — A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is `nil` (the default), the formatter doesn’t apply an increment. This value is only meaningful when the combination of allowed units, rounding rule, and formatting strategy requires expressing a unit with a fractional part. For example, a formatter that only allows minutes and uses a strategy with a length of `2` and default rounding rule formats 40 seconds as `0.67 minutes`. With a `increment` of `0.05`, the formatter formats this value as `0.65 minutes` instead.

## See Also

### Using common strategies

- [hide](hide.md) — A display strategy that hides any fractional part by truncating it.
- [hide(rounded:)](<hide(rounded_).md>) — Creates a display strategy that hides any fractional part rounding the unit value.
