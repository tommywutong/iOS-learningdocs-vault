---
title: 'init(width:locale:usage:hidesScaleName:numberFormatStyle:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/formatstyle/init(width:locale:usage:hidesscalename:numberformatstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/init(width:locale:usage:hidesscalename:numberformatstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/init%28width%3Alocale%3Ausage%3Ahidesscalename%3Anumberformatstyle%3A%29.json'
content_hash: 'sha256:989df794d815546b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# init(width:locale:usage:hidesScaleName:numberFormatStyle:)

<sub>Initializer</sub>

Creates an instance using the provided width, locale, usage type, number format, and the option to hide the unit name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(width: Measurement<UnitType>.FormatStyle.UnitWidth = .abbreviated, locale: Locale = .autoupdatingCurrent, usage: MeasurementFormatUnitUsage<UnitType> = .general, hidesScaleName: Bool = false, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil)
```

## Parameters

- `width` — The width of the measurement unit.

- `locale` — The locale to use when formatting the measurement.

- `usage` — The intended purpose of the formatted measurement.

- `hidesScaleName` — An option to hide the unit name of a measurement.

- `numberFormatStyle` — The presentation style of the numeric value.

## See Also

### Creating a measurement format style

- [init(width:locale:usage:numberFormatStyle:)](<init(width_locale_usage_numberformatstyle_).md>) — Creates an instance using the provided width, locale, usage type, and number format.
