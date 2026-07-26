---
title: 'always(showZero:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/always(showzero:)'
source_url: 'https://developer.apple.com/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/always(showzero:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/currencyformatstyleconfiguration/signdisplaystrategy/always%28showzero%3A%29.json'
content_hash: 'sha256:f7803bb35ccc0105'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) · [SignDisplayStrategy](../signdisplaystrategy.md)

# always(showZero:)

<sub>Type Method</sub>

A sign display strategy to always show the sign, with a configurable behavior for handling zero values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func always(showZero: Bool = true) -> CurrencyFormatStyleConfiguration.SignDisplayStrategy
```

## Parameters

- `showZero` — A Boolean value that indicates whether to show the sign symbol on zero values. Defaults to `true`.

## Return Value

A sign display strategy that always displays the sign, and uses the specified handling of zero values.

## See Also

### Specifying sign display strategy

- [never](never.md) — A strategy to never show the sign.
- [automatic](automatic.md) — A strategy to automatically configure sign display.
- [accounting](accounting.md) — A sign display strategy to use accounting principles.
- [accountingAlways(showZero:)](<accountingalways(showzero_).md>) — A sign display strategy to use accounting principles, with a configurable behavior for handling zero values.
