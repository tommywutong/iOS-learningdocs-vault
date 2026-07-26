---
title: 'range(ofWeekendStart:interval:containing:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/range(ofweekendstart:interval:containing:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/range(ofweekendstart:interval:containing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/range%28ofweekendstart%3Ainterval%3Acontaining%3A%29.json'
content_hash: 'sha256:23f73c23fa90e7a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# range(ofWeekendStart:interval:containing:)

<sub>Instance Method</sub>

Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(ofWeekendStart datep: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval tip: UnsafeMutablePointer<TimeInterval>?, containing date: Date) -> Bool
```

## Parameters

- `datep` — Upon return, contains the starting date of the next weekend period.

- `tip` — Upon return, contains the time interval of the next weekend period.

- `date` — The date to use to perform the calculation.

## Return Value

[true](../../swift/true.md) if the given date falls within a weekend period, otherwise [false](../../swift/false.md).

## Discussion

Note that a particular calendar day may not necessarily fall entirely within a weekend period, as weekends can start in the middle of a day in some calendars and locales.

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
- [Unit](unit.md) — Calendrical units such as year, month, day and hour.
