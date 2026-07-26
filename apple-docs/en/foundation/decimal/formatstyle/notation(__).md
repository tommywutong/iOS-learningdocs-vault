---
title: 'notation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/notation(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/notation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/notation%28_%3A%29.json'
content_hash: 'sha256:e9b233affc0631b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# notation(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notation(_ notation: Decimal.FormatStyle.Configuration.Notation) -> Decimal.FormatStyle
```

## Parameters

- `notation` — The notation to apply to the format style.

## Return Value

A decimal format style modified to use the specified notation.

## Discussion

The following example creates a default [FormatStyle](../formatstyle.md) for the `en_US` locale, and a second style that uses scientific notation style. It then applies each style to an array of decimal values.

```swift
let defaultStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let scientificStyle = defaultStyle.notation(.scientific)
let nums: [Decimal] = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]
let scientificNums = nums.map { scientificStyle.format($0) } // ["1.001E2", "1.0002E3", "1.00003E4", "1.000004E5", "1E6"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
