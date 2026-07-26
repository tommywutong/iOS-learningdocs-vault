---
title: IntegerFormatStyle.Configuration
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/integerformatstyle/configuration
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/configuration.json'
content_hash: 'sha256:9d805e6b718cacc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# IntegerFormatStyle.Configuration

<sub>Type Alias</sub>

The type the format style uses for configuration settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Configuration = NumberFormatStyleConfiguration
```

## Discussion

[IntegerFormatStyle](../integerformatstyle.md) uses [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) for its configuration type.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.
