---
title: localeIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/localeidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localeidentifier.json'
content_hash: 'sha256:27a61df351596c04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localeIdentifier

<sub>Instance Property</sub>

The identifier for the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localeIdentifier: String { get }
```

## Discussion

Examples of locale identifiers include `"en_GB"`, `"es_ES_PREEURO"`, and `"zh-Hant_HK_POSIX@collation=pinyin;currency=CNY"`.

Use [localizedString(forIdentifier:)](<../locale/localizedstring(foridentifier_).md>) to obtain a version of the value suitable for display to the user.

> [!note] Note
> The value held in the property may differ from the identifier used to initialize the locale because [NSLocale](../nslocale.md) may canonicalize it during initialization.

This property contains the same value returned by the [- objectForKey:](<object(forkey_).md>) method when passing the [NSLocaleIdentifier](key/identifier.md) key.

## See Also

### Related Documentation

- [availableLocaleIdentifiers](availablelocaleidentifiers.md) — The list of locale identifiers available on the system.

### Getting Information About a Locale

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
- [calendarIdentifier](calendaridentifier.md) — The calendar identifier for the locale.
- [quotationBeginDelimiter](quotationbegindelimiter.md) — The begin quotation symbol for the locale.
- [quotationEndDelimiter](quotationenddelimiter.md) — The end quotation symbol for the locale.
