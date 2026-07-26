---
title: 'rounded(rule:increment:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/rounded(rule:increment:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/rounded(rule:increment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/rounded%28rule%3Aincrement%3A%29.json'
content_hash: 'sha256:ba54ef5473cfa33d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FloatingPointFormatStyle](../floatingpointformatstyle.md)

# rounded(rule:increment:)

<sub>Instance Method</sub>

Modifies the format style to use the specified rounding rule and increment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rounded(rule: FloatingPointFormatStyle<Value>.Configuration.RoundingRule = .toNearestOrEven, increment: Double? = nil) -> FloatingPointFormatStyle<Value>
```

## Parameters

- `rule` — The rounding rule to apply to the format style.

- `increment` — A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is `nil` (the default), the formatter doesn’t apply an increment.

## Return Value

A floating-point format style modified to use the specified rounding rule and increment.

## Discussion

The following example creates a default [FloatingPointFormatStyle](../floatingpointformatstyle.md) for the `en_US` locale, and modifies its rounding behavior. It uses the [FloatingPointRoundingRule.up](../../swift/floatingpointroundingrule/up.md) rounding rule, and an increment of `0.25`. It then applies this style to an array of floating-point values, rounding them to the next greater increment of 0.25.

```swift
let roundedStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
    .rounded(rule: .up, increment: 0.25)
let nums = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
let roundedNums = nums.map { roundedStyle.format($0) } // ["1.00", "1.25", "1.25", "1.50", "1.50", "1.50", "1.75"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
