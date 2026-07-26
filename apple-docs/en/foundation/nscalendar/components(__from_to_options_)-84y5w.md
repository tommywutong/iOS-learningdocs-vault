---
title: 'components(_:from:to:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/components(_:from:to:options:)-84y5w'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/components(_:from:to:options:)-84y5w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/components%28_%3Afrom%3Ato%3Aoptions%3A%29-84y5w.json'
content_hash: 'sha256:5db0f7c128153c86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# components(_:from:to:options:)

<sub>Instance Method</sub>

Returns the difference between two supplied dates as date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components(_ unitFlags: NSCalendar.Unit, from startingDate: Date, to resultDate: Date, options opts: NSCalendar.Options = []) -> DateComponents
```

## Parameters

- `unitFlags` — Specifies the components for the returned `NSDateComponents` object.

- `startingDate` — The start date for the calculation.

- `resultDate` — The end date for the calculation.

- `opts` — Options for the calculation.  For possible values, see [Options](options.md). If you specify a “wrap” option ([NSCalendarWrapComponents](options/wrapcomponents.md)), the specified components are incremented and wrap around to zero/one on overflow, but do not cause higher units to be incremented. When the wrap option is not specified, overflow in a unit carries into the higher units, as in typical addition.

## Return Value

An `NSDateComponents` object whose components are specified by `unitFlags` and calculated from the difference between the `resultDate` and `startDate` using the options specified by `options`. Returns `nil` if either date falls outside the defined range of the receiver or if the computation cannot be performed.

## Discussion

The result is lossy if there is not a small enough unit requested to hold the full precision of the difference. Some operations can be ambiguous, and the behavior of the computation is calendar-specific, but generally larger components will be computed before smaller components; for example, in the Gregorian calendar a result might be 1 month and 5 days instead of, for example, 0 months and 35 days. The resulting component values may be negative if `resultDate` is before `startDate`.

The following example shows how to get the approximate number of months and days between two dates using an existing calendar (`gregorian`):

```objc
NSDate *startDate = ...;
NSDate *endDate = ...;
unsigned int unitFlags = NSMonthCalendarUnit | NSDayCalendarUnit;
NSDateComponents *comps = [gregorian components:unitFlags fromDate:startDate  toDate:endDate  options:0];
int months = [comps month];
int days = [comps day];
```

Note that some computations can take a relatively long time.

## See Also

### Related Documentation

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingComponents:toDate:options:](<date(byadding_to_options_).md>) — Returns a date representing the absolute time calculated by adding given components to a given date.

### Extracting Components

- [- date:matchesComponents:](<date(__matchescomponents_).md>) — Returns whether a given date matches all of the given date components.
- [- component:fromDate:](<component(__from_).md>) — Returns the specified date component from a given date.
- [- components:fromDate:](<components(__from_).md>) — Returns the date components representing a given date.
- [- components:fromDateComponents:toDateComponents:options:](<components(__from_to_options_)-49lo8.md>) — Returns the difference between start and end dates given as date components.
- [- componentsInTimeZone:fromDate:](<components(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [- getEra:year:month:day:fromDate:](<getera(__year_month_day_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getEra:yearForWeekOfYear:weekOfYear:weekday:fromDate:](<getera(__yearforweekofyear_weekofyear_weekday_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getHour:minute:second:nanosecond:fromDate:](<gethour(__minute_second_nanosecond_from_).md>) — Returns by reference the hour, minute, second, and nanosecond component values for a given date.
