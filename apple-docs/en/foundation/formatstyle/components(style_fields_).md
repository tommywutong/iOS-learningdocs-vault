---
title: 'components(style:fields:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/components(style:fields:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/components(style:fields:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/components%28style%3Afields%3A%29.json'
content_hash: 'sha256:67313791471c7699'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# components(style:fields:)

<sub>Type Method</sub>

Returns a style for formatting a date interval in terms of specific date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>? = nil) -> Self
```

## Parameters

- `style` — The style to use for the fields, such as [abbreviated](../date/componentsformatstyle/style-swift.struct/abbreviated.md) or [narrow](../date/componentsformatstyle/style-swift.struct/narrow.md).

- `fields` — A set of date component fields to include in the formatted output.

## Return Value

A date format style that uses the specified style and fields.

## Discussion

Use this type method when the call point allows the use of [ComponentsFormatStyle](../date/componentsformatstyle.md). You typically do this when calling the [formatted(_:)](<../../swift/range/formatted(__).md>) method of a `Range<Date>`.

The following example creates a 120-day date range, and then uses a [ComponentsFormatStyle](../date/componentsformatstyle.md) to express this as a count of weeks and days:

```swift
let date = Date()
let futureDate = Calendar.current.date(byAdding: .day, value: 120, to: date)!
let interval = (date..<futureDate)
let formatted = interval.formatted(
    .components(style: .wide,
                fields: [.week, .day])) // 17 weeks, 1 day
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
- [relative(presentation:unitsStyle:)](<relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](../date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
