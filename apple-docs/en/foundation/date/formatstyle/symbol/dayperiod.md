---
title: Date.FormatStyle.Symbol.DayPeriod
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/dayperiod
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/dayperiod.json'
content_hash: 'sha256:b9f94b1b28d6e674'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.DayPeriod

<sub>Structure</sub>

A type that specifies a format for the time period in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DayPeriod
```

## Overview

The type [DayPeriod](dayperiod.md) includes static factory methods that create custom [DayPeriod](dayperiod.md) objects.

| Factory variable | Description |
|---|---|
| [conversational(_:)](<dayperiod/conversational(__).md>) | Conversational abbreviated period. For example, `at night`, `nachm.`, `iltap`. ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Conversational narrow period. For example, `at night`, `nachmittags`, `iltapäivällä`. ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Conversational wide period. For example, `at night`, `nachm.`, `ip.` |
| [standard(_:)](<dayperiod/standard(__).md>) | Abbreviated period. For example, `am`. ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Narrow period. For example, `a`. ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Wide period. For example, `am`. |
| [with12s(_:)](<dayperiod/with12s(__).md>) | Abbreviated period including designations for noon and midnight. For example, `mid.` ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Narrow period including designations for noon and midnight. For example, `md`. ![](../../../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Wide period including designations for noon and midnight. For example, `midnight`. |

The day period format style may be uppercase or lowercase depending on the locale and other options.

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Day Period

- [conversational(_:)](<dayperiod/conversational(__).md>) — Static factory method that creates a custom day period format style using a conversational style.
- [standard(_:)](<dayperiod/standard(__).md>) — Static factory method that creates a custom day period format style using a standard style.
- [with12s(_:)](<dayperiod/with12s(__).md>) — Static factory method that creates a custom day period format style using a style that represents midday and midnight.

### Supporting Enumerations

- [Width](dayperiod/width.md) — A type representing the width of a day period in a format style.

### Comparing Day Periods

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Type Properties

- [omitted](dayperiod/omitted.md) — The option for not including the symbol in the formatted output.

## See Also

### Modifying Date Style Format Symbols

- [CyclicYear](cyclicyear.md) — A type that specifies a format for a cyclic year in a date format style.
- [Day](day.md) — A type that specifies the format for a day in a date format style.
- [DayOfYear](dayofyear.md) — A type that specifies the format for the day of the year in a date format style.
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
