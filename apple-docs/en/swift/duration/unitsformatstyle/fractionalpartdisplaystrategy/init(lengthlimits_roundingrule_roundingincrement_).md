---
title: 'init(lengthLimits:roundingRule:roundingIncrement:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/init(lengthlimits:roundingrule:roundingincrement:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/init(lengthlimits:roundingrule:roundingincrement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/init%28lengthlimits%3Aroundingrule%3Aroundingincrement%3A%29.json'
content_hash: 'sha256:e977829ee9426bc6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [FractionalPartDisplayStrategy](../fractionalpartdisplaystrategy.md)

# init(lengthLimits:roundingRule:roundingIncrement:)

<sub>Initializer</sub>

Creates a fractional part display strategy that uses the provided behaviors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Range>(lengthLimits: Range, roundingRule: FloatingPointRoundingRule = .toNearestOrEven, roundingIncrement: Double? = nil) where Range : RangeExpression, Range.Bound == Int
```

## Parameters

- `lengthLimits` — The maximum string length of the fractional part.

- `roundingRule` — A rule for rounding fractional values up or down. Defaults to [FloatingPointRoundingRule.toNearestOrEven](../../../floatingpointroundingrule/tonearestoreven.md).

- `roundingIncrement` — A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is `nil` (the default), the formatter doesn’t apply an increment. This value is only meaningful when the combination of allowed units, rounding rule, and formatting strategy requires expressing a unit with a fractional part. For example, a formatter that only allows minutes and uses a strategy with a length of `2` and default rounding rule formats 40 seconds as `0.67 minutes`. With a `roundingIncrement` of `0.05`, the formatter formats this value as `0.65 minutes` instead.
