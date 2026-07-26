---
title: weekdayOrdinal
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcalendarunit/weekdayordinal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarunit/weekdayordinal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarunit/weekdayordinal.json'
content_hash: 'sha256:4855675843f4eff9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFCalendarUnit](../cfcalendarunit.md)

# weekdayOrdinal

<sub>Type Property</sub>

Specifies the ordinal weekday unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var weekdayOrdinal: CFCalendarUnit { get }
```

## Discussion

The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of `2` for a weekday unit `3` indicates “the second Tuesday in the month”.

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
- [kCFCalendarUnitWeekday](weekday.md) — Specifies the weekday unit.
- [kCFCalendarUnitQuarter](quarter.md) — Specifies the quarter-year unit.
- [kCFCalendarUnitWeekOfMonth](weekofmonth.md) — Specifies the original week of a month calendar unit.
- [kCFCalendarUnitWeekOfYear](weekofyear.md) — Specifies the original week of the year calendar unit.
- [kCFCalendarUnitYearForWeekOfYear](yearforweekofyear.md) — Specifies the relative year for a week within a year calendar unit.
