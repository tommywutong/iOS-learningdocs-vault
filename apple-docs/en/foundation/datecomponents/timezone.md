---
title: timeZone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/timezone
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/timezone.json'
content_hash: 'sha256:c9d99e78db089cf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# timeZone

<sub>Instance Property</sub>

A time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeZone: TimeZone? { get set }
```

## Discussion

> [!note] Note
> This value is interpreted in the context of the calendar in which it is used.

## See Also

### Initializing Date Components

- [init(calendar:timeZone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayOrdinal:quarter:weekOfMonth:weekOfYear:yearForWeekOfYear:)](<init(calendar_timezone_era_year_month_day_hour_minute_second_nanosecond_weekday_weekdayordinal_quarter_weekofmonth_weekofyear_yearforweekofyear_).md>) — Initializes a date components value, optionally specifying values for its fields.
- [calendar](calendar.md) — The calendar used to interpret the other values in this structure.
