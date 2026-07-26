---
title: 'date(bySettingHour:minute:second:of:matchingPolicy:repeatedTimePolicy:direction:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/date(bysettinghour:minute:second:of:matchingpolicy:repeatedtimepolicy:direction:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/date(bysettinghour:minute:second:of:matchingpolicy:repeatedtimepolicy:direction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/date%28bysettinghour%3Aminute%3Asecond%3Aof%3Amatchingpolicy%3Arepeatedtimepolicy%3Adirection%3A%29.json'
content_hash: 'sha256:eecd4c184e8400bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# date(bySettingHour:minute:second:of:matchingPolicy:repeatedTimePolicy:direction:)

<sub>Instance Method</sub>

Returns a new `Date` representing the date calculated by setting hour, minute, and second to a given time on a specified `Date`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func date(bySettingHour hour: Int, minute: Int, second: Int, of date: Date, matchingPolicy: Calendar.MatchingPolicy = .nextTime, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, direction: Calendar.SearchDirection = .forward) -> Date?
```

## Parameters

- `hour` — A specified hour.

- `minute` — A specified minute.

- `second` — A specified second.

- `date` — The date to start calculation with.

- `matchingPolicy` — Specifies the technique the search algorithm uses to find results. Default value is `.nextTime`.

- `repeatedTimePolicy` — Specifies the behavior when multiple matches are found. Default value is `.first`.

- `direction` — Specifies the direction in time to search. Default is `.forward`.

## Return Value

A `Date` representing the result of the search, or `nil` if a result could not be found.

## Discussion

If no such time exists, the next available time is returned (which could, for example, be in a different day than the nominal target date). The intent is to return a date on the same day as the original date argument.  This may result in a date which is backward than the given date, of course.

## See Also

### Calculating Dates from Components

- [date(from:)](<date(from_).md>) — Returns a date created from the specified components.
- [date(byAdding:to:wrappingComponents:)](<date(byadding_to_wrappingcomponents_).md>) — Returns a new `Date` representing the date calculated by adding components to a given date.
- [date(byAdding:value:to:wrappingComponents:)](<date(byadding_value_to_wrappingcomponents_).md>) — Returns a new `Date` representing the date calculated by adding an amount of a specific component to a given date.
- [date(bySetting:value:of:)](<date(bysetting_value_of_).md>) — Returns a new `Date` representing the date calculated by setting a specific component to a given time, and trying to keep lower components the same.  If the component already has that value, this may result in a date which is the same as the given date.
