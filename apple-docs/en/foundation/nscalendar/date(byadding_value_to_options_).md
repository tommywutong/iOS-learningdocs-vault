---
title: 'date(byAdding:value:to:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/date(byadding:value:to:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/date(byadding:value:to:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/date%28byadding%3Avalue%3Ato%3Aoptions%3A%29.json'
content_hash: 'sha256:fa9874e2421606e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# date(byAdding:value:to:options:)

<sub>Instance Method</sub>

Returns a date representing the absolute time calculated by adding the value of a given component to a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(byAdding unit: NSCalendar.Unit, value: Int, to date: Date, options: NSCalendar.Options = []) -> Date?
```

## Parameters

- `unit` — The unit to use for the calculation. For possible values, see [Unit](unit.md).

- `value` — The value for the given unit.

- `date` — The date to use to perform the calculation.

- `options` — Options for the calculation. See [Options](options.md) for possible values. If you specify a “wrap” option ([NSCalendarWrapComponents](options/wrapcomponents.md)), the specified components are incremented and wrap around to zero/one on overflow, but do not cause higher units to be incremented. When the wrap option is false, overflow in a unit carries into the higher units, as in typical addition.

## Return Value

A new `NSDate` object representing the absolute time calculated by adding to `date` the `value` of the given calendrical `unit` using the options specified by `options`. Returns `nil` if `date` falls outside the defined range of the receiver or if the computation cannot be performed.

## See Also

### Calculating Dates

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingComponents:toDate:options:](<date(byadding_to_options_).md>) — Returns a date representing the absolute time calculated by adding given components to a given date.
- [- dateBySettingHour:minute:second:ofDate:options:](<date(bysettinghour_minute_second_of_options_).md>) — Creates a new date calculated with the given time.
- [- dateBySettingUnit:value:ofDate:options:](<date(bysettingunit_value_of_options_).md>) — Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.
- [- dateWithEra:year:month:day:hour:minute:second:nanosecond:](<date(era_year_month_day_hour_minute_second_nanosecond_).md>) — Returns a date created with the given components.
- [- dateWithEra:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:](<date(era_yearforweekofyear_weekofyear_weekday_hour_minute_second_nanosecond_).md>) — Returns a new date created with the given components base on a week-of-year value.
- [- nextWeekendStartDate:interval:options:afterDate:](<nextweekendstart(__interval_options_after_).md>) — Returns by reference the starting date and time interval range of the next weekend period after a given date.
