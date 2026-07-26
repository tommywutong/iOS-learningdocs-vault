---
title: usage
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/usage
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/usage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/usage.json'
content_hash: 'sha256:7d6a2c67a7337e1d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# usage

<sub>Instance Property</sub>

The intended purpose of the formatted measurement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var usage: MeasurementFormatUnitUsage<UnitType>?
```

## Discussion

You can use the `usage` property to specify the intended purpose of the formatted measurement. The default option, `general`, formats the measurement with the default unit for the current locale. The `asProvided` option formats the measurement using the specified unit, ignoring the unit that the locale uses.

The following example shows a formatted temperature using the default unit for the `en_US` locale and using a provided Celsius unit:

```swift
let temperature = Measurement<UnitTemperature>(value: 36.8, unit: .celsius)
temperature.formatted()
// 98°F

temperature.formatted(.measurement(width: .abbreviated, usage: .asProvided))
// 36.8°C
```

All unit types have `general` and `asProvided` options. Some subclasses have additional options, such as the following:

[UnitTemperature](../../unittemperature.md)

- `person`
- `weather`

[UnitLength](../../unitlength.md)

- `person`
- `personHeight`
- `road`

[UnitEnergy](../../unitenergy.md)

- `food`
- `workout`

[UnitMass](../../unitmass.md)

- `personWeight`

## See Also

### Modifying a measurement format style

- [width](width.md) — The width of the measurement unit.
- [UnitWidth](unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [numberFormatStyle](numberformatstyle.md) — The formatting of the measurement value.
- [hidesScaleName](hidesscalename.md) — The visibility of the unit name of a temperature.
- [locale](locale.md) — The locale of the format style.
- [locale(_:)](<locale(__).md>) — Modifies the measurement format style to use the specified locale.
