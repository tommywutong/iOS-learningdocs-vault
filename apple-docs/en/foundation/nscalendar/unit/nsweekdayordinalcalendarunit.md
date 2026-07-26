---
title: NSWeekdayOrdinalCalendarUnit
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nscalendar/unit/nsweekdayordinalcalendarunit
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/unit/nsweekdayordinalcalendarunit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/unit/nsweekdayordinalcalendarunit.json'
content_hash: 'sha256:0850f426343fd9ff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCalendar](../../nscalendar.md) · [Unit](../unit.md)

# NSWeekdayOrdinalCalendarUnit

<sub>Type Property</sub>

Specifies the ordinal weekday unit.

> [!warning] Deprecated
> Use [NSCalendarUnitWeekdayOrdinal](weekdayordinal.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var NSWeekdayOrdinalCalendarUnit: NSCalendar.Unit { get }
```

## Discussion

The corresponding value is an `kCFCalendarUnitSecond`. Equal to `kCFCalendarUnitWeekdayOrdinal`. The weekday ordinal unit describes ordinal position within the month unit of the corresponding weekday unit. For example, in the Gregorian calendar a weekday ordinal unit of 2 for a weekday unit 3 indicates “the second Tuesday in the month”.

## See Also

### Deprecated

- [NSEraCalendarUnit](nseracalendarunit.md) — Specifies the era unit. _(deprecated)_
- [NSYearCalendarUnit](nsyearcalendarunit.md) — Specifies the year unit. _(deprecated)_
- [NSMonthCalendarUnit](nsmonthcalendarunit.md) — Specifies the month unit. _(deprecated)_
- [NSDayCalendarUnit](nsdaycalendarunit.md) — Specifies the day unit. _(deprecated)_
- [NSHourCalendarUnit](nshourcalendarunit.md) — Specifies the hour unit. _(deprecated)_
- [NSMinuteCalendarUnit](nsminutecalendarunit.md) — Specifies the minute unit. _(deprecated)_
- [NSSecondCalendarUnit](nssecondcalendarunit.md) — Specifies the second unit. _(deprecated)_
- [NSWeekCalendarUnit](nsweekcalendarunit.md) — Specifies the week unit. _(deprecated)_
- [NSWeekdayCalendarUnit](nsweekdaycalendarunit.md) — Specifies the weekday unit. _(deprecated)_
- [NSQuarterCalendarUnit](nsquartercalendarunit.md) — Specifies the quarter unit. _(deprecated)_
- [NSWeekOfMonthCalendarUnit](nsweekofmonthcalendarunit.md) — Specifies the original week of a month calendar unit. _(deprecated)_
- [NSWeekOfYearCalendarUnit](nsweekofyearcalendarunit.md) — Specifies the original week of the year calendar unit. _(deprecated)_
- [NSYearForWeekOfYearCalendarUnit](nsyearforweekofyearcalendarunit.md) — Specifies the year when the calendar is being interpreted as a week-based calendar. _(deprecated)_
- [NSCalendarCalendarUnit](nscalendarcalendarunit.md) — Specifies the calendar of the calendar. _(deprecated)_
- [NSTimeZoneCalendarUnit](nstimezonecalendarunit.md) — Specifies the time zone of the calendar as an `NSTimeZone`. _(deprecated)_
