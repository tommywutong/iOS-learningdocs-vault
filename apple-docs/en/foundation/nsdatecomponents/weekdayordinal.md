---
title: weekdayOrdinal
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/weekdayordinal
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/weekdayordinal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/weekdayordinal.json'
content_hash: 'sha256:c41acc28c7be9121'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# weekdayOrdinal

<sub>Instance Property</sub>

The ordinal number of weekdays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var weekdayOrdinal: Int { get set }
```

## Discussion

Weekday ordinal units represent the position of the weekday within the next larger calendar unit, such as the month. For example, _2_ is the weekday ordinal unit for the _second_ Friday of the month.

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Weeks and Days

- [weekday](weekday.md) — The number of the weekdays.
- [weekOfMonth](weekofmonth.md) — The week number of the months.
- [weekOfYear](weekofyear.md) — The ISO 8601 week date of the year.
- [day](day.md) — The number of days.
- [- week](<week().md>) — Returns the number of weeks. _(deprecated)_
- [- setWeek:](<setweek(__).md>) — Sets the number of weeks. _(deprecated)_
