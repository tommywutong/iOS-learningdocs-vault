---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/locale
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/locale.json'
content_hash: 'sha256:46bb7716d7877c64'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# locale

<sub>Instance Property</sub>

The locale to use when formatting the relative date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale
```

## Discussion

The default value is [autoupdatingCurrentLocale](../../nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the format style resets to using [autoupdatingCurrentLocale](../../nslocale/autoupdatingcurrent.md).

## See Also

### Modifying a Relative Date Format Style

- [presentation](presentation-swift.property.md) — Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [calendar](calendar.md) — The calendar to use when formatting relative dates.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the relative dates.
- [locale(_:)](<locale(__).md>) — Modifies the relative date format style to use the specified locale.
