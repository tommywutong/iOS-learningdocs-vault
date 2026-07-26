---
title: 'presentation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/currency/presentation(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency/presentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/currency/presentation%28_%3A%29.json'
content_hash: 'sha256:be68843a91d4c127'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Decimal](../../../decimal.md) · [FormatStyle](../../formatstyle.md) · [Currency](../currency.md)

# presentation(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func presentation(_ p: Decimal.FormatStyle.Currency.Configuration.Presentation) -> Decimal.FormatStyle.Currency
```

## Parameters

- `p` — A currency presentation value, such as [isoCode](../../../currencyformatstyleconfiguration/presentation/isocode.md) or [fullName](../../../currencyformatstyleconfiguration/presentation/fullname.md).

## Return Value

A decimal currency format style modified to use the specified presentation.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [CurrencyFormatStyleConfiguration](../../../currencyformatstyleconfiguration.md) — Configuration settings for formatting currency values.
