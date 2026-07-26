---
title: 'decimalSeparator(strategy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/currency/decimalseparator(strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency/decimalseparator(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/currency/decimalseparator%28strategy%3A%29.json'
content_hash: 'sha256:99c383f33cc55a7e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FloatingPointFormatStyle](../../floatingpointformatstyle.md) · [Currency](../currency.md)

# decimalSeparator(strategy:)

<sub>Instance Method</sub>

Modifies the format style to use the specified decimal separator display strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency
```

## Parameters

- `strategy` — The decimal separator display strategy to apply to the format style.

## Return Value

A floating-point currency format style modified to use the specified decimal separator display strategy.

## See Also

### Customizing style behavior

- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [presentation(_:)](<presentation(__).md>) — Modifies the format style to use the specified presentation.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) — Configuration settings for formatting currency values.
