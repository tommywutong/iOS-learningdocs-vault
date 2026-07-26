---
title: 'components(_:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/components(_:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/components(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/components%28_%3Afrom%3A%29.json'
content_hash: 'sha256:f6e68b8390211c27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# components(_:from:)

<sub>Instance Method</sub>

Returns the date components representing a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components(_ unitFlags: NSCalendar.Unit, from date: Date) -> DateComponents
```

## Parameters

- `unitFlags` — The components into which to decompose `date`.

- `date` — The date for which to perform the calculation.

## Return Value

An `NSDateComponents` object containing `date` decomposed into the components specified by `unitFlags`. Returns `nil` if `date` falls outside of the defined range of the receiver or if the computation cannot be performed.

## Discussion

The Weekday ordinality, when requested, refers to the next larger (than Week) of the requested units. Some computations can take a relatively long time.

The following example shows how to use this method to determine the current year, month, and day, using an existing calendar (`gregorian`):

```objc
unsigned unitFlags = NSYearCalendarUnit | NSMonthCalendarUnit |  NSDayCalendarUnit;
NSDate *date = [NSDate date];
NSDateComponents *comps = [gregorian components:unitFlags fromDate:date];
```

## See Also

### Related Documentation

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingComponents:toDate:options:](<date(byadding_to_options_).md>) — Returns a date representing the absolute time calculated by adding given components to a given date.

### Extracting Components

- [- date:matchesComponents:](<date(__matchescomponents_).md>) — Returns whether a given date matches all of the given date components.
- [- component:fromDate:](<component(__from_).md>) — Returns the specified date component from a given date.
- [- components:fromDate:toDate:options:](<components(__from_to_options_)-84y5w.md>) — Returns the difference between two supplied dates as date components.
- [- components:fromDateComponents:toDateComponents:options:](<components(__from_to_options_)-49lo8.md>) — Returns the difference between start and end dates given as date components.
- [- componentsInTimeZone:fromDate:](<components(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [- getEra:year:month:day:fromDate:](<getera(__year_month_day_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getEra:yearForWeekOfYear:weekOfYear:weekday:fromDate:](<getera(__yearforweekofyear_weekofyear_weekday_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getHour:minute:second:nanosecond:fromDate:](<gethour(__minute_second_nanosecond_from_).md>) — Returns by reference the hour, minute, second, and nanosecond component values for a given date.
