---
title: 'nextWeekendStart(_:interval:options:after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/nextweekendstart(_:interval:options:after:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/nextweekendstart(_:interval:options:after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/nextweekendstart%28_%3Ainterval%3Aoptions%3Aafter%3A%29.json'
content_hash: 'sha256:02195a06f43ceffe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# nextWeekendStart(_:interval:options:after:)

<sub>Instance Method</sub>

Returns by reference the starting date and time interval range of the next weekend period after a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextWeekendStart(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval tip: UnsafeMutablePointer<TimeInterval>?, options: NSCalendar.Options = [], after date: Date) -> Bool
```

## Parameters

- `datep` — Upon return, contains the starting date of the next weekend period.

- `tip` — Upon return, contains the time interval of the next weekend period.

- `options` — Options for the calculation. If you specify a backward search option ([NSCalendarSearchBackwards](options/searchbackwards.md)), the starting date and time interval range of the preceding weekend period will be returned by reference instead.

- `date` — The date for which to perform the calculation.

## Return Value

[false](../../swift/false.md) if the calendar and locale do not have the concept of a weekend, otherwise [true](../../swift/true.md).

## Discussion

Note that a particular calendar day may not necessarily fall entirely within a weekend period, as weekends can start in the middle of a day in some calendars and locales.

## See Also

### Calculating Dates

- [- dateFromComponents:](<date(from_).md>) — Returns a date representing the absolute time calculated from given components.
- [- dateByAddingComponents:toDate:options:](<date(byadding_to_options_).md>) — Returns a date representing the absolute time calculated by adding given components to a given date.
- [- dateByAddingUnit:value:toDate:options:](<date(byadding_value_to_options_).md>) — Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [- dateBySettingHour:minute:second:ofDate:options:](<date(bysettinghour_minute_second_of_options_).md>) — Creates a new date calculated with the given time.
- [- dateBySettingUnit:value:ofDate:options:](<date(bysettingunit_value_of_options_).md>) — Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.
- [- dateWithEra:year:month:day:hour:minute:second:nanosecond:](<date(era_year_month_day_hour_minute_second_nanosecond_).md>) — Returns a date created with the given components.
- [- dateWithEra:yearForWeekOfYear:weekOfYear:weekday:hour:minute:second:nanosecond:](<date(era_yearforweekofyear_weekofyear_weekday_hour_minute_second_nanosecond_).md>) — Returns a new date created with the given components base on a week-of-year value.
