---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/locale
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/locale.json'
content_hash: 'sha256:cbfd03c93c973d63'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# locale

<sub>Instance Property</sub>

The locale of the format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale
```

## Discussion

By default, the format style displays a measurement in the unit that `locale` specifies. The default value is [autoupdatingCurrent](../../locale/autoupdatingcurrent.md).

## See Also

### Modifying a measurement format style

- [width](width.md) — The width of the measurement unit.
- [UnitWidth](unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [numberFormatStyle](numberformatstyle.md) — The formatting of the measurement value.
- [usage](usage.md) — The intended purpose of the formatted measurement.
- [hidesScaleName](hidesscalename.md) — The visibility of the unit name of a temperature.
- [locale(_:)](<locale(__).md>) — Modifies the measurement format style to use the specified locale.
