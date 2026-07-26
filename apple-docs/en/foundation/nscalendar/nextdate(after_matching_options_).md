---
title: 'nextDate(after:matching:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/nextdate(after:matching:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/nextdate(after:matching:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/nextdate%28after%3Amatching%3Aoptions%3A%29.json'
content_hash: 'sha256:887f2e29bdc7d991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# nextDate(after:matching:options:)

<sub>Instance Method</sub>

Returns the next date after a given date matching the given components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextDate(after date: Date, matching comps: DateComponents, options: NSCalendar.Options = []) -> Date?
```

## Parameters

- `date` — The date for which to perform the calculation.

- `comps` — The date components to match.

- `options` — Options for the calculation. For possible values, see [Options](options.md).

## Return Value

A new `NSDate` object.

## Discussion

To compute a sequence of dates, use the [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<enumeratedates(startingafter_matching_options_using_).md>) method instead of calling this method in a loop with the previous loop iteration’s result.

## See Also

### Scanning Dates

- [- startOfDayForDate:](<startofday(for_).md>) — Returns the first moment of a given date as a date instance.
- [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<enumeratedates(startingafter_matching_options_using_).md>) — Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [- nextDateAfterDate:matchingHour:minute:second:options:](<nextdate(after_matchinghour_minute_second_options_).md>) — Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [- nextDateAfterDate:matchingUnit:value:options:](<nextdate(after_matching_value_options_).md>) — Returns the next date after a given date matching the given calendar unit value.
- [Options](options.md) — The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md) — A legacy constant used to control overflow in date calculations.
