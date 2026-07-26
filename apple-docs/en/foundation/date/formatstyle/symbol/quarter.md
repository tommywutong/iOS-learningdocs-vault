---
title: Date.FormatStyle.Symbol.Quarter
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/quarter
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/quarter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/quarter.json'
content_hash: 'sha256:fd1cd5aeb22e1bf2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Quarter

<sub>Structure</sub>

A type that specifies the format for the quarter in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Quarter
```

## Overview

The type [Quarter](quarter.md) includes static factory variables that create custom [Quarter](quarter.md) objects:

| Factory variable | Description |
|---|---|
| [abbreviated](quarter/abbreviated.md) | Abbreviated quarter name. For example, `Q2`. |
| [narrow](quarter/narrow.md) | Minimum number of digits that represents the  numeric quarter. For example, `2`. |
| [oneDigit](quarter/onedigit.md) | One-digit numeric quarter. For example, `1`, `4`. |
| [twoDigits](quarter/twodigits.md) | Two-digit numeric quarter, zero-padded if necessary. For example, `01`, `04`. |
| [wide](quarter/wide.md) | Wide quarter name. For example, `2nd quarter`. |

To customize the month format in a string representation of a `Date`, use [quarter(_:)](<../quarter(__).md>). The following example shows a variety of [Quarter](quarter.md) format styles applied to a date.

```swift
let meetingDate = Date() // Oct 7, 2020 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().quarter(.abbreviated)) // Q4
meetingDate.formatted(Date.FormatStyle().quarter(.narrow)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter(.oneDigit)) // 4
meetingDate.formatted(Date.FormatStyle().quarter(.twoDigits)) // 04
meetingDate.formatted(Date.FormatStyle().quarter(.wide)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter()) // Q4

```

If no format is specified as a parameter, the [abbreviated](quarter/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Quarter

- [abbreviated](quarter/abbreviated.md) — The abbreviated representation of a quarter.
- [narrow](quarter/narrow.md) — The shortest representation of a quarter.
- [oneDigit](quarter/onedigit.md) — The one-digit representation of a quarter.
- [twoDigits](quarter/twodigits.md) — The two-digit representation of a quarter.
- [wide](quarter/wide.md) — The full representation of a quarter.

### Comparing Quarters

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](quarter/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
- [DayPeriod](dayperiod.md) — A type that specifies a format for the time period in a date format style.
- [Era](era.md) — A type that specifies a format for the era in a date format style.
- [Hour](hour.md) — A type that specifies a format for the hour in a date format style.
- [Minute](minute.md) — A type that specifies the format for the minutes in a date format style.
- [Month](month.md) — A type that specifies a format for the month in a date format style.
- [Second](second.md) — A type that specifies the format for the seconds in a date format style.
- [SecondFraction](secondfraction.md) — A type that specifies the format for the second fraction in a date format style.
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
