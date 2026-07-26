---
title: countryCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（27.0 起废弃）, iPadOS 10.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.12+（27.0 起废弃）, tvOS 10.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 3.0+（27.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslocale/countrycode
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/countrycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/countrycode.json'
content_hash: 'sha256:e7ba2c6565a144ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# countryCode

<sub>Instance Property</sub>

The country or region code for the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countryCode: String? { get }
```

## Discussion

Examples of country or region codes include `"GB"`, `"FR"`, and `"HK"`.

Use [- localizedStringForCountryCode:](<localizedstring(forcountrycode_).md>) to obtain a version of the value suitable for display to the user.

This property contains the same value returned by the [- objectForKey:](<object(forkey_).md>) method when passing the [NSLocaleCountryCode](key/countrycode.md) key.

## See Also

### Related Documentation

- [ISOCountryCodes](isocountrycodes.md) — The list of known country or region codes.

### Getting Information About a Locale

- [localeIdentifier](localeidentifier.md) — The identifier for the locale.
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
- [calendarIdentifier](calendaridentifier.md) — The calendar identifier for the locale.
- [quotationBeginDelimiter](quotationbegindelimiter.md) — The begin quotation symbol for the locale.
- [quotationEndDelimiter](quotationenddelimiter.md) — The end quotation symbol for the locale.
