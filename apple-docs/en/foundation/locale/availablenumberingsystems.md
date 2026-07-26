---
title: availableNumberingSystems
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/availablenumberingsystems
source_url: 'https://developer.apple.com/documentation/foundation/locale/availablenumberingsystems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/availablenumberingsystems.json'
content_hash: 'sha256:4ab4918df3830cec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# availableNumberingSystems

<sub>Instance Property</sub>

An array containing all the valid numbering systems for the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var availableNumberingSystems: [Locale.NumberingSystem] { get }
```

## Discussion

The following snippet creates a locale for Arabic as used in United Arab Emirites. For this locale, there are two numbering systems available: `latn` (Latin digits) and `arab` (Arabic-Indic digits).

```swift
let uae = Locale(identifier: "ar-AE") // Arabic / U.A.E.
let numberingSystems = uae.availableNumberingSystems
print("\(numberingSystems.map{$0.identifier})") // ["latn","arab"]
```

## See Also

### Getting measurement and counting components

- [currency](currency-swift.property.md) — The currency used by the locale.
- [Currency](currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [measurementSystem](measurementsystem-swift.property.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](numberingsystem-swift.property.md) — The numbering system used by the locale.
- [NumberingSystem](numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
