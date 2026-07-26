---
title: CFCalendarUnit
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcalendarunit
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendarunit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendarunit.json'
content_hash: 'sha256:863859d8cec65c83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendarUnit

<sub>Structure</sub>

CFCalendarUnit constants are used to specify calendrical units, such as day or month, in various calendar calculations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFCalendarUnit
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFCalendarUnitEra](cfcalendarunit/era.md) — Specifies the era unit.
- [kCFCalendarUnitYear](cfcalendarunit/year.md) — Specifies the year unit.
- [kCFCalendarUnitMonth](cfcalendarunit/month.md) — Specifies the month unit.
- [kCFCalendarUnitDay](cfcalendarunit/day.md) — Specifies the day unit.
- [kCFCalendarUnitHour](cfcalendarunit/hour.md) — Specifies the hour unit.
- [kCFCalendarUnitMinute](cfcalendarunit/minute.md) — Specifies the minute unit.
- [kCFCalendarUnitSecond](cfcalendarunit/second.md) — Specifies the second unit.
- [kCFCalendarUnitWeek](cfcalendarunit/week.md) — Specifies the week unit. _(deprecated)_
- [kCFCalendarUnitWeekday](cfcalendarunit/weekday.md) — Specifies the weekday unit.
- [kCFCalendarUnitWeekdayOrdinal](cfcalendarunit/weekdayordinal.md) — Specifies the ordinal weekday unit.
- [kCFCalendarUnitQuarter](cfcalendarunit/quarter.md) — Specifies the quarter-year unit.
- [kCFCalendarUnitWeekOfMonth](cfcalendarunit/weekofmonth.md) — Specifies the original week of a month calendar unit.
- [kCFCalendarUnitWeekOfYear](cfcalendarunit/weekofyear.md) — Specifies the original week of the year calendar unit.
- [kCFCalendarUnitYearForWeekOfYear](cfcalendarunit/yearforweekofyear.md) — Specifies the relative year for a week within a year calendar unit.

### Initializers

- [init(rawValue:)](<cfcalendarunit/init(rawvalue_).md>)

### Type Properties

- [kCFCalendarUnitDayOfYear](cfcalendarunit/dayofyear.md)

## See Also

### Constants

- [Component Wrapping Options](1533520-component-wrapping-options.md) — The wrapping option specifies overflow behavior for calendar components in calendrical calculations
