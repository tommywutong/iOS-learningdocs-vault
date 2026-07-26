---
title: 'dateInterval(of:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/dateinterval(of:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/dateinterval(of:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/dateinterval%28of%3Afor%3A%29.json'
content_hash: 'sha256:6d98d28ce8f369c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dateInterval(of:for:)

<sub>Instance Method</sub>

Returns the starting time and duration of a given calendar component that contains a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateInterval(of component: Calendar.Component, for date: Date) -> DateInterval?
```

## Parameters

- `component` — A calendar component.

- `date` — The specified date.

## Return Value

A new `DateInterval` if the starting time and duration of a component could be calculated; otherwise, `nil`.

## See Also

### Calculating Intervals

- [dateInterval(of:start:interval:for:)](<dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [dateIntervalOfWeekend(containing:start:interval:)](<dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:direction:)](<nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [nextWeekend(startingAfter:start:interval:direction:)](<nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [SearchDirection](searchdirection.md) — The direction in time to search.
