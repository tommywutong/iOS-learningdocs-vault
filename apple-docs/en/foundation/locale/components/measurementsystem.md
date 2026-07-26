---
title: measurementSystem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/measurementsystem
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/measurementsystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/measurementsystem.json'
content_hash: 'sha256:c5c554b306cbea2b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# measurementSystem

<sub>Instance Property</sub>

The measurement system used by the locale, like metric or the US system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var measurementSystem: Locale.MeasurementSystem?
```

## Discussion

Set this property to override the locale’s default measurement system. To request the default measurement system used by the locale, use the [Locale](../../locale.md) property `measurementSystem`.

This property corresponds to the `ms` key of the Unicode BCP 47 extension.

## See Also

### Specifiying measurement and counting components

- [currency](currency.md) — The currency used by the locale.
- [Currency](../currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [MeasurementSystem](../measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](numberingsystem.md) — The numbering system used by the locale.
- [NumberingSystem](../numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
