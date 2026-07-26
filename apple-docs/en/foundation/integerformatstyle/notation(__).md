---
title: 'notation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/notation(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/notation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/notation%28_%3A%29.json'
content_hash: 'sha256:d23a7e7737e8272e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# notation(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified notation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func notation(_ notation: IntegerFormatStyle<Value>.Configuration.Notation) -> IntegerFormatStyle<Value>
```

## Parameters

- `notation` — The notation to apply to the format style.

## Return Value

An integer format style modified to use the specified notation.

## Discussion

The following example creates a default [IntegerFormatStyle](../integerformatstyle.md) for the `en_US` locale, and a second style that uses scientific notation style. It then applies each style to an array of integers.

```swift
let defaultStyle = IntegerFormatStyle<Int>(locale: Locale(identifier: "en_US"))
let scientificStyle = defaultStyle.notation(.scientific)
let nums = [100, 1000, 10000, 100000, 1000000]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100", "1,000", "10,000", "100,000", "1,000,000"]
let scientificNums = nums.map { scientificStyle.format($0) } // ["1E2", "1E3", "1E4", "1E5", "1E6"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
