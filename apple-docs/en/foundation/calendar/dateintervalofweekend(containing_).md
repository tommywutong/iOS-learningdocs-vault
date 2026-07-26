---
title: 'dateIntervalOfWeekend(containing:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/dateintervalofweekend(containing:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/dateintervalofweekend(containing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/dateintervalofweekend%28containing%3A%29.json'
content_hash: 'sha256:ea2498d8e348a2c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# dateIntervalOfWeekend(containing:)

<sub>Instance Method</sub>

Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateIntervalOfWeekend(containing date: Date) -> DateInterval?
```

## Parameters

- `date` — The date contained in the weekend.

## Return Value

A `DateInterval`, or `nil` if the date is not in a weekend.

## See Also

### Calculating Intervals

- [dateInterval(of:for:)](<dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateInterval(of:start:interval:for:)](<dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:start:interval:)](<dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:direction:)](<nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [nextWeekend(startingAfter:start:interval:direction:)](<nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [SearchDirection](searchdirection.md) — The direction in time to search.
