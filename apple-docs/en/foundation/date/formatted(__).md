---
title: 'formatted(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatted%28_%3A%29.json'
content_hash: 'sha256:7a1ad6bb4b2dab0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# formatted(_:)

<sub>Instance Method</sub>

Generates a locale-aware string representation of a date using the specified date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<F>(_ format: F) -> F.FormatOutput where F : FormatStyle, F.FormatInput == Date
```

## Parameters

- `format` — The date format style to apply to the date.

## Return Value

A string, formatted according to the specified style.

## Discussion

For full customization of the string representation of a date, use the [formatted(_:)](<formatted(__).md>) instance method of [Date](../date.md) and provide a [FormatStyle](formatstyle.md) object.

You can achieve any customization of date and time representation your app requires by appying a series of convenience modifiers to your format style. This example applies a series of modifiers to the format style to precisely define the formatting of the year, month, day, hour, minute, and timezone components of the resulting string.

```swift
// Call the .formatted method on an instance of Date passing in an instance of Date.FormatStyle.

let birthday = Date()

birthday.formatted(
    Date.FormatStyle()
        .year(.defaultDigits)
        .month(.abbreviated)
        .day(.twoDigits)
        .hour(.defaultDigits(amPM: .abbreviated))
        .minute(.twoDigits)
        .timeZone(.identifier(.long))
        .era(.wide)
        .dayOfYear(.defaultDigits)
        .weekday(.abbreviated)
        .week(.defaultDigits)
) 
// Sun, Jan 17, 2021 Anno Domini (week: 4), 11:18 AM America/Chicago
```

For the default date formatting, use the [formatted()](<formatted().md>) method. For basic customization of the formatted date string, use the [formatted(date:time:)](<formatted(date_time_).md>) and include a date and time style.

For more information about formatting dates, see [FormatStyle](formatstyle.md).

## See Also

### Formatting a Date

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of a date using the default date format style.
- [formatted(date:time:)](<formatted(date_time_).md>) — Generates a locale-aware string representation of a date using specified date and time format styles.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [ISO8601Format(_:)](<iso8601format(__).md>) — Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
