---
title: 'sign(strategy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/floatingpointformatstyle/percent/sign(strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent/sign(strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle/percent/sign%28strategy%3A%29.json'
content_hash: 'sha256:54c5a066baba1a7b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FloatingPointFormatStyle](../../floatingpointformatstyle.md) · [Percent](../percent.md)

# sign(strategy:)

<sub>Instance Method</sub>

Modifies the format style to use the specified sign display strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sign(strategy: FloatingPointFormatStyle<Value>.Percent.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Percent
```

## Parameters

- `strategy` — The sign display strategy to apply to the format style.

## Return Value

A floating-point format style modified to use the specified sign display strategy.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [Configuration](configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
