---
title: 'scale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/scale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/scale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/scale%28_%3A%29.json'
content_hash: 'sha256:9fd53a55b9afd64b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FloatingPointFormatStyle](../floatingpointformatstyle.md)

# scale(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified scale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scale(_ multiplicand: Double) -> FloatingPointFormatStyle<Value>
```

## Parameters

- `multiplicand` — The multiplicand to apply to the format style.

## Return Value

A floating-point format style modified to use the specified scale.

## Discussion

The following example creates a default [FloatingPointFormatStyle](../floatingpointformatstyle.md) for the `en_US` locale, and a second style that scales by a `multiplicand` of `0.001`. It then applies each style to an array of floating-point values. The formatting that the modified style applies expresses each value in terms of one-thousandths.

```swift
let defaultStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
let scaledStyle = defaultStyle.scale(0.001)
let nums = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let defaultNums = nums.map { defaultStyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]
let scaledNums = nums.map { scaledStyle.format($0) } // ["0.1001", "1.0002", "10.0003", "100.0004", "1,000.0005"]
```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
