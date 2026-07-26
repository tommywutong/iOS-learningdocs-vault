---
title: Date.FormatStyle.Symbol.TimeZone
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/timezone
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/timezone.json'
content_hash: 'sha256:12734713d2127531'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Symbol](../symbol.md)

# Date.FormatStyle.Symbol.TimeZone

<sub>Structure</sub>

A type that specifies a format for the time zone in a date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TimeZone
```

## Overview

The type [TimeZone](timezone.md) includes static factory variables and methods that create custom [TimeZone](timezone.md) objects:

| Factory variable | Description |
|---|---|
| [specificName(_:)](<timezone/specificname(__).md>) | The specific, non-location representation of a timezone. For example, `CDT` (`short`), `Central Daylight Time` (`long`). |
| [genericName(_:)](<timezone/genericname(__).md>) | The generic, non-location representation of a timezone. For example, `CT` (`short`), `Central Time` (`long`). |
| [iso8601(_:)](<timezone/iso8601(__).md>) | The ISO 8601 representation of the timezone with hours, minutes, and optional seconds. For example, `-0500` (`short`), `-05:00` (`long`). |
| [localizedGMT(_:)](<timezone/localizedgmt(__).md>) | The localized GMT format representation of a timezone. For example, `GMT-5` (`short`), `GMT-05:00` (`long`). |
| [identifier(_:)](<timezone/identifier(__).md>) | The timezone identifier. For example, `uschi` (`short`), `America/Chicago` (`long`). |
| [exemplarLocation](timezone/exemplarlocation.md) | The exemplar city for a timezone. For example, `Chicago`. |
| [genericLocation](timezone/genericlocation.md) | The generic location representation of a timezone. For example, `Chicago Time`. |

To customize the hour format in a string representation of a `Date`, use [timeZone(_:)](<../timezone(__).md>). The following example shows a variety of [TimeZone](timezone.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 7:00 PM

meetingDate.formatted(Date.FormatStyle().timeZone(.specificName(.short)))
// CDT
meetingDate.formatted(Date.FormatStyle().timeZone(.specificName(.long)))
// Central Daylight Time

meetingDate.formatted(Date.FormatStyle().timeZone(.genericName(.short)))
// CT
meetingDate.formatted(Date.FormatStyle().timeZone(.genericName(.long)))
// Central Time

meetingDate.formatted(Date.FormatStyle().timeZone(.iso8601(.short)))
// -0500
meetingDate.formatted(Date.FormatStyle().timeZone(.iso8601(.long)))
// -05:00

meetingDate.formatted(Date.FormatStyle().timeZone(.localizedGMT(.short)))
// GMT-5
meetingDate.formatted(Date.FormatStyle().timeZone(.localizedGMT(.long)))
// GMT-05:00

meetingDate.formatted(Date.FormatStyle().timeZone(.identifier(.short)))
// uschi
meetingDate.formatted(Date.FormatStyle().timeZone(.identifier(.long)))
// America/Chicago

meetingDate.formatted(Date.FormatStyle().timeZone(.exemplarLocation))
// Chicago

meetingDate.formatted(Date.FormatStyle().timeZone(.genericLocation))
// Chicago Time

```

If you don’t provide a format, the system formats a timezone using the short [specificName(_:)](<timezone/specificname(__).md>) static function with the width [Date.FormatStyle.Symbol.TimeZone.Width.short](timezone/width/short.md).

For more information about formatting dates, see the [FormatStyle](../../formatstyle.md).

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Modifying a Time Zone

- [specificName(_:)](<timezone/specificname(__).md>) — Returns the specific, non-location representation of a timezone.
- [genericName(_:)](<timezone/genericname(__).md>) — Returns the generic, non-location representation of a timezone.
- [iso8601(_:)](<timezone/iso8601(__).md>) — Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [localizedGMT(_:)](<timezone/localizedgmt(__).md>) — Returns the localized GMT format representation of a timezone.
- [identifier(_:)](<timezone/identifier(__).md>) — Returns the timezone identifier.
- [exemplarLocation](timezone/exemplarlocation.md) — The exemplar city for a timezone.
- [genericLocation](timezone/genericlocation.md) — The generic location representation of a timezone.

### Comparing Time Zones

- [==(_:_:)](<../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Supporting Enumerations

- [Width](timezone/width.md) — A type representing the width of a timezone in a format style.

### Type Properties

- [omitted](timezone/omitted.md) — The option for not including the symbol in the formatted output.

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
- [VerbatimHour](verbatimhour.md) — A type that specifies a format for the hour in a date format style.
