---
title: NumberFormatStyleConfiguration
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatstyleconfiguration
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration.json'
content_hash: 'sha256:8f4862aeac97885f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NumberFormatStyleConfiguration

<sub>Enumeration</sub>

Configuration settings for formatting numbers of different types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NumberFormatStyleConfiguration
```

## Overview

This type is effectively a namespace to collect types that configure parts of a formatted number, such as grouping, precision, and separator and sign characters.

## Topics

### Specifying Configuration

- [DecimalSeparatorDisplayStrategy](numberformatstyleconfiguration/decimalseparatordisplaystrategy.md) — A structure that an integer format style uses to configure a decimal separator display strategy.
- [Grouping](numberformatstyleconfiguration/grouping.md) — A structure that an integer format style uses to configure grouping.
- [Precision](numberformatstyleconfiguration/precision.md) — A structure that an integer format style uses to configure precision.
- [RoundingRule](numberformatstyleconfiguration/roundingrule.md) — The type used for rounding rule values.
- [SignDisplayStrategy](numberformatstyleconfiguration/signdisplaystrategy.md) — A structure that an integer format style uses to configure a sign display strategy.
- [Notation](numberformatstyleconfiguration/notation.md) — A structure that an integer format style uses to configure notation.

## See Also

### Customizing style behavior

- [decimalSeparator(strategy:)](<decimal/formatstyle/decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<decimal/formatstyle/grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<decimal/formatstyle/locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<decimal/formatstyle/notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<decimal/formatstyle/precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<decimal/formatstyle/rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<decimal/formatstyle/scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<decimal/formatstyle/sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](decimal/formatstyle/configuration.md) — The type the format style uses for configuration settings.
