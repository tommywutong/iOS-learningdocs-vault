---
title: weekOfMonth
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/weekofmonth
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/weekofmonth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/weekofmonth.json'
content_hash: 'sha256:55a8dcb32d1ad262'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# weekOfMonth

<sub>Instance Property</sub>

The week number of the months.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var weekOfMonth: Int { get set }
```

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Weeks and Days

- [weekday](weekday.md) — The number of the weekdays.
- [weekdayOrdinal](weekdayordinal.md) — The ordinal number of weekdays.
- [weekOfYear](weekofyear.md) — The ISO 8601 week date of the year.
- [day](day.md) — The number of days.
- [- week](<week().md>) — Returns the number of weeks. _(deprecated)_
- [- setWeek:](<setweek(__).md>) — Sets the number of weeks. _(deprecated)_
