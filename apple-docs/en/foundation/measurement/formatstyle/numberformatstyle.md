---
title: numberFormatStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/numberformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/numberformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/numberformatstyle.json'
content_hash: 'sha256:d8ac8fc6df0d3e4b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# numberFormatStyle

<sub>Instance Property</sub>

The formatting of the measurement value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberFormatStyle: FloatingPointFormatStyle<Double>?
```

## Discussion

The `numberFormat` property specifies the formatting of the measurement value. You can customize the precision, grouping, and rounding mode of the measurement by creating a numeric number format style.

The following example shows a customized measurement format style that includes two decimal numbers and excludes separators:

```swift
let volume = Measurement<UnitVolume>(value: 2300, unit: .milliliters)
volume.formatted(.measurement(width: .abbreviated,
                              usage: .asProvided,
                              numberFormatStyle: .number
                                  .precision(.fractionLength(2))
                                  .grouping(.never))) // "2300.00 mL"
```

## See Also

### Modifying a measurement format style

- [width](width.md) — The width of the measurement unit.
- [UnitWidth](unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [usage](usage.md) — The intended purpose of the formatted measurement.
- [hidesScaleName](hidesscalename.md) — The visibility of the unit name of a temperature.
- [locale](locale.md) — The locale of the format style.
- [locale(_:)](<locale(__).md>) — Modifies the measurement format style to use the specified locale.
