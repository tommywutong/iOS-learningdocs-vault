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
doc_path: '/documentation/foundation/date/relativeformatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:e2bb267cddb5fd60'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the relative date format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Date.RelativeFormatStyle
```

## Parameters

- `locale` — The locale to use when formatting relative dates.

## Return Value

A relative date format style with the provided locale.

## See Also

### Modifying a Relative Date Format Style

- [presentation](presentation-swift.property.md) — Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [calendar](calendar.md) — The calendar to use when formatting relative dates.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the relative dates.
- [locale](locale.md) — The locale to use when formatting the relative date.
