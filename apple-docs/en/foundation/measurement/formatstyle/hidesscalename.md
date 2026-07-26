---
title: hidesScaleName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/hidesscalename
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/hidesscalename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/hidesscalename.json'
content_hash: 'sha256:b11b309b6dec867d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# hidesScaleName

<sub>Instance Property</sub>

The visibility of the unit name of a temperature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hidesScaleName: Bool { get set }
```

## Discussion

Set `hidesScaleName` to `true` to exclude the unit name from a formatted temperature string. For example, `90°` rather than `90°F` or `90°C` with the [narrow](unitwidth/narrow.md) unit width, or `90 degrees` rather than `90 degrees Celcius` or `90 degrees Fahrenheit` with the [wide](unitwidth/wide.md) width.

Hiding the unit name only affects the presentation of the measurement. Unless you specify `asProvided` as the `usage`, the system converts the temperature to the unit that the locale uses.

## See Also

### Modifying a measurement format style

- [width](width.md) — The width of the measurement unit.
- [UnitWidth](unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [numberFormatStyle](numberformatstyle.md) — The formatting of the measurement value.
- [usage](usage.md) — The intended purpose of the formatted measurement.
- [locale](locale.md) — The locale of the format style.
- [locale(_:)](<locale(__).md>) — Modifies the measurement format style to use the specified locale.
