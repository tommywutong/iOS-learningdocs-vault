---
title: 'range(of:in:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/range(of:in:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/range(of:in:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/range%28of%3Ain%3Afor%3A%29.json'
content_hash: 'sha256:1cbaff64ae03a6b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# range(of:in:for:)

<sub>Instance Method</sub>

Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range(of smaller: Calendar.Component, in larger: Calendar.Component, for date: Date) -> Range<Int>?
```

## Parameters

- `smaller` — The smaller calendar component.

- `larger` — The larger calendar component.

- `date` — The absolute time for which the calculation is performed.

## Return Value

The range of absolute time values smaller can take on in larger at the time specified by date. Returns `nil` if larger is not logically bigger than smaller in the calendar, or the given combination of components does not make sense (or is a computation which is undefined).

## Discussion

You can use this method to calculate, for example, the range the `day` component can take on in the `month` in which `date` lies.

## See Also

### Getting Calendar Information

- [identifier](identifier-swift.property.md) — The identifier of the calendar.
- [locale](locale.md) — The locale of the calendar.
- [firstWeekday](firstweekday.md) — The first day of the week for the calendar.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The number of minimum days in the first week.
- [timeZone](timezone.md) — The time zone of the calendar.
- [maximumRange(of:)](<maximumrange(of_).md>) — The maximum range limits of the values that a given component can take on.
- [minimumRange(of:)](<minimumrange(of_).md>) — Returns the minimum range limits of the values that a given component can take on.
- [ordinality(of:in:for:)](<ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
