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
doc_path: '/documentation/foundation/integerformatstyle/rounded(rule:increment:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/rounded(rule:increment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/rounded%28rule%3Aincrement%3A%29.json'
content_hash: 'sha256:b6f3d15851717bf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# rounded(rule:increment:)

<sub>Instance Method</sub>

Modifies the format style to use the specified rounding rule and increment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rounded(rule: IntegerFormatStyle<Value>.Configuration.RoundingRule = .toNearestOrEven, increment: Int? = nil) -> IntegerFormatStyle<Value>
```

## Parameters

- `rule` — The rounding rule to apply to the format style.

- `increment` — A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is `nil` (the default), the formatter doesn’t apply an increment.

## Return Value

An integer format style modified to use the specified rounding rule and increment.

## Discussion

The following example creates a default [IntegerFormatStyle](../integerformatstyle.md) for the `en_US` locale, and a modified style that rounds integers to the nearest multiple of `100`. It then formats the value `1999` using these format styles.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let roundedStyle = defaultStyle.rounded(rule: .toNearestOrEven,
                                        increment: 100)
let num = 1999
let defaultNum = num.formatted(defaultStyle) // "1,999"
let roundedNum = num.formatted(roundedStyle) // "2,000"
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
