---
title: 'decimalSeparator(strategy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/decimalseparator(strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/decimalseparator(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/decimalseparator%28strategy%3A%29.json'
content_hash: 'sha256:97fb3a4d07169873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# decimalSeparator(strategy:)

<sub>Instance Method</sub>

Modifies the format style to use the specified decimal separator display strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decimalSeparator(strategy: IntegerFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>
```

## Parameters

- `strategy` — The decimal separator display strategy to apply to the format style.

## Return Value

An integer format style modified to use the specified decimal separator display strategy.

## Discussion

The following example creates a default [IntegerFormatStyle](../integerformatstyle.md) for the `en_US` locale, and a second style that uses the [always](../numberformatstyleconfiguration/decimalseparatordisplaystrategy/always.md) strategy. It then applies each style to an array of integers. The formatting that the modified style applies adds a trailing decimal separator in all cases.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let alwaysStyle = defaultStyle.decimalSeparator(strategy: .always)
let nums = [100, 1000, 10000, 100000, 1000000]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100", "1,000", "10,000", "100,000", "1,000,000"]
let alwaysNums = nums.map { alwaysStyle.format($0) } // ["100.", "1,000.", "10,000.", "100,000.", "1,000,000."]
```

## See Also

### Customizing style behavior

- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
