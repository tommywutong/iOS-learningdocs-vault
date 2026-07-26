---
title: 'precision(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/currency/precision(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency/precision(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/currency/precision%28_%3A%29.json'
content_hash: 'sha256:15ca59b246d1ecf8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Decimal](../../../decimal.md) · [FormatStyle](../../formatstyle.md) · [Currency](../currency.md)

# precision(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified precision.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func precision(_ p: Decimal.FormatStyle.Currency.Configuration.Precision) -> Decimal.FormatStyle.Currency
```

## Parameters

- `p` — The precision to apply to the format style.

## Return Value

A decimal format style modified to use the specified precision.

## Discussion

The [Precision](../../../numberformatstyleconfiguration/precision.md) type lets you specify a fixed number of digits to show for a number’s integer and fractional part. You can also set a fixed number of significant digits.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [presentation(_:)](<presentation(__).md>) — Modifies the format style to use the specified presentation.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [CurrencyFormatStyleConfiguration](../../../currencyformatstyleconfiguration.md) — Configuration settings for formatting currency values.
