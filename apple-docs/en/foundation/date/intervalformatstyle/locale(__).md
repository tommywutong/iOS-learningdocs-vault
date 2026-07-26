---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/intervalformatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:f348454449c355ed'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the date interval format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Date.IntervalFormatStyle
```

## Parameters

- `locale` — The locale for formatting a date interval.

## Return Value

A date inteverval format style with the provided locale.

## See Also

### Specifying Date Interval Format Styles

- [timeZone(_:)](<timezone(__).md>) — Modifies the date interval format style to use the specified time zone format.
- [calendar](calendar.md) — The calendar for formatting the date interval.
- [locale](locale.md) — The locale for formatting the date and time interval components.
- [timeZone](timezone.md) — The time zone for formatting the date interval components.
