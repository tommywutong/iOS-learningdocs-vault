---
title: 'startOfDay(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/startofday(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/startofday(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/startofday%28for%3A%29.json'
content_hash: 'sha256:9e5cdc04a54cbffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# startOfDay(for:)

<sub>Instance Method</sub>

Returns the first moment of a given date as a date instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startOfDay(for date: Date) -> Date
```

## Parameters

- `date` — The date for which to perform the calculation.

## Return Value

An `NSDate` instance representing the first moment date of the given date.

## Discussion

For example, passing `[NSDate date]` for the `date` parameter would give you the start of “today.”

### Special Considerations

If there were two midnights, this method returns the first. If there was none, it returns the first moment that did exist.

## See Also

### Scanning Dates

- [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<enumeratedates(startingafter_matching_options_using_).md>) — Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [- nextDateAfterDate:matchingComponents:options:](<nextdate(after_matching_options_).md>) — Returns the next date after a given date matching the given components.
- [- nextDateAfterDate:matchingHour:minute:second:options:](<nextdate(after_matchinghour_minute_second_options_).md>) — Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [- nextDateAfterDate:matchingUnit:value:options:](<nextdate(after_matching_value_options_).md>) — Returns the next date after a given date matching the given calendar unit value.
- [Options](options.md) — The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md) — A legacy constant used to control overflow in date calculations.
