---
title: dateTemplate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/datetemplate
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/datetemplate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/datetemplate.json'
content_hash: 'sha256:f773270014be80fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateIntervalFormatter](../dateintervalformatter.md)

# dateTemplate

<sub>Instance Property</sub>

The template for formatting one date and time value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dateTemplate: String! { get set }
```

## Discussion

Use this string to specify a custom fixed format for each of the date and time values. The string you specify is based on the Unicode Technical Standard #35, which uses characters to represent the day, time, year, hour, minute, and other pieces of date or time information.

If you do not assign a value to this string, the formatter object automatically updates the string based on the values in the [dateStyle](datestyle.md) and [timeStyle](timestyle.md) properties.

For information about how to define a custom formatting string, see [Date Formatters](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/dfDateFormatting10_4.html#//apple_ref/doc/uid/TP40002369) in [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## See Also

### Configuring the Formatter Options

- [dateStyle](datestyle.md) — The style to use when formatting day, month, and year information.
- [timeStyle](timestyle.md) — The style to use when formatting hour, minute, and second information.
- [calendar](calendar.md) — The calendar to use for date values.
- [locale](locale.md) — The locale to use when formatting date and time values.
- [timeZone](timezone.md) — The time zone with which to specify time values.
