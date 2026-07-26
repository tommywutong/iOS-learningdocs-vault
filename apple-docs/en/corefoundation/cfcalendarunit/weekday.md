---
title: weekday
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcalendarunit/weekday
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarunit/weekday'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarunit/weekday.json'
content_hash: 'sha256:08646bef4c87dd43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFCalendarUnit](../cfcalendarunit.md)

# weekday

<sub>Type Property</sub>

Specifies the weekday unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var weekday: CFCalendarUnit { get }
```

## Discussion

The weekday units are the numbers `1`-`N` (where for the Gregorian calendar `N=7` and `1` is Sunday).

## See Also

### Constants

- [kCFCalendarUnitEra](era.md) — Specifies the era unit.
- [kCFCalendarUnitYear](year.md) — Specifies the year unit.
- [kCFCalendarUnitMonth](month.md) — Specifies the month unit.
- [kCFCalendarUnitDay](day.md) — Specifies the day unit.
- [kCFCalendarUnitHour](hour.md) — Specifies the hour unit.
- [kCFCalendarUnitMinute](minute.md) — Specifies the minute unit.
- [kCFCalendarUnitSecond](second.md) — Specifies the second unit.
- [kCFCalendarUnitWeek](week.md) — Specifies the week unit. _(deprecated)_
- [kCFCalendarUnitWeekdayOrdinal](weekdayordinal.md) — Specifies the ordinal weekday unit.
- [kCFCalendarUnitQuarter](quarter.md) — Specifies the quarter-year unit.
- [kCFCalendarUnitWeekOfMonth](weekofmonth.md) — Specifies the original week of a month calendar unit.
- [kCFCalendarUnitWeekOfYear](weekofyear.md) — Specifies the original week of the year calendar unit.
- [kCFCalendarUnitYearForWeekOfYear](yearforweekofyear.md) — Specifies the relative year for a week within a year calendar unit.
