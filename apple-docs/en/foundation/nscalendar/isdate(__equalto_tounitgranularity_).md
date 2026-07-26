---
title: 'isDate(_:equalTo:toUnitGranularity:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/isdate(_:equalto:tounitgranularity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/isdate(_:equalto:tounitgranularity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/isdate%28_%3Aequalto%3Atounitgranularity%3A%29.json'
content_hash: 'sha256:c0c16a7c736e1004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# isDate(_:equalTo:toUnitGranularity:)

<sub>Instance Method</sub>

Indicates whether two dates are equal to a given unit of granularity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDate(_ date1: Date, equalTo date2: Date, toUnitGranularity unit: NSCalendar.Unit) -> Bool
```

## Parameters

- `date1` — The first date to compare.

- `date2` — The second date to compare.

- `unit` — The smallest unit that must, along with all larger units, be equal in the given dates. For possible values, see [Unit](unit.md).

## Return Value

[true](../../swift/true.md) if both dates have equal date component for all units greater than or equal to the given unit, otherwise [false](../../swift/false.md).

## See Also

### Comparing Dates

- [- compareDate:toDate:toUnitGranularity:](<compare(__to_tounitgranularity_).md>) — Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [- isDate:inSameDayAsDate:](<isdate(__insamedayas_).md>) — Indicates whether two dates are in the same day.
- [- isDateInToday:](<isdateintoday(__).md>) — Indicates whether the given date is in “today.”
- [- isDateInTomorrow:](<isdateintomorrow(__).md>) — Indicates whether the given date is in “tomorrow.”
- [- isDateInWeekend:](<isdateinweekend(__).md>) — Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [- isDateInYesterday:](<isdateinyesterday(__).md>) — Indicates whether the given date is in “yesterday.”
