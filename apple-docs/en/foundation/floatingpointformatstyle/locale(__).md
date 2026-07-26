---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:ec82f6d0f0d4512b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FloatingPointFormatStyle](../floatingpointformatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> FloatingPointFormatStyle<Value>
```

## Parameters

- `locale` — The locale to apply to the format style.

## Return Value

A floating-point format style modified to use the provided locale.

## Discussion

Use this modifier to change the locale that an existing format style uses. To instead determine the locale this format style uses, use the [locale](locale.md) property.

The following example creates a default [FloatingPointFormatStyle](../floatingpointformatstyle.md) for the `en_US` locale, and applies the [notation(_:)](<../integerformatstyle/notation(__).md>) modifier to use compact name notation. Next, the sample creates a second style based on this first style, but using the German (`DE`) locale. It then applies each style to an array of floating-point values.

```swift
let compactStyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
    .notation(.compactName)
let germanStyle = compactStyle.locale(Locale(identifier: "DE"))
let nums: [Double] = [100, 1000, 10000, 100000, 1000000]
let enUSCompactNums = nums.map { compactStyle.format($0) } // ["100", "1K", "10K", "100K", "1M"]
let deCompactNums = nums.map { germanStyle.format($0) } // ["100", "1000", "10.000", "100.000", "1 Mio."]

```

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
