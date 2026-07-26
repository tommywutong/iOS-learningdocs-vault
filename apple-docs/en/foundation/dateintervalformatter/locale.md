---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/locale
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/locale.json'
content_hash: 'sha256:89ceb7d95861bac4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateIntervalFormatter](../dateintervalformatter.md)

# locale

<sub>Instance Property</sub>

The locale to use when formatting date and time values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale! { get set }
```

## Discussion

The default value of this property is the current user’s locale, which is accessible from the [currentLocale](../nslocale/current.md) method of [NSLocale](../nslocale.md). You can change this value to a different locale to generate strings based on that locale.

## See Also

### Configuring the Formatter Options

- [dateStyle](datestyle.md) — The style to use when formatting day, month, and year information.
- [timeStyle](timestyle.md) — The style to use when formatting hour, minute, and second information.
- [dateTemplate](datetemplate.md) — The template for formatting one date and time value.
- [calendar](calendar.md) — The calendar to use for date values.
- [timeZone](timezone.md) — The time zone with which to specify time values.
