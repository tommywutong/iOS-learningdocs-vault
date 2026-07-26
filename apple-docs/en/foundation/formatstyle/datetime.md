---
title: dateTime
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/datetime
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/datetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/datetime.json'
content_hash: 'sha256:468bc7f12f4ce012'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# dateTime

<sub>Type Property</sub>

A style for formatting a date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var dateTime: Date.FormatStyle { get }
```

## Discussion

Use this type property when the call point allows the use of [FormatStyle](../date/formatstyle.md). You typically do this when calling the [formatted(_:)](<../date/formatted(__).md>) method of [Date](../date.md).

Customize the date format style using modifier syntax to apply specific date and time formats. For example:

```swift
let meetingDate = Date()
let localeArray = ["en_US", "sv_SE", "en_GB", "th_TH", "fr_BE"]
let formattedDates = localeArray.map { localeID in
    meetingDate.formatted(.dateTime
                          .day(.twoDigits)
                          .month(.wide)
                          .weekday(.short)
                          .hour(.conversationalTwoDigits(amPM: .wide))
                          .locale(Locale(identifier: localeID)))
        } // ["Mo, July 31 at 05 PM", "må 31 juli 17", "Mo, 31 July at 17", "จ. 31 กรกฎาคม เวลา 17", "lu 31 juillet à 17 h"]
```

The default format styles provided are [numeric](../date/formatstyle/datestyle/numeric.md) date format and [shortened](../date/formatstyle/timestyle/shortened.md) time format. For example:

```swift
let meetingDate = Date()
let formatted = meetingDate.formatted(.dateTime) // "7/31/2023, 5:15 PM"
```

## See Also

### Applying date and time styles

- [FormatStyle](../date/formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](../date/iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](../date/verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](../date/intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](../date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
