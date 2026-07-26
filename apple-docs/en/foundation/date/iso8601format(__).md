---
title: 'ISO8601Format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601format%28_%3A%29.json'
content_hash: 'sha256:102e1a3bff8f0401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# ISO8601Format(_:)

<sub>Instance Method</sub>

Generates a locale-aware string representation of a date using the ISO 8601 date format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ISO8601Format(_ style: Date.ISO8601FormatStyle = .init()) -> String
```

## Parameters

- `style` — A customized [ISO8601FormatStyle](iso8601formatstyle.md) to apply. By default, the method applies an unmodified ISO 8601 format style.

## Return Value

A string, formatted according to the specified style.

## Discussion

Calling this method is equivalent to passing a [ISO8601FormatStyle](iso8601formatstyle.md) to a date’s [formatted()](<formatted().md>) method.

## See Also

### Formatting a Date

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of a date using the default date format style.
- [formatted(date:time:)](<formatted(date_time_).md>) — Generates a locale-aware string representation of a date using specified date and time format styles.
- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of a date using the specified date format style.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
