---
title: Date.FormatStyle.Symbol.Era
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/era
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/era'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/era.json'
content_hash: 'sha256:590e328f1dd1de1c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.Era

<sub>Structure</sub>

A type that specifies a format for the era in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Era
```

## Overview

The type [Era](era.md) includes static factory variables that create custom [Era](era.md) objects.

| Factory variable | Description |
|---|---|
| [abbreviated](era/abbreviated.md) | An abbreviated representation of an era. For example, `AD`, `BC`. |
| [narrow](era/narrow.md) | A narrow era representation. For example, `A`, `B`. |
| [wide](era/wide.md) | A full representation of an era. For example, `Anno Domini`, `Before Christ`. |

To customize the era format in a string representation of a `Date`, use [era(_:)](<../era(__).md>). The following example shows a variety of [Era](era.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().era(.abbreviated)) // AD
meetingDate.formatted(Date.FormatStyle().era(.narrow)) // A
meetingDate.formatted(Date.FormatStyle().era(.wide)) // Anno Domini
meetingDate.formatted(Date.FormatStyle().era()) // AD
```

If no format is specified as a parameter, the [abbreviated](era/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying an Era

- [abbreviated](era/abbreviated.md) — An abbreviated representation of an era.
- [narrow](era/narrow.md) — A narrow representation of an era.
- [wide](era/wide.md) — A full representation of an era.

### Comparing an Era

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](era/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
- [DayPeriod](dayperiod.md) — A type that specifies a format for the time period in a date format style.
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
