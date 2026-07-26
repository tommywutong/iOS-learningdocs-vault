---
title: unitOptions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatter/unitoptions-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/unitoptions-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/unitoptions-swift.property.json'
content_hash: 'sha256:768cf05ef1bc7f67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# unitOptions

<sub>Instance Property</sub>

The options for how the unit is formatted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitOptions: MeasurementFormatter.UnitOptions { get set }
```

## Discussion

You can set this property to ensure that the formatter chooses the preferred unit to format for the measurement based on the formatter’s locale. For possible values, see [UnitOptions](unitoptions-swift.struct.md).

If no options are specified, the formatter localizes according to the preferences of the formatter’s [locale](locale.md). For example, a measurement in kilocalories may be formatted as `C` instead of `kcal`, or a measurement in kilometers per hour may be formatted as `miles per hour` for US and UK locales, but `kilometers per hour` for other locales. However, if the `providedUnit` option is specified, a measurement with [kilocalories](../unitenergy/kilocalories.md) units would be formatted as `kcal`, even if the locale prefers `C`, and a measurement with [kilometersPerHour](../unitspeed/kilometersperhour.md) units would be formatted as `kilometers per hour` for US and UK locales, even though they prefer `miles per hour`.

> [!note] Note
> `NSMeasurementFormatter` handles the conversion of measurements to the preferred units in a particular locale when this option is specified. For example, if provided a measurement object in kilojoules, the formatter implicitly converts the measurement object to kilocalories and returns the formatted string as the equivalent measurement in kilocalories.

## See Also

### Specifying the Format

- [UnitOptions](unitoptions-swift.struct.md) — Measurement formatter options.
- [unitStyle](unitstyle.md) — The unit style.
- [locale](locale.md) — The locale of the formatter.
- [numberFormatter](numberformatter.md) — The number formatter used to format the quantity of a measurement.
