---
title: 'date(bySettingUnit:value:of:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/date(bysettingunit:value:of:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/date(bysettingunit:value:of:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/date%28bysettingunit%3Avalue%3Aof%3Aoptions%3A%29.json'
content_hash: 'sha256:59e3d91360cbc8ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# date(bySettingUnit:value:of:options:)

<sub>Instance Method</sub>

Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(bySettingUnit unit: NSCalendar.Unit, value v: Int, of date: Date, options opts: NSCalendar.Options = []) -> Date?
```

## Parameters

- `unit` — The unit to set with the given value. For possible values, see [Unit](unit.md).

- `v` — The value to set for the given calendar unit.

- `date` — The date to use to perform the calculation.

- `opts` — Options for the calculation. For possible values, see [Options](options.md).

## Return Value

A new `NSDate` instance representing the date calculated by setting a specific component of a given date to a given value. If the unit already has that value, this may result in a date which is the same as the given date. If no such time exists for the specified components, the next available date is returned, which may be on a different calendar day.

## Discussion

Changing a component’s value often requires higher or coupled components to change as well. For example, setting the `weekday` to “Thursday” will require the `day` component to change its value, and possibly the `month` and `year` as well. You can use the [- nextDateAfterDate:matchingUnit:value:options:](<nextdate(after_matching_value_options_).md>) method to specify more precise behavior for determining the next or previous date for a given date component.

## See Also

### Related Documentation

- [- nextDateAfterDate:matchingUnit:value:options:](<nextdate(after_matching_value_options_).md>) — Returns the next date after a given date matching the given calendar unit value.

### Calculating Dates

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingComponents:toDate:options:](<date(byadding_to_options_).md>) — Returns a date representing the absolute time calculated by adding given components to a given date.
- [- dateByAddingUnit:value:toDate:options:](<date(byadding_value_to_options_).md>) — Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [- dateBySettingHour:minute:second:ofDate:options:](<date(bysettinghour_minute_second_of_options_).md>) — Creates a new date calculated with the given time.
- [- dateWithEra:year:month:day:hour:minute:second:nanosecond:](<date(era_year_month_day_hour_minute_second_nanosecond_).md>) — Returns a date created with the given components.
- [- dateWithEra:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:](<date(era_yearforweekofyear_weekofyear_weekday_hour_minute_second_nanosecond_).md>) — Returns a new date created with the given components base on a week-of-year value.
- [- nextWeekendStartDate:interval:options:afterDate:](<nextweekendstart(__interval_options_after_).md>) — Returns by reference the starting date and time interval range of the next weekend period after a given date.
