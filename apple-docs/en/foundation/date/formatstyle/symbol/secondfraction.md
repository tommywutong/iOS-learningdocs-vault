---
title: Date.FormatStyle.Symbol.SecondFraction
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/secondfraction
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/secondfraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/secondfraction.json'
content_hash: 'sha256:140922e3e95a1902'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.SecondFraction

<sub>Structure</sub>

A type that specifies the format for the second fraction in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SecondFraction
```

## Overview

The type [SecondFraction](secondfraction.md) includes static factory methods that create custom [SecondFraction](secondfraction.md) objects:

| Factory variable | Description |
|---|---|
| [fractional(_:)](<secondfraction/fractional(__).md>) | Returns the numerical representation of the fractional component of the second. For example, `8`, `827`. |
| [milliseconds(_:)](<secondfraction/milliseconds(__).md>) | Returns the number of milliseconds elapsed in the day. For example, `11122827`. |

To customize the second format in a string representation of a `Date`, use [secondFraction(_:)](<../secondfraction(__).md>). The following example shows a variety of [SecondFraction](secondfraction.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05:41 PM
meetingDate.formatted(Date.FormatStyle().secondFraction(.fractional(3))) // 827
meetingDate.formatted(Date.FormatStyle().secondFraction(.fractional(1))) // 8
meetingDate.formatted(Date.FormatStyle().secondFraction(.milliseconds(4))) // 11122827
```

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Second Fraction

- [fractional(_:)](<secondfraction/fractional(__).md>) — Creates a custom format style representing the fractional seconds component of a date.
- [milliseconds(_:)](<secondfraction/milliseconds(__).md>) — Creates a custom format style representing the milliseconds elapsed in a day.

### Comparing Second Fractions

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](secondfraction/omitted.md) — The option for not including the symbol in the formatted output.

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
- [StandaloneMonth](standalonemonth.md) — A type that specifies the format for a standalone month.
- [StandaloneQuarter](standalonequarter.md) — A type that specifies the format for a standalone quarter.
- [StandaloneWeekday](standaloneweekday.md) — A type that specifies the format for a standalone weekday.
- [TimeZone](timezone.md) — A type that specifies a format for the time zone in a date format style.
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
