---
title: Date.FormatStyle.Symbol.Month
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/month
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/month'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/month.json'
content_hash: 'sha256:53688f71dc6c443f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Month

<sub>Structure</sub>

A type that specifies a format for the month in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Month
```

## Overview

The type [Month](month.md) includes static factory variables that create custom [Month](month.md) objects:

| Factory variable | Description |
|---|---|
| [abbreviated](month/abbreviated.md) | Abbreviated month name. For example, `Sep`. |
| [defaultDigits](month/defaultdigits.md) | Minimum number of digits that represents the numeric month. For example, `9`, `12`. |
| [narrow](month/narrow.md) | Narrow month name. For example, `S`. |
| [twoDigits](month/twodigits.md) | Two-digit numeric month, zero-padded if necessary. For example, `09`, `12`. |
| [wide](month/wide.md) | Wide month name. For example, `September`. |

To customize the month format in a string representation of a `Date`, use [month(_:)](<../month(__).md>). The following example shows a variety of [Month](month.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().month(.abbreviated)) // Feb
meetingDate.formatted(Date.FormatStyle().month(.narrow)) // F
meetingDate.formatted(Date.FormatStyle().month(.defaultDigits)) // 2
meetingDate.formatted(Date.FormatStyle().month(.twoDigits)) // 02
meetingDate.formatted(Date.FormatStyle().month(.wide)) // February
meetingDate.formatted(Date.FormatStyle().month()) // Feb
```

If no format is specified as a parameter, the [abbreviated](month/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Month

- [abbreviated](month/abbreviated.md) — The abbreviated representation of a month.
- [defaultDigits](month/defaultdigits.md) — Custom month format style showing the minimum number of digits that represents the numeric month.
- [narrow](month/narrow.md) — The shortest representation of a month.
- [twoDigits](month/twodigits.md) — The custom month format style that uses two digits to represent the numeric month.
- [wide](month/wide.md) — The full representation of a month.

### Comparing a Month

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](month/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
- [DayPeriod](dayperiod.md) — A type that specifies a format for the time period in a date format style.
- [Era](era.md) — A type that specifies a format for the era in a date format style.
- [Hour](hour.md) — A type that specifies a format for the hour in a date format style.
- [Minute](minute.md) — A type that specifies the format for the minutes in a date format style.
- [Quarter](quarter.md) — A type that specifies the format for the quarter in a date format style.
- [Second](second.md) — A type that specifies the format for the seconds in a date format style.
- [SecondFraction](secondfraction.md) — A type that specifies the format for the second fraction in a date format style.
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
