---
title: 'getHour(_:minute:second:nanosecond:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/gethour(_:minute:second:nanosecond:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/gethour(_:minute:second:nanosecond:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/gethour%28_%3Aminute%3Asecond%3Ananosecond%3Afrom%3A%29.json'
content_hash: 'sha256:1eae3408a26f1426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# getHour(_:minute:second:nanosecond:from:)

<sub>Instance Method</sub>

Returns by reference the hour, minute, second, and nanosecond component values for a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>?, minute minuteValuePointer: UnsafeMutablePointer<Int>?, second secondValuePointer: UnsafeMutablePointer<Int>?, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>?, from date: Date)
```

## Parameters

- `hourValuePointer` — Upon return, contains the hour of the given date.

- `minuteValuePointer` — Upon return, contains the minute of the given date.

- `secondValuePointer` — Upon return, contains the second of the given date.

- `nanosecondValuePointer` — Upon return, contains the nanosecond of the given date.

- `date` — The date for which to perform the calculation.

## Discussion

Pass `NULL` to ignore any individual component parameter.

This is a convenience method for getting the time components of a given date using [- components:fromDate:](<components(__from_).md>)

## See Also

### Extracting Components

- [- date:matchesComponents:](<date(__matchescomponents_).md>) — Returns whether a given date matches all of the given date components.
- [- component:fromDate:](<component(__from_).md>) — Returns the specified date component from a given date.
- [- components:fromDate:](<components(__from_).md>) — Returns the date components representing a given date.
- [- components:fromDate:toDate:options:](<components(__from_to_options_)-84y5w.md>) — Returns the difference between two supplied dates as date components.
- [- components:fromDateComponents:toDateComponents:options:](<components(__from_to_options_)-49lo8.md>) — Returns the difference between start and end dates given as date components.
- [- componentsInTimeZone:fromDate:](<components(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [- getEra:year:month:day:fromDate:](<getera(__year_month_day_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getEra:yearForWeekOfYear:weekOfYear:weekday:fromDate:](<getera(__yearforweekofyear_weekofyear_weekday_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
