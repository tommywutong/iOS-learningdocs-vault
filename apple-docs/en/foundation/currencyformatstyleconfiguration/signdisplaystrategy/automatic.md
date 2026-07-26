---
title: automatic
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/automatic
source_url: 'https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/automatic.json'
content_hash: 'sha256:9048c5ef3642e4c6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) · [SignDisplayStrategy](../signdisplaystrategy.md)

# automatic

<sub>Type Property</sub>

A strategy to automatically configure sign display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: CurrencyFormatStyleConfiguration.SignDisplayStrategy { get }
```

## See Also

### Specifying sign display strategy

- [never](never.md) — A strategy to never show the sign.
- [accounting](accounting.md) — A sign display strategy to use accounting principles.
- [accountingAlways(showZero:)](<accountingalways(showzero_).md>) — A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.
- [always(showZero:)](<always(showzero_).md>) — A sign display strategy to always show the sign, with a configurable behavior for handling zero values.
