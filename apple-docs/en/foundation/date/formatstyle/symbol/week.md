---
title: Date.FormatStyle.Symbol.Week
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/week
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/week'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/week.json'
content_hash: 'sha256:5bb895b76d5ab289'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Week

<sub>Structure</sub>

A type that specifies the format for the week in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Week
```

## Overview

The type [Week](week.md) includes static factory variables that create custom [Week](week.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigits](week/defaultdigits.md) | The minimum number of digits that represents the full numeric week. For example, `1`, `18`. |
| [twoDigits](week/twodigits.md) | Two-digit numeric week, zero-padded if necessary. For example, `01`, `18`. |
| [weekOfMonth](week/weekofmonth.md) | The numeric week of the month. For example, `1`, `4`. |

To customize the week format in a string representation of a `Date`, use [week(_:)](<../week(__).md>). The following example shows a variety of [Week](week.md) format styles applied to a date.

```swift
let meetingDate = Date() // May 3, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().week(.defaultDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.twoDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.weekOfMonth)) // 2
meetingDate.formatted(Date.FormatStyle().week()) // 19

```

An incomplete week at the start of a month is week of the month `1`. If no format is specified as a parameter, the [defaultDigits](week/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Week

- [defaultDigits](week/defaultdigits.md) — Custom week format style showing the minimum number of digits that represents the numeric week.
- [twoDigits](week/twodigits.md) — Custom format style portraying the two-digit numeric week, zero-padded if necessary.
- [weekOfMonth](week/weekofmonth.md) — Custom format style portraying the numeric week of the month.

### Comparing Weeks

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](week/omitted.md) — The option for not including the symbol in the formatted output.

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
- [Quarter](quarter.md) — A type that specifies the format for the quarter in a date format style.
- [Second](second.md) — A type that specifies the format for the seconds in a date format style.
- [SecondFraction](secondfraction.md) — A type that specifies the format for the second fraction in a date format style.
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
