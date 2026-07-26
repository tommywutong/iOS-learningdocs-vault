---
title: 'precision(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/precision(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/precision(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/precision%28_%3A%29.json'
content_hash: 'sha256:c0b2331cdd7492f4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# precision(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified precision.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func precision(_ p: Decimal.FormatStyle.Configuration.Precision) -> Decimal.FormatStyle
```

## Parameters

- `p` — The precision to apply to the format style.

## Return Value

A decimal format style modified to use the specified precision.

## Discussion

The [Precision](../../numberformatstyleconfiguration/precision.md) type lets you specify fixed numbers of digits to show for a number’s integer and fractional parts. You can also set a fixed number of significant digits.

The following example creates a default [FormatStyle](../formatstyle.md) for the `en_US` locale, and a second style that uses a maximum of four significant digits. It then applies each style to an array of decimal values. The formatting applied by the modified style truncates precision to `0` after the fourth most-significant digit.

```swift
let defaultStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let precisionStyle = defaultStyle.precision(.significantDigits(1...4))
let nums: [Decimal] = [123.1, 1234.1, 12345.1, 123456.1, 1234567.1]
let defaultNums = nums.map { defaultStyle.format($0) } // ["123.1", "1,234.1", "12,345.1", "123,456.1", "1,234,567.1"]
let precisionNums = nums.map { precisionStyle.format($0) } // ["123.1", "1,234", "12,350", "123,500", "1,235,000"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
