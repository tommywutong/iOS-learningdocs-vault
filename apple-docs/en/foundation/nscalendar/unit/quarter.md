---
title: quarter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscalendar/unit/quarter
source_url: 'https://developer.apple.com/documentation/foundation/nscalendar/unit/quarter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscalendar/unit/quarter.json'
content_hash: 'sha256:8c6bb9bbb7e66689'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSCalendar](../../nscalendar.md) · [Unit](../unit.md)

# quarter

<sub>Type Property</sub>

Identifier for the quarter of the calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var quarter: NSCalendar.Unit { get }
```

## Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitQuarter`.

> [!important] Important
> The `NSCalendarUnitQuarter` unit is largely unimplemented, and is not recommended for use.

## See Also

### Specifying Years and Months

- [NSCalendarUnitEra](era.md) — Identifier for the era unit.
- [NSCalendarUnitYear](year.md) — Identifier for the year unit.
- [NSCalendarUnitYearForWeekOfYear](yearforweekofyear.md) — Identifier for the week-counting year unit.
- [NSCalendarUnitMonth](month.md) — Identifier for the month unit.
- [NSCalendarUnitIsLeapMonth](isleapmonth.md) — Identifier for the time zone of a date components object.
