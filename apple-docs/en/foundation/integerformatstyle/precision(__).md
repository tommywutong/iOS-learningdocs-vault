---
title: 'precision(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/precision(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/precision(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/precision%28_%3A%29.json'
content_hash: 'sha256:0d29680fcb20acb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# precision(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified precision.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func precision(_ p: IntegerFormatStyle<Value>.Configuration.Precision) -> IntegerFormatStyle<Value>
```

## Parameters

- `p` — The precision to apply to the format style.

## Return Value

An integer format style modified to use the specified precision.

## Discussion

The [Precision](../numberformatstyleconfiguration/precision.md) type lets you specify a fixed number of digits to show for a number’s integer and fractional parts, although [IntegerFormatStyle](../integerformatstyle.md) only uses the former. You can also set a fixed number of significant digits.

The following example creates a default [IntegerFormatStyle](../integerformatstyle.md) for the `en_US` locale, and a second style that uses a maximum of four significant digits. It then applies each style to an array of integers. The formatting that the modified style applies truncates precision to `0` after the fourth most significant digit.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let precisionStyle = defaultStyle.precision(.significantDigits(1...4))
let nums = [123, 1234, 12345, 123456, 1234567]
let defaultNums = nums.map { defaultStyle.format($0) } // ["123", "1,234", "12,345", "123,456", "1,234,567"]
let precisionNums = nums.map { precisionStyle.format($0) } // ["123", "1,234", "12,340", "123,500", "1,235,000"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
