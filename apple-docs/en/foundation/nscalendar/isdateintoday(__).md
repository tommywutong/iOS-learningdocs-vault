---
title: 'isDateInToday(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/isdateintoday(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/isdateintoday(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/isdateintoday%28_%3A%29.json'
content_hash: 'sha256:0840269e3f9e0982'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# isDateInToday(_:)

<sub>Instance Method</sub>

Indicates whether the given date is in “today.”

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDateInToday(_ date: Date) -> Bool
```

## Parameters

- `date` — The date for which to perform the calculation.

## Return Value

[true](../../swift/true.md) if the given date is in “today,” otherwise [false](../../swift/false.md).

## See Also

### Comparing Dates

- [- compareDate:toDate:toUnitGranularity:](<compare(__to_tounitgranularity_).md>) — Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [- isDate:equalToDate:toUnitGranularity:](<isdate(__equalto_tounitgranularity_).md>) — Indicates whether two dates are equal to a given unit of granularity.
- [- isDate:inSameDayAsDate:](<isdate(__insamedayas_).md>) — Indicates whether two dates are in the same day.
- [- isDateInTomorrow:](<isdateintomorrow(__).md>) — Indicates whether the given date is in “tomorrow.”
- [- isDateInWeekend:](<isdateinweekend(__).md>) — Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [- isDateInYesterday:](<isdateinyesterday(__).md>) — Indicates whether the given date is in “yesterday.”
