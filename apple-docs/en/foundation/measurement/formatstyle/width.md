---
title: width
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/width
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/width'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/width.json'
content_hash: 'sha256:0d2a69745dbbb9cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# width

<sub>Instance Property</sub>

The width of the measurement unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var width: Measurement<UnitType>.FormatStyle.UnitWidth
```

## Discussion

The `width` property specifies the display of the measurement unit. The possible values are [abbreviated](unitwidth/abbreviated.md), [narrow](unitwidth/narrow.md), and [wide](unitwidth/wide.md). The format style represents the unit in the shortest notation available.

The following example shows _100 degrees Fahrenheit_ in each width for the `en_US` locale.

```swift
let temperatureMeasurement = Measurement<UnitTemperature>(value: 100, unit: .fahrenheit)
temperatureMeasurement.formatted(.measurement(width: .wide)) // 100 degrees Fahrenheit
temperatureMeasurement.formatted(.measurement(width: .abbreviated)) // 100°F
temperatureMeasurement.formatted(.measurement(width: .narrow)) // 100°
```

## See Also

### Modifying a measurement format style

- [UnitWidth](unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [numberFormatStyle](numberformatstyle.md) — The formatting of the measurement value.
- [usage](usage.md) — The intended purpose of the formatted measurement.
- [hidesScaleName](hidesscalename.md) — The visibility of the unit name of a temperature.
- [locale](locale.md) — The locale of the format style.
- [locale(_:)](<locale(__).md>) — Modifies the measurement format style to use the specified locale.
