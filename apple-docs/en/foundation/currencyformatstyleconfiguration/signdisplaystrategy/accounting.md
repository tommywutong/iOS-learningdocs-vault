---
title: accounting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/accounting
source_url: 'https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/accounting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/accounting.json'
content_hash: 'sha256:9e3c3119a719948e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) · [SignDisplayStrategy](../signdisplaystrategy.md)

# accounting

<sub>Type Property</sub>

A sign display strategy to use accounting principles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var accounting: CurrencyFormatStyleConfiguration.SignDisplayStrategy { get }
```

## Discussion

This strategy always shows the currency symbol, and shows negative values in parenthesis. Examples of this strategy include `$123`, `$0`, and `($123)`.

## See Also

### Specifying sign display strategy

- [never](never.md) — A strategy to never show the sign.
- [automatic](automatic.md) — A strategy to automatically configure sign display.
- [accountingAlways(showZero:)](<accountingalways(showzero_).md>) — A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.
- [always(showZero:)](<always(showzero_).md>) — A sign display strategy to always show the sign, with a configurable behavior for handling zero values.
