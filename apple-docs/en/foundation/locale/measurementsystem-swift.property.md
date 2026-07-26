---
title: measurementSystem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/measurementsystem-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/locale/measurementsystem-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/measurementsystem-swift.property.json'
content_hash: 'sha256:2255524077f6f2c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# measurementSystem

<sub>Instance Property</sub>

The measurement system used by the locale, like metric or the US system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var measurementSystem: Locale.MeasurementSystem { get }
```

## Discussion

When called on the special [Locale](../locale.md) instances [current](current.md) or [autoupdatingCurrent](autoupdatingcurrent.md), if the user overrode the default measurement system, this property provides the user’s preference.

This property corresponds to the `ms` key of the Unicode BCP 47 extension.

For locale instances created with the `ms` specifier (such as `en-US@ms=metric`), or with a custom [Components](components.md), this property represents the custom measurement system. Otherwise, it represents the locale’s default measurement system.

## See Also

### Getting measurement and counting components

- [currency](currency-swift.property.md) — The currency used by the locale.
- [Currency](currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [MeasurementSystem](measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](numberingsystem-swift.property.md) — The numbering system used by the locale.
- [availableNumberingSystems](availablenumberingsystems.md) — An array containing all the valid numbering systems for the locale.
- [NumberingSystem](numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
