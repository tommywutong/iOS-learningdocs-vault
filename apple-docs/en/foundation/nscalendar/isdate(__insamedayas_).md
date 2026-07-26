---
title: 'isDate(_:inSameDayAs:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/isdate(_:insamedayas:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/isdate(_:insamedayas:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/isdate%28_%3Ainsamedayas%3A%29.json'
content_hash: 'sha256:7e6610f57f078189'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# isDate(_:inSameDayAs:)

<sub>Instance Method</sub>

Indicates whether two dates are in the same day.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDate(_ date1: Date, inSameDayAs date2: Date) -> Bool
```

## Parameters

- `date1` — The first date to compare.

- `date2` — The second date to compare.

## Return Value

[true](../../swift/true.md) if both dates are within the same day, otherwise [false](../../swift/false.md).

## See Also

### Comparing Dates

- [- compareDate:toDate:toUnitGranularity:](<compare(__to_tounitgranularity_).md>) — Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [- isDate:equalToDate:toUnitGranularity:](<isdate(__equalto_tounitgranularity_).md>) — Indicates whether two dates are equal to a given unit of granularity.
- [- isDateInToday:](<isdateintoday(__).md>) — Indicates whether the given date is in “today.”
- [- isDateInTomorrow:](<isdateintomorrow(__).md>) — Indicates whether the given date is in “tomorrow.”
- [- isDateInWeekend:](<isdateinweekend(__).md>) — Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [- isDateInYesterday:](<isdateinyesterday(__).md>) — Indicates whether the given date is in “yesterday.”
