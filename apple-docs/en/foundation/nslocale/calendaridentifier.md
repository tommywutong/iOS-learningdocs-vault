---
title: calendarIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/calendaridentifier
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/calendaridentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/calendaridentifier.json'
content_hash: 'sha256:1579d45448470b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# calendarIdentifier

<sub>Instance Property</sub>

The calendar identifier for the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var calendarIdentifier: String { get }
```

## Discussion

Possible values are listed in `Calendar Identifiers`.

Use [- localizedStringForCalendarIdentifier:](<localizedstring(forcalendaridentifier_).md>) to obtain a version of the value suitable for display to the user.

## See Also

### Getting Information About a Locale

- [localeIdentifier](localeidentifier.md) — The identifier for the locale.
- [countryCode](countrycode.md) — The country or region code for the locale. _(deprecated)_
- [languageCode](languagecode.md) — The language code for the locale.
- [scriptCode](scriptcode.md) — The script code for the locale.
- [variantCode](variantcode.md) — The variant code for the locale.
- [exemplarCharacterSet](exemplarcharacterset.md) — The exemplar character set for the locale.
- [collationIdentifier](collationidentifier.md) — The collation identifier for the locale.
- [collatorIdentifier](collatoridentifier.md) — The collator identifier for the locale.
- [usesMetricSystem](usesmetricsystem.md) — A Boolean value that indicates whether the locale uses the metric system.
- [decimalSeparator](decimalseparator.md) — The decimal separator for the locale.
- [groupingSeparator](groupingseparator.md) — The grouping separator for the locale.
- [currencyCode](currencycode.md) — The currency code for the locale.
- [currencySymbol](currencysymbol.md) — The currency symbol for the locale.
- [quotationBeginDelimiter](quotationbegindelimiter.md) — The begin quotation symbol for the locale.
- [quotationEndDelimiter](quotationenddelimiter.md) — The end quotation symbol for the locale.
