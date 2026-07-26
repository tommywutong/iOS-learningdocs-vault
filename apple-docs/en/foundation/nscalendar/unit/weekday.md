---
title: weekday
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/unit/weekday
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/unit/weekday'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/unit/weekday.json'
content_hash: 'sha256:f1a983e121179253'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCalendar](../../nscalendar.md) · [Unit](../unit.md)

# weekday

<sub>Type Property</sub>

Identifier for the weekday unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var weekday: NSCalendar.Unit { get }
```

## Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitWeekday`. The weekday units are the numbers `1` through `N` (where for the Gregorian calendar `N`=`7` and `1` is Sunday).

## See Also

### Specifying Weeks and Days

- [NSCalendarUnitWeekOfYear](weekofyear.md) — Identifier for the week of the year calendar unit.
- [NSCalendarUnitWeekOfMonth](weekofmonth.md) — Identifier for the week of the month calendar unit.
- [NSCalendarUnitWeekdayOrdinal](weekdayordinal.md) — Identifier for the ordinal weekday unit.
- [NSCalendarUnitDay](day.md) — Identifier for the day unit.
- [NSCalendarUnitDayOfYear](dayofyear.md) — Identifier for the nanosecond unit.
- [NSCalendarUnitIsRepeatedDay](isrepeatedday.md) — Identifier for the time zone of a date components object.
