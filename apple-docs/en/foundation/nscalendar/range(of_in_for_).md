---
title: 'range(of:in:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/range(of:in:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/range(of:in:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/range%28of%3Ain%3Afor%3A%29.json'
content_hash: 'sha256:701c1dbab4624898'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# range(of:in:for:)

<sub>Instance Method</sub>

Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(of smaller: NSCalendar.Unit, in larger: NSCalendar.Unit, for date: Date) -> NSRange
```

## Parameters

- `smaller` — The smaller calendar unit.

- `larger` — The larger calendar unit.

- `date` — The absolute time for which the calculation is performed.

## Return Value

The range of absolute time values `smaller` can take on in `larger` at the time specified by `date`. Returns `{NSNotFound, NSNotFound`} if `larger` is not logically bigger than `smaller` in the calendar, or the given combination of units does not make sense (or is a computation which is undefined).

## Discussion

You can use this method to calculate, for example, the range the Day unit can take on in the Month in which `date` lies.

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
- [- rangeOfUnit:startDate:interval:forDate:](<range(of_start_interval_for_).md>) — Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [- rangeOfWeekendStartDate:interval:containingDate:](<range(ofweekendstart_interval_containing_).md>) — Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [Unit](unit.md) — Calendrical units such as year, month, day and hour.
