---
title: weekOfYear
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/weekofyear
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/weekofyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/weekofyear.json'
content_hash: 'sha256:9a6c4ee9a7045256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# weekOfYear

<sub>Instance Property</sub>

The ISO 8601 week date of the year.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var weekOfYear: Int { get set }
```

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Related Documentation

- [yearForWeekOfYear](yearforweekofyear.md) — The ISO 8601 week-numbering year.

### Accessing Weeks and Days

- [weekday](weekday.md) — The number of the weekdays.
- [weekdayOrdinal](weekdayordinal.md) — The ordinal number of weekdays.
- [weekOfMonth](weekofmonth.md) — The week number of the months.
- [day](day.md) — The number of days.
- [- week](<week().md>) — Returns the number of weeks. _(deprecated)_
- [- setWeek:](<setweek(__).md>) — Sets the number of weeks. _(deprecated)_
