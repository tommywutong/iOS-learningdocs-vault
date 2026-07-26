---
title: Date.FormatStyle.Symbol.Weekday
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/weekday
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/weekday'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/weekday.json'
content_hash: 'sha256:7fa6dd3acffeb695'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Weekday

<sub>Structure</sub>

A type that specifies the format for the weekday name in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Weekday
```

## Overview

The type [Weekday](weekday.md) includes static factory variables that create custom [Weekday](weekday.md) objects:

| Factory variable | Description |
|---|---|
| [abbreviated](month/abbreviated.md) | Abbreviated weekday name. For example, `Tue`. |
| [wide](month/wide.md) | Wide weekday name. For example, `Tuesday`. |
| [narrow](month/narrow.md) | Narrow weekday name. For example, `T`. |
| [short](weekday/short.md) | Short weekday name. For example, `Tu`. |
| [oneDigit](weekday/onedigit.md) | Local numeric one-digit day of week. The value depends on the local starting day of the week. For example, this is `2` if Sunday is the first day of the week. |
| [twoDigits](weekday/twodigits.md) | Local numeric two-digit day of week, zero-padded if necessary. The value depends on the local starting day of the week. For example, this is `02` if Sunday is the first day of the week. |

To customize the weekday, name format in a string representation of a `Date`, use [weekday(_:)](<../weekday(__).md>). This example shows a variety of [Weekday](weekday.md) format styles applied to a Thursday, using locale `en_US`:

```swift
let meetingDate = Date() // Feb 18, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().weekday(.abbreviated)) // Thu
meetingDate.formatted(Date.FormatStyle().weekday(.narrow)) // T
meetingDate.formatted(Date.FormatStyle().weekday(.short)) // Th
meetingDate.formatted(Date.FormatStyle().weekday(.wide)) // Thursday
meetingDate.formatted(Date.FormatStyle().weekday(.oneDigit)) // 5
meetingDate.formatted(Date.FormatStyle().weekday(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().weekday()) // Thu
```

If no format is specified as a parameter, the [abbreviated](month/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Weekday

- [abbreviated](weekday/abbreviated.md) — A shortened weekday representation.
- [narrow](weekday/narrow.md) — The shortest weekday representation.
- [oneDigit](weekday/onedigit.md) — The one-digit representation of a weekday.
- [short](weekday/short.md) — The short weekday representation.
- [twoDigits](weekday/twodigits.md) — The two-digit representation of a standalone weekday, zero-padded if necessary.
- [wide](weekday/wide.md) — The complete weekday representation.

### Comparing a Weekday

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](weekday/omitted.md) — The option for not including the symbol in the formatted output.

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
