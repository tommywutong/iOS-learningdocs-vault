---
title: 'nextWeekend(startingAfter:start:interval:direction:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/nextweekend(startingafter:start:interval:direction:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/nextweekend(startingafter:start:interval:direction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/nextweekend%28startingafter%3Astart%3Ainterval%3Adirection%3A%29.json'
content_hash: 'sha256:19df3f11a23ea4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# nextWeekend(startingAfter:start:interval:direction:)

<sub>Instance Method</sub>

Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextWeekend(startingAfter date: Date, start: inout Date, interval: inout TimeInterval, direction: Calendar.SearchDirection = .forward) -> Bool
```

## Parameters

- `date` — The date at which to begin the search.

- `start` — Upon return, the starting time of the calendar component that contains the date.

- `interval` — Upon return, the duration of the calendar component that contains the date.

- `direction` — Which direction in time to search. The default value is `.forward`.

## Return Value

`false` if the calendar and locale do not have the concept of a weekend, otherwise `true`.

## Discussion

If `direction` is `.backward`, then finds the previous weekend range strictly before the given date.

Note that a given entire day within a calendar is not necessarily all in a weekend or not; weekends can start in the middle of a day in some calendars and locales.

## See Also

### Calculating Intervals

- [dateInterval(of:for:)](<dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateInterval(of:start:interval:for:)](<dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [dateIntervalOfWeekend(containing:start:interval:)](<dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:direction:)](<nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [SearchDirection](searchdirection.md) — The direction in time to search.
