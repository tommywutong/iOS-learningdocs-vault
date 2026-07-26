---
title: Date.FormatStyle.Symbol.CyclicYear
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/cyclicyear
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/cyclicyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/cyclicyear.json'
content_hash: 'sha256:bceee1dc7e4ca23f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.CyclicYear

<sub>Structure</sub>

A type that specifies a format for a cyclic year in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CyclicYear
```

## Overview

Calendars such as the Chinese lunar calendar and Hindu calendars use 60-year cycles of year names. If the calendar doesn’t provide cyclic year-name data, or if the year value to format is out of the range of years for which the system provides cyclic name data, then the formatting is numeric, as in [Year](year.md).

The [CyclicYear](cyclicyear.md) type includes static factory variables that create custom [CyclicYear](cyclicyear.md) objects:

| Factory variable | Description |
|---|---|
| [abbreviated](cyclicyear/abbreviated.md) | A shortened representation of the cyclic year appropriate for space-constrained applications. |
| [narrow](cyclicyear/narrow.md) | The shortest representation of the cyclic year. |
| [wide](cyclicyear/wide.md) | The full representation of the cyclic year. |

If no format is specified as a parameter, the [abbreviated](cyclicyear/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Cyclic Year

- [abbreviated](cyclicyear/abbreviated.md) — Custom cyclic year format style that portrays a shortened cyclic year.
- [narrow](cyclicyear/narrow.md) — Custom cyclic year format style that portrays the shortest representation of a cyclic year.
- [wide](cyclicyear/wide.md) — Custom cyclic year format style that portrays a complete representation of a cyclic year.

### Comparing Cyclic Years

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](cyclicyear/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
- [DayPeriod](dayperiod.md) — A type that specifies a format for the time period in a date format style.
- [Era](era.md) — A type that specifies a format for the era in a date format style.
- [Hour](hour.md) — A type that specifies a format for the hour in a date format style.
- [Minute](minute.md) — A type that specifies the format for the minutes in a date format style.
- [Month](month.md) — A type that specifies a format for the month in a date format style.
- [Quarter](quarter.md) — A type that specifies the format for the quarter in a date format style.
- [Second](second.md) — A type that specifies the format for the seconds in a date format style.
- [SecondFraction](secondfraction.md) — A type that specifies the format for the second fraction in a date format style.
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
