---
title: 'verbatim(_:locale:timeZone:calendar:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/verbatim(_:locale:timezone:calendar:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/verbatim(_:locale:timezone:calendar:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/verbatim%28_%3Alocale%3Atimezone%3Acalendar%3A%29.json'
content_hash: 'sha256:031ba45b0a7774e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# verbatim(_:locale:timeZone:calendar:)

<sub>Type Method</sub>

Returns a style for formatting a date with an explicitly-specified style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func verbatim(_ format: Date.FormatString, locale: Locale? = nil, timeZone: TimeZone, calendar: Calendar) -> Date.VerbatimFormatStyle
```

## Parameters

- `format` — A [FormatString](../date/formatstring.md) that provides the explicit components and their respective styles to use when formatting a date.

- `locale` — The locale to use when formatting. Defaults to `nil`.

- `timeZone` — The time zone to use when formatting.

- `calendar` — The calendar to use when formatting.

## Return Value

A date format style that uses the provided format string and timekeeping parameters.

## Discussion

Use this format style only when you need to produce or parse an exact format, such as when working with programmatically-produced date strings. For formatting dates that people read, use [dateTime](datetime.md) to get a localized [FormatStyle](../date/formatstyle.md) instead. To use the ISO-8601 standard, use `FormatStyle/iso8601` to get a [ISO8601FormatStyle](../date/iso8601formatstyle.md).

Use the dot-notation form of this type method when the call point allows the use of [VerbatimFormatStyle](../date/verbatimformatstyle.md). You typically do this when calling the [formatted(_:)](<../date/formatted(__).md>) method of [Date](../date.md).

The following example formats the current date with a verbatim format that uses a two-digit month, two-digit day, and default-digits year, separated by slashes. The format style zero-pads the month and day components. This style isn’t localized — while this format string mimicks `en_US` conventions, it uses this format in any locale, ignoring locale-apporpriate conventions.

```swift
let date = Date()
let formatted = date.formatted(
    .verbatim("\(month: .twoDigits)/\(day: .twoDigits)/\(year: .defaultDigits)" as Date.FormatString,
              locale: .autoupdatingCurrent,
              timeZone: .current,
              calendar: .current)) // 12/05/2022
```

## See Also

### Applying date and time styles

- [dateTime](datetime.md) — A style for formatting a date and time.
- [FormatStyle](../date/formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](../date/iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [VerbatimFormatStyle](../date/verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](../date/intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](../date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](../date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
