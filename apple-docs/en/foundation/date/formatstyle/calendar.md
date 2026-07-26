---
title: calendar
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/calendar
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/calendar.json'
content_hash: 'sha256:d387ffcd391e3b55'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# calendar

<sub>Instance Property</sub>

The calendar to use when formatting the date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendar: Calendar
```

## Discussion

Defaults to [autoupdatingCurrentCalendar](../../nscalendar/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using `autoupdatingCurrent`.

## See Also

### Modifying a Date Format Style

- [locale(_:)](<locale(__).md>) — Modifies the date format style to use the specified locale.
- [timeZone](timezone.md) — The time zone to use when formatting the date and time components.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the date.
- [locale](locale.md) — The locale to use when formatting the date and time components.
