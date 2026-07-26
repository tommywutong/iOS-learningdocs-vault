---
title: Date.FormatStyle.Symbol.Minute
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/minute
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/minute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/minute.json'
content_hash: 'sha256:9a6039bf3e74cf2c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Minute

<sub>Structure</sub>

A type that specifies the format for the minutes in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Minute
```

## Overview

The type [Minute](minute.md) includes static factory variables that create custom [Minute](minute.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigits](minute/defaultdigits.md) | The minimum number of digits that represents the  numeric minute. For example, `1`, `18`. |
| [twoDigits](minute/twodigits.md) | Two-digit numeric minute, zero-padded if necessary. For example, `01`, `18`. |

To customize the minute format in a string representation of a `Date`, use [minute(_:)](<../minute(__).md>). The following example shows a variety of [Minute](minute.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05 PM
meetingDate.formatted(Date.FormatStyle().minute(.defaultDigits)) // 5
meetingDate.formatted(Date.FormatStyle().minute(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().minute()) // 5
```

If no format is specified as a parameter, the [defaultDigits](minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Minute

- [defaultDigits](minute/defaultdigits.md) — The custom minute format style showing the minimum number of digits that represents the numeric minute.
- [twoDigits](minute/twodigits.md) — The custom format style that shows the two-digit numeric minute, zero-padded if necessary.

### Comparing a Minute

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](minute/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
- [DayPeriod](dayperiod.md) — A type that specifies a format for the time period in a date format style.
- [Era](era.md) — A type that specifies a format for the era in a date format style.
- [Hour](hour.md) — A type that specifies a format for the hour in a date format style.
- [Month](month.md) — A type that specifies a format for the month in a date format style.
- [Quarter](quarter.md) — A type that specifies the format for the quarter in a date format style.
- [Second](second.md) — A type that specifies the format for the seconds in a date format style.
- [SecondFraction](secondfraction.md) — A type that specifies the format for the second fraction in a date format style.
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
