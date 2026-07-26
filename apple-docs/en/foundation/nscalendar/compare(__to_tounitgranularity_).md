---
title: 'compare(_:to:toUnitGranularity:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscalendar/compare(_:to:tounitgranularity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/compare(_:to:tounitgranularity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/compare%28_%3Ato%3Atounitgranularity%3A%29.json'
content_hash: 'sha256:bd643b9248c884d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCalendar](../nscalendar.md)

# compare(_:to:toUnitGranularity:)

<sub>Instance Method</sub>

Indicates the ordering of two given dates based on their components down to a given unit granularity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ date1: Date, to date2: Date, toUnitGranularity unit: NSCalendar.Unit) -> ComparisonResult
```

## Parameters

- `date1` — The first date to compare.

- `date2` — The second date to compare.

- `unit` — The smallest unit that must, along with all larger units, be equal for the given dates to be considered the same. For possible values, see [Unit](unit.md).

## Return Value

`NSOrderedSame` if the dates are the same down to the given granularity, otherwise `NSOrderedAscending` or `NSOrderedDescending`.

## See Also

### Comparing Dates

- [- isDate:equalToDate:toUnitGranularity:](<isdate(__equalto_tounitgranularity_).md>) — Indicates whether two dates are equal to a given unit of granularity.
- [- isDate:inSameDayAsDate:](<isdate(__insamedayas_).md>) — Indicates whether two dates are in the same day.
- [- isDateInToday:](<isdateintoday(__).md>) — Indicates whether the given date is in “today.”
- [- isDateInTomorrow:](<isdateintomorrow(__).md>) — Indicates whether the given date is in “tomorrow.”
- [- isDateInWeekend:](<isdateinweekend(__).md>) — Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [- isDateInYesterday:](<isdateinyesterday(__).md>) — Indicates whether the given date is in “yesterday.”
