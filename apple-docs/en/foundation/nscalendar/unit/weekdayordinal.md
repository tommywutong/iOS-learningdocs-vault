---
title: weekdayOrdinal
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/unit/weekdayordinal
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/unit/weekdayordinal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/unit/weekdayordinal.json'
content_hash: 'sha256:042b934825360b1b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCalendar](../../nscalendar.md) · [Unit](../unit.md)

# weekdayOrdinal

<sub>Type Property</sub>

Identifier for the ordinal weekday unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var weekdayOrdinal: NSCalendar.Unit { get }
```

## Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitWeekdayOrdinal`. The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of `2` for a weekday unit `3` indicates “the second Tuesday in the month”.

## See Also

### Specifying Weeks and Days

- [NSCalendarUnitWeekOfYear](weekofyear.md) — Identifier for the week of the year calendar unit.
- [NSCalendarUnitWeekOfMonth](weekofmonth.md) — Identifier for the week of the month calendar unit.
- [NSCalendarUnitWeekday](weekday.md) — Identifier for the weekday unit.
- [NSCalendarUnitDay](day.md) — Identifier for the day unit.
- [NSCalendarUnitDayOfYear](dayofyear.md) — Identifier for the nanosecond unit.
- [NSCalendarUnitIsRepeatedDay](isrepeatedday.md) — Identifier for the time zone of a date components object.
