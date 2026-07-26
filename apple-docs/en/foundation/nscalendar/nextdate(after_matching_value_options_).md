---
title: 'nextDate(after:matching:value:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/nextdate(after:matching:value:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/nextdate(after:matching:value:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/nextdate%28after%3Amatching%3Avalue%3Aoptions%3A%29.json'
content_hash: 'sha256:a6bc29938accff39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# nextDate(after:matching:value:options:)

<sub>Instance Method</sub>

Returns the next date after a given date matching the given calendar unit value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextDate(after date: Date, matching unit: NSCalendar.Unit, value: Int, options: NSCalendar.Options = []) -> Date?
```

## Parameters

- `date` — The date for which to perform the calculation.

- `unit` — The component to use. For possible values, see [Unit](unit.md).

- `value` — The value for the given component.

- `options` — Options for the calculation. For possible values, see [Options](options.md).

## Return Value

A new `NSDate` object.

## See Also

### Scanning Dates

- [- startOfDayForDate:](<startofday(for_).md>) — Returns the first moment of a given date as a date instance.
- [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<enumeratedates(startingafter_matching_options_using_).md>) — Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [- nextDateAfterDate:matchingComponents:options:](<nextdate(after_matching_options_).md>) — Returns the next date after a given date matching the given components.
- [- nextDateAfterDate:matchingHour:minute:second:options:](<nextdate(after_matchinghour_minute_second_options_).md>) — Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [Options](options.md) — The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md) — A legacy constant used to control overflow in date calculations.
