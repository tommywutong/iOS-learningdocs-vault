---
title: era
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/era
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/era'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/era.json'
content_hash: 'sha256:2144e8a6e26e4819'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# era

<sub>Instance Property</sub>

The number of eras.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var era: Int { get set }
```

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Years and Months

- [year](year.md) — The number of years.
- [yearForWeekOfYear](yearforweekofyear.md) — The ISO 8601 week-numbering year.
- [quarter](quarter.md) — The number of quarters.
- [month](month.md) — The number of months.
- [leapMonth](isleapmonth.md) — A Boolean value that indicates whether the month is a leap month.
