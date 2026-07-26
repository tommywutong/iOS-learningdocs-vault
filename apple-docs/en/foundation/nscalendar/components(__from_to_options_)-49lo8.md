---
title: 'components(_:from:to:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/components(_:from:to:options:)-49lo8'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/components(_:from:to:options:)-49lo8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/components%28_%3Afrom%3Ato%3Aoptions%3A%29-49lo8.json'
content_hash: 'sha256:61d9f2c66ede8d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# components(_:from:to:options:)

<sub>Instance Method</sub>

Returns the difference between start and end dates given as date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components(_ unitFlags: NSCalendar.Unit, from startingDateComp: DateComponents, to resultDateComp: DateComponents, options: NSCalendar.Options = []) -> DateComponents
```

## Parameters

- `unitFlags` — Specifies the components for the returned `NSDateComponents` object.

- `startingDateComp` — The start date for the calculation as an `NSDateComponents` object.

- `resultDateComp` — The end date for the calculation as an `NSDateComponents` object.

- `options` — The `options` parameter is currently unused.

## Return Value

An `NSDateComponents` object whose components are specified by `unitFlags` and calculated from the difference between the `startingDateComp` and `resultDateComp` using the options specified by `options`. Returns `nil` if either date falls outside the defined range of the receiver or if the computation cannot be performed.

## Discussion

If an `NSDateComponents` object does not specify a value for a calendar unit required to determine an absolute date, the base value of that unit is assumed. For example, given an `NSDateComponents` object with only a `year` and a `month` specified, the resulting `NSDate` object would be constructed using a `day` value of `1` and `hour`, `minute`, `second` and `nanosecond` values of `0`. Passing an `NSDateComponents` argument with an unspecified `era` or `year` value is not advised.

If an `NSDateComponents` object’s `timeZone` property is set, the time zone property value will be used in the calculation. If an `NSDateComponents` object’s `calendar` property is set, the calendar property value will be used instead of the receiving calendar. If both an `NSDateComponents` object’s `timeZone` and `calendar` properties are set, the time zone property value overrides the time zone of the calendar property value.

## See Also

### Extracting Components

- [- date:matchesComponents:](<date(__matchescomponents_).md>) — Returns whether a given date matches all of the given date components.
- [- component:fromDate:](<component(__from_).md>) — Returns the specified date component from a given date.
- [- components:fromDate:](<components(__from_).md>) — Returns the date components representing a given date.
- [- components:fromDate:toDate:options:](<components(__from_to_options_)-84y5w.md>) — Returns the difference between two supplied dates as date components.
- [- componentsInTimeZone:fromDate:](<components(in_from_).md>) — Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [- getEra:year:month:day:fromDate:](<getera(__year_month_day_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getEra:yearForWeekOfYear:weekOfYear:weekday:fromDate:](<getera(__yearforweekofyear_weekofyear_weekday_from_).md>) — Returns by reference the era, year, week of year, and weekday component values for a given date.
- [- getHour:minute:second:nanosecond:fromDate:](<gethour(__minute_second_nanosecond_from_).md>) — Returns by reference the hour, minute, second, and nanosecond component values for a given date.
