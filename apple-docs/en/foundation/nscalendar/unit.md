---
title: NSCalendar.Unit
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/unit
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/unit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/unit.json'
content_hash: 'sha256:7f3c19fce6c37b5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# NSCalendar.Unit

<sub>Structure</sub>

Calendrical units such as year, month, day and hour.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Unit
```

## Overview

Calendar units may be used as a bit mask to specify a combination of units. Values in this enumeration are equal to the corresponding constants in `CFCalendarUnit`.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<unit/init(rawvalue_).md>) — Creates a new calendar unit from the raw value.

### Specifying Years and Months

- [NSCalendarUnitEra](unit/era.md) — Identifier for the era unit.
- [NSCalendarUnitYear](unit/year.md) — Identifier for the year unit.
- [NSCalendarUnitYearForWeekOfYear](unit/yearforweekofyear.md) — Identifier for the week-counting year unit.
- [NSCalendarUnitQuarter](unit/quarter.md) — Identifier for the quarter of the calendar.
- [NSCalendarUnitMonth](unit/month.md) — Identifier for the month unit.
- [NSCalendarUnitIsLeapMonth](unit/isleapmonth.md) — Identifier for the time zone of a date components object.

### Specifying Weeks and Days

- [NSCalendarUnitWeekOfYear](unit/weekofyear.md) — Identifier for the week of the year calendar unit.
- [NSCalendarUnitWeekOfMonth](unit/weekofmonth.md) — Identifier for the week of the month calendar unit.
- [NSCalendarUnitWeekday](unit/weekday.md) — Identifier for the weekday unit.
- [NSCalendarUnitWeekdayOrdinal](unit/weekdayordinal.md) — Identifier for the ordinal weekday unit.
- [NSCalendarUnitDay](unit/day.md) — Identifier for the day unit.
- [NSCalendarUnitDayOfYear](unit/dayofyear.md) — Identifier for the nanosecond unit.
- [NSCalendarUnitIsRepeatedDay](unit/isrepeatedday.md) — Identifier for the time zone of a date components object.

### Specifying Hours, Minutes, and Seconds

- [NSCalendarUnitHour](unit/hour.md) — Identifier for the hour unit.
- [NSCalendarUnitMinute](unit/minute.md) — Identifier for the minute unit.
- [NSCalendarUnitSecond](unit/second.md) — Identifier for the second unit.
- [NSCalendarUnitNanosecond](unit/nanosecond.md) — Identifier for the nanosecond unit.

### Specifying Calendars and Time Zones

- [NSCalendarUnitCalendar](unit/calendar.md) — Identifier for the calendar of a date components object.
- [NSCalendarUnitTimeZone](unit/timezone.md) — Identifier for the time zone of a date components object.

### Deprecated

- [NSEraCalendarUnit](unit/nseracalendarunit.md) — Specifies the era unit. _(deprecated)_
- [NSYearCalendarUnit](unit/nsyearcalendarunit.md) — Specifies the year unit. _(deprecated)_
- [NSMonthCalendarUnit](unit/nsmonthcalendarunit.md) — Specifies the month unit. _(deprecated)_
- [NSDayCalendarUnit](unit/nsdaycalendarunit.md) — Specifies the day unit. _(deprecated)_
- [NSHourCalendarUnit](unit/nshourcalendarunit.md) — Specifies the hour unit. _(deprecated)_
- [NSMinuteCalendarUnit](unit/nsminutecalendarunit.md) — Specifies the minute unit. _(deprecated)_
- [NSSecondCalendarUnit](unit/nssecondcalendarunit.md) — Specifies the second unit. _(deprecated)_
- [NSWeekCalendarUnit](unit/nsweekcalendarunit.md) — Specifies the week unit. _(deprecated)_
- [NSWeekdayCalendarUnit](unit/nsweekdaycalendarunit.md) — Specifies the weekday unit. _(deprecated)_
- [NSWeekdayOrdinalCalendarUnit](unit/nsweekdayordinalcalendarunit.md) — Specifies the ordinal weekday unit. _(deprecated)_
- [NSQuarterCalendarUnit](unit/nsquartercalendarunit.md) — Specifies the quarter unit. _(deprecated)_
- [NSWeekOfMonthCalendarUnit](unit/nsweekofmonthcalendarunit.md) — Specifies the original week of a month calendar unit. _(deprecated)_
- [NSWeekOfYearCalendarUnit](unit/nsweekofyearcalendarunit.md) — Specifies the original week of the year calendar unit. _(deprecated)_
- [NSYearForWeekOfYearCalendarUnit](unit/nsyearforweekofyearcalendarunit.md) — Specifies the year when the calendar is being interpreted as a week-based calendar. _(deprecated)_
- [NSCalendarCalendarUnit](unit/nscalendarcalendarunit.md) — Specifies the calendar of the calendar. _(deprecated)_
- [NSTimeZoneCalendarUnit](unit/nstimezonecalendarunit.md) — Specifies the time zone of the calendar as an `NSTimeZone`. _(deprecated)_
- [NSEraCalendarUnit](unit/nseracalendarunit.md) — Specifies the era unit. _(deprecated)_
- [NSYearCalendarUnit](unit/nsyearcalendarunit.md) — Specifies the year unit. _(deprecated)_
- [NSMonthCalendarUnit](unit/nsmonthcalendarunit.md) — Specifies the month unit. _(deprecated)_
- [NSDayCalendarUnit](unit/nsdaycalendarunit.md) — Specifies the day unit. _(deprecated)_
- [NSHourCalendarUnit](unit/nshourcalendarunit.md) — Specifies the hour unit. _(deprecated)_
- [NSMinuteCalendarUnit](unit/nsminutecalendarunit.md) — Specifies the minute unit. _(deprecated)_
- [NSSecondCalendarUnit](unit/nssecondcalendarunit.md) — Specifies the second unit. _(deprecated)_
- [NSWeekCalendarUnit](unit/nsweekcalendarunit.md) — Specifies the week unit. _(deprecated)_
- [NSWeekdayCalendarUnit](unit/nsweekdaycalendarunit.md) — Specifies the weekday unit. _(deprecated)_
- [NSWeekdayOrdinalCalendarUnit](unit/nsweekdayordinalcalendarunit.md) — Specifies the ordinal weekday unit. _(deprecated)_
- [NSQuarterCalendarUnit](unit/nsquartercalendarunit.md) — Specifies the quarter unit. _(deprecated)_
- [NSWeekOfMonthCalendarUnit](unit/nsweekofmonthcalendarunit.md) — Specifies the original week of a month calendar unit. _(deprecated)_
- [NSWeekOfYearCalendarUnit](unit/nsweekofyearcalendarunit.md) — Specifies the original week of the year calendar unit. _(deprecated)_
- [NSYearForWeekOfYearCalendarUnit](unit/nsyearforweekofyearcalendarunit.md) — Specifies the year when the calendar is being interpreted as a week-based calendar. _(deprecated)_
- [NSCalendarCalendarUnit](unit/nscalendarcalendarunit.md) — Specifies the calendar of the calendar. _(deprecated)_
- [NSTimeZoneCalendarUnit](unit/nstimezonecalendarunit.md) — Specifies the time zone of the calendar as an `NSTimeZone`. _(deprecated)_

## See Also

### Getting Calendar Information

- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.
- [firstWeekday](firstweekday.md) — The index of the first weekday of the receiver.
- [locale](locale.md) — The locale of the receiver.
- [timeZone](timezone.md) — The time zone for the calendar.
- [- maximumRangeOfUnit:](<maximumrange(of_).md>) — Returns the maximum range limits of the values that a given unit can take on.
- [- minimumRangeOfUnit:](<minimumrange(of_).md>) — Returns the minimum range limits of the values that a given unit can take on.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The minimum number of days in the first week of the receiver.
- [- ordinalityOfUnit:inUnit:forDate:](<ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [- rangeOfUnit:inUnit:forDate:](<range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [- rangeOfUnit:startDate:interval:forDate:](<range(of_start_interval_for_).md>) — Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [- rangeOfWeekendStartDate:interval:containingDate:](<range(ofweekendstart_interval_containing_).md>) — Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
