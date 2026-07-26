---
title: formatted()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatted()
source_url: 'https://developer.apple.com/documentation/foundation/date/formatted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatted%28%29.json'
content_hash: 'sha256:f37a716dba2ec3ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# formatted()

<sub>Instance Method</sub>

Generates a locale-aware string representation of a date using the default date format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted() -> String
```

## Return Value

A string, formatted according to the default style.

## Discussion

Use the [formatted()](<formatted().md>) method to apply the default format style to a date, as in the following example:

```swift
let birthday = Date()
print(birthday.formatted())
// 6/4/2021, 2:24 PM
```

The default date format style uses the `numeric` date style and the `shortened` time style.

To customize the formatted measurement string, use either the [formatted(_:)](<formatted(__).md>) method and include a `Measurement.FormatStyle` or the [formatted(date:time:)](<formatted(date_time_).md>) and include a date and time style.

For more information about formatting dates, see [FormatStyle](formatstyle.md).

## See Also

### Formatting a Date

- [formatted(date:time:)](<formatted(date_time_).md>) — Generates a locale-aware string representation of a date using specified date and time format styles.
- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of a date using the specified date format style.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [ISO8601Format(_:)](<iso8601format(__).md>) — Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
