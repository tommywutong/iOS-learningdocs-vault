---
title: Date.FormatStyle.Symbol.Year
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/year
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/year.json'
content_hash: 'sha256:f1dd62887d582f72'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Year

<sub>Structure</sub>

A type that specifies a format for the year in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Year
```

## Overview

The [Year](year.md) type includes static factory variables and methods that create custom [Year](year.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigits](year/defaultdigits.md) | The minimum number of digits that represents the full year. For example, `2`, `20`, `201`, `2017`. |
| [twoDigits](year/twodigits.md) | The year’s two lowest-order digits, zero-padded or truncated if necessary. For example, `02`, `20`, `01`, `17`, `73`. |
| [padded(_:)](<year/padded(__).md>) | Three or more digits, zero-padded if necessary. For example, `002`, `020`, `201`, `2017`. |
| [relatedGregorian(minimumLength:)](<year/relatedgregorian(minimumlength_).md>) | For non-Gregorian calendars, output corresponds to the extended Gregorian year in which the calendar’s year begins. The default length is the minimum needed to show the full year. |
| [extended(minimumLength:)](<year/extended(minimumlength_).md>) | A single number designating the year of the calendar system, encompassing all supra-year fields. The default length is the minimum needed to show the full year. |

To customize the year format in a string representation of a `Date`, use [year(_:)](<../year(__).md>). The following example shows a variety of [Year](year.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().year(.defaultDigits)) // 2021
meetingDate.formatted(Date.FormatStyle().year(.twoDigits)) // 21
meetingDate.formatted(Date.FormatStyle().year(.extended(minimumLength: 5))) // 02021
meetingDate.formatted(Date.FormatStyle().year(.extended())) // 2021
meetingDate.formatted(Date.FormatStyle().year(.padded(6))) // 002021
meetingDate.formatted(Date.FormatStyle().year(.relatedGregorian())) // 2021
```

If no format is specified as a parameter, the [defaultDigits](day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Year

- [defaultDigits](year/defaultdigits.md) — The custom year format style showing the minimum number of digits that represents the numeric year.
- [twoDigits](year/twodigits.md) — The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [padded(_:)](<year/padded(__).md>) — Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.
- [relatedGregorian(minimumLength:)](<year/relatedgregorian(minimumlength_).md>) — Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [extended(minimumLength:)](<year/extended(minimumlength_).md>) — Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.

### Comparing Years

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](year/omitted.md) — The option for not including the symbol in the formatted output.

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
