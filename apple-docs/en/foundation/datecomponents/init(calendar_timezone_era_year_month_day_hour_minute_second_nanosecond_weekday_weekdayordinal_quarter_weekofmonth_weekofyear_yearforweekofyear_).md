---
title: 'init(calendar:timeZone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayOrdinal:quarter:weekOfMonth:weekOfYear:yearForWeekOfYear:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/init(calendar:timezone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayordinal:quarter:weekofmonth:weekofyear:yearforweekofyear:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/init(calendar:timezone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayordinal:quarter:weekofmonth:weekofyear:yearforweekofyear:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/init%28calendar%3Atimezone%3Aera%3Ayear%3Amonth%3Aday%3Ahour%3Aminute%3Asecond%3Ananosecond%3Aweekday%3Aweekdayordinal%3Aquarter%3Aweekofmonth%3Aweekofyear%3Ayearforweekofyear%3A%29.json'
content_hash: 'sha256:03fbb7c19af41dc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# init(calendar:timeZone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayOrdinal:quarter:weekOfMonth:weekOfYear:yearForWeekOfYear:)

<sub>Initializer</sub>

Initializes a date components value, optionally specifying values for its fields.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(calendar: Calendar? = nil, timeZone: TimeZone? = nil, era: Int? = nil, year: Int? = nil, month: Int? = nil, day: Int? = nil, hour: Int? = nil, minute: Int? = nil, second: Int? = nil, nanosecond: Int? = nil, weekday: Int? = nil, weekdayOrdinal: Int? = nil, quarter: Int? = nil, weekOfMonth: Int? = nil, weekOfYear: Int? = nil, yearForWeekOfYear: Int? = nil)
```

## See Also

### Initializing Date Components

- [calendar](calendar.md) — The calendar used to interpret the other values in this structure.
- [timeZone](timezone.md) — A time zone.
