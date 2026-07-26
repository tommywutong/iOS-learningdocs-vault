---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:f00a91978632989c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Date.FormatStyle
```

## Parameters

- `locale` — The locale to use when formatting a date.

## Return Value

A date format style with the provided locale.

## See Also

### Modifying a Date Format Style

- [timeZone](timezone.md) — The time zone to use when formatting the date and time components.
- [calendar](calendar.md) — The calendar to use when formatting the date.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the date.
- [locale](locale.md) — The locale to use when formatting the date and time components.
