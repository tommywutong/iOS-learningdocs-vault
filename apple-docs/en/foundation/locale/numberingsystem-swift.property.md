---
title: numberingSystem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/numberingsystem-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/locale/numberingsystem-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/numberingsystem-swift.property.json'
content_hash: 'sha256:b09ada1267197826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# numberingSystem

<sub>Instance Property</sub>

The numbering system used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberingSystem: Locale.NumberingSystem { get }
```

## Discussion

This property corresponds to the `nu` key of the Unicode BCP 47 extension.

For locale instances created with the `nu` specifier (such as `en-US@nu=jpanfin`), or with a custom [Components](components.md), this property represents the custom numbering system. Otherwise, it represents the locale’s default numbering system.

## See Also

### Getting measurement and counting components

- [currency](currency-swift.property.md) — The currency used by the locale.
- [Currency](currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [measurementSystem](measurementsystem-swift.property.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [availableNumberingSystems](availablenumberingsystems.md) — An array containing all the valid numbering systems for the locale.
- [NumberingSystem](numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
