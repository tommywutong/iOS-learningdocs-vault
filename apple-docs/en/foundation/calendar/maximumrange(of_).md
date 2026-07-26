---
title: 'maximumRange(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/maximumrange(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/maximumrange(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/maximumrange%28of%3A%29.json'
content_hash: 'sha256:6ed602bfe2ed20b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# maximumRange(of:)

<sub>Instance Method</sub>

The maximum range limits of the values that a given component can take on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maximumRange(of component: Calendar.Component) -> Range<Int>?
```

## Parameters

- `component` — A component to calculate a range for.

## Return Value

The range, or nil if it could not be calculated.

## Discussion

As an example, in the Gregorian calendar the maximum range of values for the Day component is 1-31.

## See Also

### Getting Calendar Information

- [identifier](identifier-swift.property.md) — The identifier of the calendar.
- [locale](locale.md) — The locale of the calendar.
- [firstWeekday](firstweekday.md) — The first day of the week for the calendar.
- [minimumDaysInFirstWeek](minimumdaysinfirstweek.md) — The number of minimum days in the first week.
- [timeZone](timezone.md) — The time zone of the calendar.
- [minimumRange(of:)](<minimumrange(of_).md>) — Returns the minimum range limits of the values that a given component can take on.
- [ordinality(of:in:for:)](<ordinality(of_in_for_).md>) — Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [range(of:in:for:)](<range(of_in_for_).md>) — Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.
