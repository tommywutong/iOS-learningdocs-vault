---
title: Date.FormatStyle.Symbol.Second
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/second
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/second'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/second.json'
content_hash: 'sha256:4e48f91e72f9eafe'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Second

<sub>Structure</sub>

A type that specifies the format for the seconds in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Second
```

## Overview

The type [Second](second.md) includes static factory variables that create custom [Second](second.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigits](second/defaultdigits.md) | The minimum number of digits that represents the numeric second. For example, `1`, `18`. |
| [twoDigits](second/twodigits.md) | Two-digit numeric second, zero-padded if necessary. For example, `01`, `18`. |

To customize the second format in a string representation of a `Date`, use [second(_:)](<../second(__).md>). The following example shows a variety of [Second](second.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05 PM
meetingDate.formatted(Date.FormatStyle().second(.defaultDigits)) // 5
meetingDate.formatted(Date.FormatStyle().second(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().second()) // 5
```

If no format is specified as a parameter, the [defaultDigits](second/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Second

- [defaultDigits](second/defaultdigits.md) — The custom format style that conveys the minimum number of digits that represents the numeric second.
- [twoDigits](second/twodigits.md) — The custom format style that conveys a two-digit numeric second, zero-padded if necessary.

### Comparing Seconds

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](second/omitted.md) — The option for not including the symbol in the formatted output.

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
- [SecondFraction](secondfraction.md) — A type that specifies the format for the second fraction in a date format style.
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
