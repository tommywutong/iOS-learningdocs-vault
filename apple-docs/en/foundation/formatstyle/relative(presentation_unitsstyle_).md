---
title: 'relative(presentation:unitsStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/relative(presentation:unitsstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/relative(presentation:unitsstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/relative%28presentation%3Aunitsstyle%3A%29.json'
content_hash: 'sha256:29c9facfc10b0fd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# relative(presentation:unitsStyle:)

<sub>Type Method</sub>

Returns a style for formatting a date as relative to the current date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func relative(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle = .wide) -> Self
```

## Parameters

- `presentation` — The style to use when describing a relative date; for example, “1 day ago” or “yesterday”.

- `unitsStyle` — The style to use when formatting the quantity or the name of the unit; for example, “1 day ago” or “one day ago”.

## Return Value

A relative date format style customized with the specified presentation and unit styles.

## Discussion

Use this static method when the call point allows the use of [RelativeFormatStyle](../date/relativeformatstyle.md). You typically do this when calling the [formatted(_:)](<../date/formatted(__).md>) method of [Date](../date.md).

The following example shows the [relative(presentation:unitsStyle:)](<relative(presentation_unitsstyle_).md>) relative format style with two different presentations.

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    let formattedNumeric = past.formatted(
        .relative(presentation: .numeric)) // "1 week ago"
    let formattedNamed = past.formatted(
        .relative(presentation: .named)) // "last week"
}
```

## See Also

### Applying date and time styles

- [dateTime](datetime.md) — A style for formatting a date and time.
- [FormatStyle](../date/formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](../date/iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](../date/verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](../date/intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [RelativeFormatStyle](../date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
