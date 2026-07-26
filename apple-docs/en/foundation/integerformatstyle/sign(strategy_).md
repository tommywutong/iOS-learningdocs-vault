---
title: 'sign(strategy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/sign(strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/sign(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/sign%28strategy%3A%29.json'
content_hash: 'sha256:c1ba913eb7c87498'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# sign(strategy:)

<sub>Instance Method</sub>

Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sign(strategy: IntegerFormatStyle<Value>.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>
```

## Parameters

- `strategy` — The sign display strategy to apply to the format style, such as [automatic](../numberformatstyleconfiguration/signdisplaystrategy/automatic.md) or [never](../numberformatstyleconfiguration/signdisplaystrategy/never.md).

## Return Value

An integer format style modified to use the specified sign display strategy.

## Discussion

The following example creates a default [IntegerFormatStyle](../integerformatstyle.md) for the `en_US` locale, and a second style that displays a sign for all values except zero. It then applies each style to an array of integers. The formatting that the modified style applies adds the negative (`-`) or positive (`+`) sign to all the numbers.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let alwaysStyle = defaultStyle.sign(strategy: .always(includingZero: false))
let nums = [-2, -1, 0, 1, 2]
let defaultNums = nums.map { defaultStyle.format($0) } // ["-2", "-1", "0", "1", "2"]
let alwaysNums = nums.map { alwaysStyle.format($0) } // ["-2", "-1", "0", "+1", "+2"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
