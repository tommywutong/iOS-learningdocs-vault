---
title: 'rounded(rule:increment:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/currency/rounded(rule:increment:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency/rounded(rule:increment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/currency/rounded%28rule%3Aincrement%3A%29.json'
content_hash: 'sha256:9856ee85e60b7b06'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FloatingPointFormatStyle](../../floatingpointformatstyle.md) · [Currency](../currency.md)

# rounded(rule:increment:)

<sub>Instance Method</sub>

Modifies the format style to use the specified rounding rule and increment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rounded(rule: FloatingPointFormatStyle<Value>.Currency.Configuration.RoundingRule = .toNearestOrEven, increment: Double? = nil) -> FloatingPointFormatStyle<Value>.Currency
```

## Parameters

- `rule` — The rounding rule to apply to the format style.

- `increment` — A multiple by which the formatter rounds the fractional part. The formatter produces a value that’s an even multiple of this increment. If this parameter is `nil` (the default), the formatter doesn’t apply an increment.

## Return Value

A floating-point currency format style modified to use the specified rounding rule and increment.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [presentation(_:)](<presentation(__).md>) — Modifies the format style to use the specified presentation.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) — Configuration settings for formatting currency values.
