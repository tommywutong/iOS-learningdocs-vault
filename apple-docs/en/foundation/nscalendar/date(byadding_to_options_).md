---
title: 'date(byAdding:to:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/date(byadding:to:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/date(byadding:to:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/date%28byadding%3Ato%3Aoptions%3A%29.json'
content_hash: 'sha256:d764cd4bdffb31fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# date(byAdding:to:options:)

<sub>Instance Method</sub>

Returns a date representing the absolute time calculated by adding given components to a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(byAdding comps: DateComponents, to date: Date, options opts: NSCalendar.Options = []) -> Date?
```

## Parameters

- `comps` — The components to add to `date`.

- `date` — The date to which `comps` are added.

- `opts` — Options for the calculation. See [Options](options.md) for possible values. If you specify no options, overflow in a unit carries into the higher units (as in typical addition).

## Return Value

A new `NSDate` object representing the absolute time calculated by adding to `date` the calendrical components specified by `comps` using the options specified by `opts`. Returns `nil` if `date` falls outside the defined range of the receiver or if the computation cannot be performed.

## Discussion

Some operations can be ambiguous, and the behavior of the computation is calendar-specific, but generally components are added in the order specified.

The following example shows how to add 2 months and 3 days to the current date and time using an existing calendar (`gregorian`):

```objc
NSDate *currentDate = [NSDate date];
NSDateComponents *comps = [[NSDateComponents alloc] init];
[comps setMonth:2];
[comps setDay:3];
NSDate *date = [gregorian dateByAddingComponents:comps toDate:currentDate options:0];
[comps release];
```

Note that some computations can take a relatively long time.

## See Also

### Related Documentation

- [- components:fromDate:toDate:options:](<components(__from_to_options_)-84y5w.md>) — Returns the difference between two supplied dates as date components.

### Calculating Dates

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingUnit:value:toDate:options:](<date(byadding_value_to_options_).md>) — Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [- dateBySettingHour:minute:second:ofDate:options:](<date(bysettinghour_minute_second_of_options_).md>) — Creates a new date calculated with the given time.
- [- dateBySettingUnit:value:ofDate:options:](<date(bysettingunit_value_of_options_).md>) — Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.
- [- dateWithEra:year:month:day:hour:minute:second:nanosecond:](<date(era_year_month_day_hour_minute_second_nanosecond_).md>) — Returns a date created with the given components.
- [- dateWithEra:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:](<date(era_yearforweekofyear_weekofyear_weekday_hour_minute_second_nanosecond_).md>) — Returns a new date created with the given components base on a week-of-year value.
- [- nextWeekendStartDate:interval:options:afterDate:](<nextweekendstart(__interval_options_after_).md>) — Returns by reference the starting date and time interval range of the next weekend period after a given date.
