---
title: 'timeZone(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/intervalformatstyle/timezone(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/timezone(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/timezone%28_%3A%29.json'
content_hash: 'sha256:fc5c87e6abd8864b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# timeZone(_:)

<sub>Instance Method</sub>

Modifies the date interval format style to use the specified time zone format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeZone(_ format: Date.IntervalFormatStyle.Symbol.TimeZone = .genericName(.short)) -> Date.IntervalFormatStyle
```

## Parameters

- `format` — The time zone format style for formatting a date interval.

## Return Value

A date interval format style with the provided time zone format.

## See Also

### Specifying Date Interval Format Styles

- [locale(_:)](<locale(__).md>) — Modifies the date interval format style to use the specified locale.
- [calendar](calendar.md) — The calendar for formatting the date interval.
- [locale](locale.md) — The locale for formatting the date and time interval components.
- [timeZone](timezone.md) — The time zone for formatting the date interval components.
