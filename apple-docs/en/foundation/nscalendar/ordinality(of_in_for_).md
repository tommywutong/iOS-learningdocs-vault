---
title: 'ordinality(of:in:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/ordinality(of:in:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/ordinality(of:in:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/ordinality%28of%3Ain%3Afor%3A%29.json'
content_hash: 'sha256:74566441e2c30bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# ordinality(of:in:for:)

<sub>Instance Method</sub>

Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ordinality(of smaller: NSCalendar.Unit, in larger: NSCalendar.Unit, for date: Date) -> Int
```

## Parameters

- `smaller` — The smaller calendar unit

- `larger` — The larger calendar unit

- `date` — The absolute time for which the calculation is performed

## Return Value

The ordinal number of `smaller` within `larger` at the time specified by `date`. Returns `NSNotFound` if `larger` is not logically bigger than `smaller` in the calendar, or the given combination of units does not make sense (or is a computation which is undefined).

## Discussion

The ordinality is in most cases not the same as the decomposed value of the unit. Typically return values are `1` and greater. For example, the time `00:45` is in the first hour of the day, and for units Hour and Day respectively, the result would be `1`. An exception is the week-in-month calculation, which returns `0` for days before the first week in the month containing the date.

Note that some computations can take a relatively long time.

## See Also

### Getting Calendar Information

- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.
- [firstWeekday](firstweekday.md) — The index of the first weekday of the receiver.
- [locale](locale.md) — The locale of the receiver.
- [timeZone](timezone.md) — The time zone for the calendar.
- [- maximumRangeOfUnit:](<maximumrange(of_).md>) — Returns the maximum range limits of the values that a given unit can take on.
- [- minimumRangeOfUnit:](<minimumrange(of_).md>) — Returns the minimum range limits of the values that a given unit can take on.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The minimum number of days in the first week of the receiver.
- [- rangeOfUnit:inUnit:forDate:](<range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [- rangeOfUnit:startDate:interval:forDate:](<range(of_start_interval_for_).md>) — Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [- rangeOfWeekendStartDate:interval:containingDate:](<range(ofweekendstart_interval_containing_).md>) — Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [Unit](unit.md) — Calendrical units such as year, month, day and hour.
