---
title: weekdayOrdinal
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/weekdayordinal
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/weekdayordinal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/weekdayordinal.json'
content_hash: 'sha256:e9bd46e531361362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# weekdayOrdinal

<sub>Instance Property</sub>

A weekday ordinal or count of weekday ordinals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var weekdayOrdinal: Int? { get set }
```

## Discussion

Weekday ordinal units represent the position of the weekday within the next larger calendar unit, such as the month. For example, 2 is the weekday ordinal unit for the second Friday of the month.

> [!note] Note
> This value is interpreted in the context of the calendar in which it is used.

## See Also

### Accessing Weeks and Days

- [weekOfMonth](weekofmonth.md) — A week of the month or a count of weeks of the month.
- [weekOfYear](weekofyear.md) — A week of the year or count of the weeks of the year.
- [weekday](weekday.md) — A weekday or count of weekdays.
- [day](day.md) — A day or count of days.
