---
title: 'dateInterval(of:start:interval:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/dateinterval(of:start:interval:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/dateinterval(of:start:interval:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/dateinterval%28of%3Astart%3Ainterval%3Afor%3A%29.json'
content_hash: 'sha256:e6dd4122179a2848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dateInterval(of:start:interval:for:)

<sub>Instance Method</sub>

Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateInterval(of component: Calendar.Component, start: inout Date, interval: inout TimeInterval, for date: Date) -> Bool
```

## Parameters

- `component` — A calendar component.

- `start` — Upon return, the starting time of the calendar component that contains the date.

- `interval` — Upon return, the duration of the calendar component that contains the date.

- `date` — The specified date.

## Return Value

`true` if the starting time and duration of a component could be calculated; otherwise, `false`.

## See Also

### Calculating Intervals

- [dateInterval(of:for:)](<dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [dateIntervalOfWeekend(containing:start:interval:)](<dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:direction:)](<nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [nextWeekend(startingAfter:start:interval:direction:)](<nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [SearchDirection](searchdirection.md) — The direction in time to search.
