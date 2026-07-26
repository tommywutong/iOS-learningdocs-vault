---
title: Date.FormatStyle.Symbol.DayOfYear
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/dayofyear
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayofyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/dayofyear.json'
content_hash: 'sha256:21e43976280aa666'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.DayOfYear

<sub>Structure</sub>

A type that specifies the format for the day of the year in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DayOfYear
```

## Overview

The type [DayOfYear](dayofyear.md) includes static factory variables that create custom [DayOfYear](dayofyear.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigits](dayofyear/defaultdigits.md) | The minimum number of digits that represents the full day of the year. For example, `1`, `18`, `317`. |
| [threeDigits](dayofyear/threedigits.md) | Three-digit numeric day of the year, zero-padded if necessary. For example, `001`, `018`, `317`. |
| [twoDigits](dayofyear/twodigits.md) | Two-digit numeric day of the year, zero-padded if necessary. This format has no effect on three-digit values. For example, `01`, `18`, `317`. |

To customize the day format in a string representation of a `Date`, use [dayOfYear(_:)](<../dayofyear(__).md>). The following example shows a variety of [DayOfYear](dayofyear.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().dayOfYear(.defaultDigits)) // 40
meetingDate.formatted(Date.FormatStyle().dayOfYear(.twoDigits)) // 40
meetingDate.formatted(Date.FormatStyle().dayOfYear(.threeDigits)) // 040
meetingDate.formatted(Date.FormatStyle().dayOfYear()) // 40

```

If no format is specified as a parameter, the [defaultDigits](dayofyear/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Day of Year Value

- [defaultDigits](dayofyear/defaultdigits.md) — Custom format style portraying the minimum number of digits that represents the numeric day of the year.
- [threeDigits](dayofyear/threedigits.md) — Custom format style portraying the three-digit numeric day of the year, zero-padded if necessary.
- [twoDigits](dayofyear/twodigits.md) — Custom format style portraying the two-digit numeric day of the year, zero-padded if necessary.

### Comparing Day of Year Values

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](dayofyear/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
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
