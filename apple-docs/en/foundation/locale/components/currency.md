---
title: currency
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/currency
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/currency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/currency.json'
content_hash: 'sha256:403827dc33b4e0c0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# currency

<sub>Instance Property</sub>

The currency used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currency: Locale.Currency?
```

## Discussion

Set this property to override the locale’s default currency. To request the default currency used by the locale, use the [Locale](../../locale.md) property [currency](../currency-swift.property.md).

This property corresponds to the `cu` key of the Unicode BCP 47 extension.

## See Also

### Specifiying measurement and counting components

- [Currency](../currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [measurementSystem](measurementsystem.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](../measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](numberingsystem.md) — The numbering system used by the locale.
- [NumberingSystem](../numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
