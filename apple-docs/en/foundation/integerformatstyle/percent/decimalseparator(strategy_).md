---
title: 'decimalSeparator(strategy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/percent/decimalseparator(strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/percent/decimalseparator(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/percent/decimalseparator%28strategy%3A%29.json'
content_hash: 'sha256:e87e5b59631ccd27'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Percent](../percent.md)

# decimalSeparator(strategy:)

<sub>Instance Method</sub>

Modifies the format style to use the specified decimal separator display strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decimalSeparator(strategy: IntegerFormatStyle<Value>.Percent.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Percent
```

## Parameters

- `strategy` — The decimal separator display strategy to apply to the format style.

## Return Value

An integer percent format style modified to use the specified decimal separator display strategy.

## See Also

### Customizing style behavior

- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
