---
title: 'range(of:start:interval:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/range(of:start:interval:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/range(of:start:interval:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/range%28of%3Astart%3Ainterval%3Afor%3A%29.json'
content_hash: 'sha256:e4e10ab253dcf442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# range(of:start:interval:for:)

<sub>Instance Method</sub>

Returns by reference the starting time and duration of a given calendar unit that contains a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(of unit: NSCalendar.Unit, start datep: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval tip: UnsafeMutablePointer<TimeInterval>?, for date: Date) -> Bool
```

## Parameters

- `unit` — A calendar unit (see [Unit](unit.md) for possible values).

- `datep` — Upon return, contains the starting time of the calendar unit `unit` that contains the date `date`

- `tip` — Upon return, contains the duration of the calendar unit `unit` that contains the date `date`

- `date` — A date.

## Return Value

[true](../../swift/true.md) if the starting time and duration of a unit could be calculated, otherwise [false](../../swift/false.md).

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
- [- rangeOfWeekendStartDate:interval:containingDate:](<range(ofweekendstart_interval_containing_).md>) — Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [Unit](unit.md) — Calendrical units such as year, month, day and hour.
