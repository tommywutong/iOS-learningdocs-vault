---
title: Date.FormatStyle.Symbol.Hour
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/hour
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour.json'
content_hash: 'sha256:a56eda5907a86578'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Hour

<sub>Structure</sub>

A type that specifies a format for the hour in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Hour
```

## Overview

The type [Hour](hour.md) includes static factory variables and methods that create custom [Hour](hour.md) objects:

| Factory variable | Description |
|---|---|
| [defaultDigitsNoAMPM](hour/defaultdigitsnoampm.md) | The minimum number of digits that represents the full numeric hour. This doesn’t include the day period (a.m. or p.m.). For example, `1`, `11`. |
| [twoDigitsNoAMPM](hour/twodigitsnoampm.md) | Two-digit numeric hour, zero-padded if necessary. This doesn’t include the day period (a.m. or p.m.). For example, `01`, `11`. |
| [defaultDigits(amPM:)](<hour/defaultdigits(ampm_).md>) | The minimum number of digits that represents the full numeric hour. This may include the day period (a.m. or p.m.), depending on locale. For example, `7a` (`narrow`), `7AM` (`abbreviated`), `7A.M.` (`wide`). |
| [twoDigits(amPM:)](<hour/twodigits(ampm_).md>) | Two-digit numeric hour, zero-padded if necessary. This may include the day period (a.m. or p.m.), depending on locale. For example, `07a` (`narrow`), `07AM` (`abbreviated`), `07A.M.` (`wide`). |
| [conversationalDefaultDigits(amPM:)](<hour/conversationaldefaultdigits(ampm_).md>) | The minimum number of digits that represents the full numeric hour. This may include the day period (a.m. or p.m.), depending on locale, and can include conversational period formats. For example, `7a` (`narrow`), `7AM` (`abbreviated`), `7A.M.` (`wide`). |
| [conversationalTwoDigits(amPM:)](<hour/conversationaltwodigits(ampm_).md>) | Two-digit numeric hour, zero-padded if necessary. This may include the day period (a.m. or p.m.), depending on locale, and can include conversational period formats. For example, `07a` (`narrow`), `07AM` (`abbreviated`), `07A.M.` (`wide`). |

To customize the hour format in a string representation of a `Date`, use [hour(_:)](<../hour(__).md>) The example below shows a variety of [Hour](hour.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 7:00 PM
meetingDate.formatted(Date.FormatStyle().hour(.defaultDigitsNoAMPM)) 
// 7

meetingDate.formatted(Date.FormatStyle().hour(.twoDigitsNoAMPM)) 
// 07

meetingDate.formatted(Date.FormatStyle().hour(.defaultDigits(amPM: .narrow))) 
// 7p

meetingDate.formatted(Date.FormatStyle().hour(.twoDigits(amPM: .abbreviated))
// 07 PM

meetingDate.formatted(Date.FormatStyle().hour(.conversationalDefaultDigits(amPM: .wide))
// 7 P.M.
```

If no format is specified as a parameter, the [defaultDigits](minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying an Hour

- [defaultDigitsNoAMPM](hour/defaultdigitsnoampm.md) — Custom format style portraying the minimum number of digits that represents the numeric hour. _(deprecated)_
- [twoDigitsNoAMPM](hour/twodigitsnoampm.md) — Custom format style portraying the numeric hour using two digits. _(deprecated)_
- [conversationalDefaultDigits(amPM:)](<hour/conversationaldefaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [conversationalTwoDigits(amPM:)](<hour/conversationaltwodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [defaultDigits(amPM:)](<hour/defaultdigits(ampm_).md>) — Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [twoDigits(amPM:)](<hour/twodigits(ampm_).md>) — Custom format style portraying two digits that represent the hour and locale-dependent day period formats.

### Supporting Structures

- [AMPMStyle](hour/ampmstyle.md) — The format style of the string representation of the day period, before or after noon, in a date.

### Comparing an Hour

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](hour/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
- [DayPeriod](dayperiod.md) — A type that specifies a format for the time period in a date format style.
- [Era](era.md) — A type that specifies a format for the era in a date format style.
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
