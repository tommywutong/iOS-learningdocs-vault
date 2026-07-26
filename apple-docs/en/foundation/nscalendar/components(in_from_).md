---
title: 'components(in:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/components(in:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/components(in:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/components%28in%3Afrom%3A%29.json'
content_hash: 'sha256:03a9562d1d30d377'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# components(in:from:)

<sub>Instance Method</sub>

Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components(in timezone: TimeZone, from date: Date) -> DateComponents
```

## Parameters

- `timezone` — The time zone to use when returning the components. This value overrides the time zone of the receiving `NSCalendar`.

- `date` — The date for which to perform the calculation.

## Return Value

An `NSDateComponents` object containing all the components from the given date, calculated using the given time zone.

## Discussion

If you want “date information in a given time zone” for the purpose to displaying it, you should use [DateFormatter](../dateformatter.md) to format the date.

## See Also

### Extracting Components

- [- date:matchesComponents:](<date(__matchescomponents_).md>) — Returns whether a given date matches all of the given date components.
- [- component:fromDate:](<component(__from_).md>) — Returns the specified date component from a given date.
- [- components:fromDate:](<components(__from_).md>) — Returns the date components representing a given date.
- [- components:fromDate:toDate:options:](<components(__from_to_options_)-84y5w.md>) — Returns the difference between two supplied dates as date components.
- [- components:fromDateComponents:toDateComponents:options:](<components(__from_to_options_)-49lo8.md>) — Returns the difference between start and end dates given as date components.
- [- getEra:year:month:day:fromDate:](<getera(__year_month_day_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getEra:yearForWeekOfYear:weekOfYear:weekday:fromDate:](<getera(__yearforweekofyear_weekofyear_weekday_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getHour:minute:second:nanosecond:fromDate:](<gethour(__minute_second_nanosecond_from_).md>) — Returns by reference the hour, minute, second, and nanosecond component values for a given date.
