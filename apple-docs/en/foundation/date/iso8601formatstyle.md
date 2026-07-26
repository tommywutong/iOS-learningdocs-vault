---
title: Date.ISO8601FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/iso8601formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle.json'
content_hash: 'sha256:7ad7036a8acb1247'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.ISO8601FormatStyle

<sub>Structure</sub>

A type that converts between dates and their ISO-8601 string representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ISO8601FormatStyle
```

## Overview

The [ISO8601FormatStyle](iso8601formatstyle.md) type generates and parses string representations of dates following the [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard, like `2024-04-01T12:34:56.789Z`. Use this type to create ISO-8601 representations of dates and create dates from text strings in ISO 8601 format. For other formatting conventions, like human-readable, localized date formats, use [FormatStyle](formatstyle.md).

Instance modifier methods applied to an ISO-8601 format style customize the formatted output, as the following example illustrates.

```swift
let now = Date()
print(now.formatted(Date.ISO8601FormatStyle().dateSeparator(.dash)))
// 2021-06-21T211015Z
```

Use the static factory property `FormatStyle/iso8601` to create an instance of [ISO8601FormatStyle](iso8601formatstyle.md). Then apply instance modifier methods to customize the format, as in the example below.

```swift
let meetNow = Date()
let formatted = meetNow.formatted(.iso8601
    .year()
    .month()
    .day()
    .timeZone(separator: .omitted)
    .time(includingFractionalSeconds: true)
    .timeSeparator(.colon)
) // "2022-06-10T12:34:56.789Z"

```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an ISO 8601 Format Style

- [init(dateSeparator:dateTimeSeparator:timeZone:)](<iso8601formatstyle/init(dateseparator_datetimeseparator_timezone_).md>) — Creates an instance using the provided date separator, date and time components separator, and time zone.

### Modifying an ISO 8601 Format Style

- [dateSeparator](iso8601formatstyle/dateseparator-swift.property.md) — The character used to separate the components of a date.
- [dateTimeSeparator](iso8601formatstyle/datetimeseparator-swift.property.md) — The character used to separate the date and time components of an ISO 8601 string representation of a date.
- [timeZone](iso8601formatstyle/timezone.md) — The time zone used to create and parse date representations.
- [dateTimeSeparator(_:)](<iso8601formatstyle/datetimeseparator(__).md>) — Sets the character that specifies the date and time components.

### Modifying Dates in an ISO 8601 Format Style

- [dateSeparator(_:)](<iso8601formatstyle/dateseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified date separator.
- [year()](<iso8601formatstyle/year().md>) — Modifies the ISO 8601 date format style to include the year in the formatted output.
- [month()](<iso8601formatstyle/month().md>) — Modifies the ISO 8601 date format style to include the month in the formatted output.
- [weekOfYear()](<iso8601formatstyle/weekofyear().md>) — Modifies the ISO 8601 date format style to include the week of the year in the formatted output.
- [day()](<iso8601formatstyle/day().md>) — Modifies the ISO 8601 date format style to include the day in the formatted output.

### Modifying Times in an ISO 8601 Format Style

- [time(includingFractionalSeconds:)](<iso8601formatstyle/time(includingfractionalseconds_).md>) — Modifies the ISO 8601 date format style to include the time in the formatted output.
- [timeSeparator(_:)](<iso8601formatstyle/timeseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified time separator.
- [timeZone(separator:)](<iso8601formatstyle/timezone(separator_).md>) — Modifies the ISO 8601 date format style to include the time zone in the formatted output.
- [timeZoneSeparator(_:)](<iso8601formatstyle/timezoneseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified time zone separator.

### Parsing an ISO 8601 Format Style

- [parse(_:)](<iso8601formatstyle/parse(__).md>) — Parses a string into a date.
- [parseStrategy](iso8601formatstyle/parsestrategy.md) — The strategy used to parse a string into a date.

### Applying an ISO 8601 Format Style

- [format(_:)](<iso8601formatstyle/format(__).md>) — Creates a locale-aware ISO 8601 string representation from a date value.

### Comparing ISO 8601 Format Styles

- [==(_:_:)](<==(____).md>) — Returns true if the two `Date` values represent the same point in time.

### Supporting Types

- [DateSeparator](iso8601formatstyle/dateseparator-swift.enum.md) — A type describing the character separating year, month, and day components of a date in an ISO 8601 date format.
- [DateTimeSeparator](iso8601formatstyle/datetimeseparator-swift.enum.md) — Type describing the character separating the date and time components of a date in an ISO 8601 date format.
- [TimeSeparator](iso8601formatstyle/timeseparator-swift.enum.md) — Type describing the character separating the time components of a date in an ISO 8601 date format.
- [TimeZoneSeparator](iso8601formatstyle/timezoneseparator-swift.enum.md) — A type describing the character separating the time and time zone of a date in an ISO 8601 date format.

### Initializers

- [init(dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:includingFractionalSeconds:timeZone:)](<iso8601formatstyle/init(dateseparator_datetimeseparator_timeseparator_timezoneseparator_includingfractionalseconds_timezone_).md>)

### Instance Properties

- [includingFractionalSeconds](iso8601formatstyle/includingfractionalseconds.md) — If set, the style includes fractional seconds when formatting. Before Swift 6.2, if true when parsing, fractional seconds must be present. If false when parsing, fractional seconds must not be present. After Swift 6.2, fractional seconds may be present in the String regardless of the setting of this property.
- [timeSeparator](iso8601formatstyle/timeseparator-swift.property.md)
- [timeZoneSeparator](iso8601formatstyle/timezoneseparator-swift.property.md)

### Default Implementations

- [CustomConsumingRegexComponent Implementations](iso8601formatstyle/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](iso8601formatstyle/formatstyle-implementations.md)
- [ParseStrategy Implementations](iso8601formatstyle/parsestrategy-implementations.md)
- [ParseableFormatStyle Implementations](iso8601formatstyle/parseableformatstyle-implementations.md)
- [RegexComponent Implementations](iso8601formatstyle/regexcomponent-implementations.md)

## See Also

### Applying date and time styles

- [dateTime](../formatstyle/datetime.md) — A style for formatting a date and time.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [verbatim(_:locale:timeZone:calendar:)](<../formatstyle/verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](../formatstyle/interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<../formatstyle/relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<../formatstyle/components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
