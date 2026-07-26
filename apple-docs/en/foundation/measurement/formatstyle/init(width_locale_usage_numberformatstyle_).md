---
title: 'init(width:locale:usage:numberFormatStyle:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/formatstyle/init(width:locale:usage:numberformatstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/init(width:locale:usage:numberformatstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/init%28width%3Alocale%3Ausage%3Anumberformatstyle%3A%29.json'
content_hash: 'sha256:1c25bf8b8816cf7c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# init(width:locale:usage:numberFormatStyle:)

<sub>Initializer</sub>

Creates an instance using the provided width, locale, usage type, and number format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(width: Measurement<UnitType>.FormatStyle.UnitWidth, locale: Locale = .autoupdatingCurrent, usage: MeasurementFormatUnitUsage<UnitType> = .general, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil)
```

## Parameters

- `width` — The width of the measurement unit.

- `locale` — The locale to use when formatting the measurement.

- `usage` — The intended purpose of the formatted measurement.

- `numberFormatStyle` — The presentation style of the numeric value.

## See Also

### Creating a measurement format style

- [init(width:locale:usage:hidesScaleName:numberFormatStyle:)](<init(width_locale_usage_hidesscalename_numberformatstyle_).md>) — Creates an instance using the provided width, locale, usage type, number format, and the option to hide the unit name.
