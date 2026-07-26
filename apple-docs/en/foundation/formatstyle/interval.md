---
title: interval
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/interval
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/interval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/interval.json'
content_hash: 'sha256:b6f3c40852f31f1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# interval

<sub>Type Property</sub>

A style for formatting a date interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var interval: Date.IntervalFormatStyle { get }
```

## Discussion

Use this type property when the call point allows the use of [IntervalFormatStyle](../date/intervalformatstyle.md). You typically do this when calling the [formatted(_:)](<../../swift/range/formatted(__).md>) method of a `Range<Date>`.

The folllowing example uses [interval](interval.md) to create a date interval string with specific styling of the day, month, and weekday components, omitting the year and time.

```swift
if let today = Calendar.current.date(byAdding: .day, value: -120, to: Date()),
    let thirtyDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -30, to: today) {
    // today: June 5, 2023
    // thirtyDaysBeforeToday: May 6, 2023

    // Create a Range<Date>.
    let last30days = thirtyDaysBeforeToday..<today

    let formatted = last30days.formatted(
        .interval
        .day()
        .month(.wide)
        .weekday(.abbreviated)
    ) // "Sat, May 6 – Mon, June 5"
}
```

## See Also

### Applying date and time styles

- [dateTime](datetime.md) — A style for formatting a date and time.
- [FormatStyle](../date/formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](../date/iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](../date/verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [IntervalFormatStyle](../date/intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](../date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
