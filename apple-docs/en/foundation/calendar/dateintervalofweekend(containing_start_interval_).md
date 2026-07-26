---
title: 'dateIntervalOfWeekend(containing:start:interval:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/dateintervalofweekend(containing:start:interval:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/dateintervalofweekend(containing:start:interval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/dateintervalofweekend%28containing%3Astart%3Ainterval%3A%29.json'
content_hash: 'sha256:5a848365be3c484f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dateIntervalOfWeekend(containing:start:interval:)

<sub>Instance Method</sub>

Find the range of the weekend around the given date, returned via two by-reference parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateIntervalOfWeekend(containing date: Date, start: inout Date, interval: inout TimeInterval) -> Bool
```

## Parameters

- `date` — The date at which to start the search.

- `start` — When the result is `true`, set

## Return Value

`true` if a date range could be found, and `false` if the date is not in a weekend.

## Discussion

Note that a given entire day within a calendar is not necessarily all in a weekend or not; weekends can start in the middle of a day in some calendars and locales.

## See Also

### Calculating Intervals

- [dateInterval(of:for:)](<dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateInterval(of:start:interval:for:)](<dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [nextWeekend(startingAfter:direction:)](<nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [nextWeekend(startingAfter:start:interval:direction:)](<nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [SearchDirection](searchdirection.md) — The direction in time to search.
