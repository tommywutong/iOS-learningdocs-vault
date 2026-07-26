---
title: CurrencyFormatStyleConfiguration.SignDisplayStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy
source_url: 'https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy.json'
content_hash: 'sha256:83056193d6a761e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CurrencyFormatStyleConfiguration](../currencyformatstyleconfiguration.md)

# CurrencyFormatStyleConfiguration.SignDisplayStrategy

<sub>Structure</sub>

A structure used to configure sign display strategies for currency format styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SignDisplayStrategy
```

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Specifying sign display strategy

- [never](signdisplaystrategy/never.md) — A strategy to never show the sign.
- [automatic](signdisplaystrategy/automatic.md) — A strategy to automatically configure sign display.
- [accounting](signdisplaystrategy/accounting.md) — A sign display strategy to use accounting principles.
- [accountingAlways(showZero:)](<signdisplaystrategy/accountingalways(showzero_).md>) — A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.
- [always(showZero:)](<signdisplaystrategy/always(showzero_).md>) — A sign display strategy to always show the sign, with a configurable behavior for handling zero values.

## See Also

### Specifying Configuration

- [Grouping](grouping.md) — The type used to configure grouping for currency format styles.
- [Precision](precision.md) — The type used to configure precision for currency format styles.
- [DecimalSeparatorDisplayStrategy](decimalseparatordisplaystrategy.md) — The type used to configure decimal separator display strategies for currency format styles.
- [RoundingRule](roundingrule.md) — The type used to configure rounding rules for currency format styles.
- [Presentation](presentation.md) — A structure used to configure the presentation of currency format styles.
