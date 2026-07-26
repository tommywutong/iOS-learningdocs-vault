---
title: 'nextWeekend(startingAfter:direction:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/nextweekend(startingafter:direction:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/nextweekend(startingafter:direction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/nextweekend%28startingafter%3Adirection%3A%29.json'
content_hash: 'sha256:cef85493cdb3c17f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# nextWeekend(startingAfter:direction:)

<sub>Instance Method</sub>

Returns a `DateInterval` of the next weekend, which starts strictly after the given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextWeekend(startingAfter date: Date, direction: Calendar.SearchDirection = .forward) -> DateInterval?
```

## Parameters

- `date` — The date at which to begin the search.

- `direction` — Which direction in time to search. The default value is `.forward`.

## Return Value

A `DateInterval`, or `nil` if weekends do not exist in the specific calendar or locale.

## Discussion

If `direction` is `.backward`, then finds the previous weekend range strictly before the given date.

Note that a given entire day within a calendar is not necessarily all in a weekend or not; weekends can start in the middle of a day in some calendars and locales.

## See Also

### Calculating Intervals

- [dateInterval(of:for:)](<dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateInterval(of:start:interval:for:)](<dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [dateIntervalOfWeekend(containing:start:interval:)](<dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:start:interval:direction:)](<nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [SearchDirection](searchdirection.md) — The direction in time to search.
