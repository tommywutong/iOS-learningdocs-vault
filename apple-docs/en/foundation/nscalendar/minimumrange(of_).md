---
title: 'minimumRange(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/minimumrange(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/minimumrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/minimumrange%28of%3A%29.json'
content_hash: 'sha256:7f165629ab18d9cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# minimumRange(of:)

<sub>Instance Method</sub>

Returns the minimum range limits of the values that a given unit can take on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func minimumRange(of unit: NSCalendar.Unit) -> NSRange
```

## Parameters

- `unit` — The unit for which the maximum range is returned.

## Return Value

The minimum range limits of the values that the unit specified by `unit` can take on in the receiver.

## Discussion

As an example, in the Gregorian calendar the minimum range of values for the Day unit is 1-28.

## See Also

### Getting Calendar Information

- [calendarIdentifier](calendaridentifier.md) — An identifier for the calendar.
- [firstWeekday](firstweekday.md) — The index of the first weekday of the receiver.
- [locale](locale.md) — The locale of the receiver.
- [timeZone](timezone.md) — The time zone for the calendar.
- [- maximumRangeOfUnit:](<maximumrange(of_).md>) — Returns the maximum range limits of the values that a given unit can take on.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The minimum number of days in the first week of the receiver.
- [- ordinalityOfUnit:inUnit:forDate:](<ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [- rangeOfUnit:inUnit:forDate:](<range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [- rangeOfUnit:startDate:interval:forDate:](<range(of_start_interval_for_).md>) — Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [- rangeOfWeekendStartDate:interval:containingDate:](<range(ofweekendstart_interval_containing_).md>) — Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [Unit](unit.md) — Calendrical units such as year, month, day and hour.
