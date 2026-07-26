---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/intervalformatstyle/locale
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/locale.json'
content_hash: 'sha256:2528cb2c0e55dbf5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# locale

<sub>Instance Property</sub>

The locale for formatting the date and time interval components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale
```

## Discussion

The default value is [autoupdatingCurrentLocale](../../nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to use `autoupdatingCurrent.`

## See Also

### Specifying Date Interval Format Styles

- [timeZone(_:)](<timezone(__).md>) — Modifies the date interval format style to use the specified time zone format.
- [locale(_:)](<locale(__).md>) — Modifies the date interval format style to use the specified locale.
- [calendar](calendar.md) — The calendar for formatting the date interval.
- [timeZone](timezone.md) — The time zone for formatting the date interval components.
