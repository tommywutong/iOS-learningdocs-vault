---
title: 'date(era:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/date(era:yearforweekofyear:weekofyear:weekday:hour:minute:second:nanosecond:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/date(era:yearforweekofyear:weekofyear:weekday:hour:minute:second:nanosecond:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/date%28era%3Ayearforweekofyear%3Aweekofyear%3Aweekday%3Ahour%3Aminute%3Asecond%3Ananosecond%3A%29.json'
content_hash: 'sha256:bd00c4dee1b47b18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# date(era:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:)

<sub>Instance Method</sub>

Returns a new date created with the given components base on a week-of-year value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(era eraValue: Int, yearForWeekOfYear yearValue: Int, weekOfYear weekValue: Int, weekday weekdayValue: Int, hour hourValue: Int, minute minuteValue: Int, second secondValue: Int, nanosecond nanosecondValue: Int) -> Date?
```

## Parameters

- `eraValue` — The value for the era component.

- `yearValue` — The value for the year component.

- `weekValue` — The value for the week-of-year component.

- `weekdayValue` — The value to use as the weekday.

- `hourValue` — The value for the hour component.

- `minuteValue` — The value for the minute component.

- `secondValue` — The value for the second component.

- `nanosecondValue` — The value for the nanosecond component.

## Return Value

A new `NSDate` instance created with the given components based on a week-of-year calculation, or `nil` if the components do not correspond to a valid date.

## See Also

### Calculating Dates

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingComponents:toDate:options:](<date(byadding_to_options_).md>) — Returns a date representing the absolute time calculated by adding given components to a given date.
- [- dateByAddingUnit:value:toDate:options:](<date(byadding_value_to_options_).md>) — Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [- dateBySettingHour:minute:second:ofDate:options:](<date(bysettinghour_minute_second_of_options_).md>) — Creates a new date calculated with the given time.
- [- dateBySettingUnit:value:ofDate:options:](<date(bysettingunit_value_of_options_).md>) — Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.
- [- dateWithEra:year:month:day:hour:minute:second:nanosecond:](<date(era_year_month_day_hour_minute_second_nanosecond_).md>) — Returns a date created with the given components.
- [- nextWeekendStartDate:interval:options:afterDate:](<nextweekendstart(__interval_options_after_).md>) — Returns by reference the starting date and time interval range of the next weekend period after a given date.
