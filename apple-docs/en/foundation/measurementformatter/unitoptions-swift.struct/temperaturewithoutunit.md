---
title: temperatureWithoutUnit
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatter/unitoptions-swift.struct/temperaturewithoutunit
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions-swift.struct/temperaturewithoutunit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/unitoptions-swift.struct/temperaturewithoutunit.json'
content_hash: 'sha256:770304eb609de728'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [MeasurementFormatter](../../measurementformatter.md) · [UnitOptions](../unitoptions-swift.struct.md)

# temperatureWithoutUnit

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var temperatureWithoutUnit: MeasurementFormatter.UnitOptions { get }
```

## Discussion

Specifies that representations of a measurement with the `NSTemperatureUnit` unit omit the letter denoting the temperature scale. For example, a temperature measurement with value equal to 72 using the [degreeFahrenheit()](<../../../healthkit/hkunit/degreefahrenheit().md>) would be represented as `72°` rather than `72°F`.

## See Also

### Working with options

- [NSMeasurementFormatterUnitOptionsProvidedUnit](providedunit.md)
- [NSMeasurementFormatterUnitOptionsNaturalScale](naturalscale.md)
