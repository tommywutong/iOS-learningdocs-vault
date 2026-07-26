---
title: Date.FormatStyle.Symbol.Day
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/day
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/day.json'
content_hash: 'sha256:e2336ee54d73efd7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Day

<sub>Structure</sub>

A type that specifies the format for a day in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Day
```

## Overview

The [Day](day.md) type includes static factory variables and methods that create custom [Day](day.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigits](day/defaultdigits.md) | The minimum number of digits that shows the numeric day of month. For example, `1`, `18`. |
| [julianModified(minimumLength:)](<day/julianmodified(minimumlength_).md>) | The modified Julian day. The field length specifies the minimum number of digits, zero-padded if necessary. For example, `2451334`. |
| [ordinalOfDayInMonth](day/ordinalofdayinmonth.md) | The ordinal of the day in the month. For example, the second Wednesday in July would yield `2`. |
| [twoDigits](day/twodigits.md) | The two-digit numeric day of month, zero-padded if necessary. For example, `01`, `18`. |

To customize the day format in a string representation of a `Date`, use [day(_:)](<../day(__).md>). The following example shows a variety of [Day](day.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().day(.defaultDigits)) // 9
meetingDate.formatted(Date.FormatStyle().day(.ordinalOfDayInMonth)) // 2 (second Tuesday of the month)
meetingDate.formatted(Date.FormatStyle().day(.twoDigits)) // 09
meetingDate.formatted(Date.FormatStyle().day(.julianModified(minimumLength: 12))) // 0002459255
meetingDate.formatted(Date.FormatStyle().day()) // 9
```

If no format is specified as a parameter, the [defaultDigits](day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Day Format

- [defaultDigits](day/defaultdigits.md) — Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [ordinalOfDayInMonth](day/ordinalofdayinmonth.md) — Custom format style portraying the ordinal of the day in the month.
- [twoDigits](day/twodigits.md) — Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.
- [julianModified(minimumLength:)](<day/julianmodified(minimumlength_).md>) — Creates a custom day format style representing the modified Julian day.

### Comparing Day Formats

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](day/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
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
