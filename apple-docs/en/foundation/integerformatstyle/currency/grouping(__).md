---
title: 'grouping(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/currency/grouping(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/currency/grouping(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/currency/grouping%28_%3A%29.json'
content_hash: 'sha256:ddb87dc70d5a6eb9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Currency](../currency.md)

# grouping(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified grouping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func grouping(_ group: IntegerFormatStyle<Value>.Currency.Configuration.Grouping) -> IntegerFormatStyle<Value>.Currency
```

## Parameters

- `group` — The grouping to apply to the format style.

## Return Value

An integer currency format style modified to use the specified grouping.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [presentation(_:)](<presentation(__).md>) — Modifies the format style to use the specified presentation.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) — Configuration settings for formatting currency values.
