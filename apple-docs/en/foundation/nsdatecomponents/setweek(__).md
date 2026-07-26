---
title: 'setWeek(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdatecomponents/setweek(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/setweek(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/setweek%28_%3A%29.json'
content_hash: 'sha256:3d975abdfd9143f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# setWeek(_:)

<sub>Instance Method</sub>

Sets the number of weeks.

> [!warning] Deprecated
> Use [weekOfYear](weekofyear.md) or [weekOfMonth](weekofmonth.md) instead, depending on what you intend.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func setWeek(_ v: Int)
```

## Parameters

- `v` — The number of week units.

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Weeks and Days

- [weekday](weekday.md) — The number of the weekdays.
- [weekdayOrdinal](weekdayordinal.md) — The ordinal number of weekdays.
- [weekOfMonth](weekofmonth.md) — The week number of the months.
- [weekOfYear](weekofyear.md) — The ISO 8601 week date of the year.
- [day](day.md) — The number of days.
- [- week](<week().md>) — Returns the number of weeks. _(deprecated)_
