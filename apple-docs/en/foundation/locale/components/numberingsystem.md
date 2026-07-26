---
title: numberingSystem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/numberingsystem
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/numberingsystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/numberingsystem.json'
content_hash: 'sha256:9c4e06abe6b1b119'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# numberingSystem

<sub>Instance Property</sub>

The numbering system used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberingSystem: Locale.NumberingSystem?
```

## Discussion

Set this property to override the locale’s default numbering system. To request the default numbering system used by the locale, use the [Locale](../../locale.md) property `numberingSystem`.

This property corresponds to the `nu` key of the Unicode BCP 47 extension.

## See Also

### Specifiying measurement and counting components

- [currency](currency.md) — The currency used by the locale.
- [Currency](../currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [measurementSystem](measurementsystem.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](../measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [NumberingSystem](../numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
