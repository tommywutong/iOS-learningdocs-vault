---
title: scriptCode
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalekey/scriptcode
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalekey/scriptcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalekey/scriptcode.json'
content_hash: 'sha256:07637a5f0f35a850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFLocaleKey](../cflocalekey.md)

# scriptCode

<sub>Type Property</sub>

Specifies the locale script code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let scriptCode: CFLocaleKey!
```

## Discussion

The corresponding value is a CFString containing a Unicode script tag (strictly, an ISO 15924 script tag). Usually this is empty (it is for “`ja_JP`”). It may be present for locales where a script _must_ be specified, for example “`uz-Latn-UZ`” vs. “`uz-Cyrl-UZ`” for Uzbek in Latin vs. Cyrillic (in the first case the script code is “`Latn`”, and in the second it is “`Cyrl`”).

## See Also

### Constants

- [kCFLocaleIdentifier](identifier.md) — Specifies locale identifier.
- [kCFLocaleLanguageCode](languagecode.md) — Specifies the locale language code.
- [kCFLocaleCountryCode](countrycode.md) — Specifies the locale country code.
- [kCFLocaleVariantCode](variantcode.md) — Specifies the locale variant code.
- [kCFLocaleExemplarCharacterSet](exemplarcharacterset.md) — Specifies the locale character set.
- [kCFLocaleCalendarIdentifier](calendaridentifier.md) — Specifies the locale calendar identifier.
- [kCFLocaleCalendar](calendar.md) — Specifies the locale calendar.
- [kCFLocaleCollationIdentifier](collationidentifier.md) — Specifies the locale collation identifier.
- [kCFLocaleUsesMetricSystem](usesmetricsystem.md) — Specifies the whether the locale uses the metric system.
- [kCFLocaleMeasurementSystem](measurementsystem.md) — Specifies the measurement system used.
- [kCFLocaleDecimalSeparator](decimalseparator.md) — Specifies the decimal point string.
- [kCFLocaleGroupingSeparator](groupingseparator.md) — Specifies the separator string between groups of digits.
- [kCFLocaleCurrencySymbol](currencysymbol.md) — Specifies the currency symbol.
- [kCFLocaleCurrencyCode](currencycode.md) — Specifies the locale currency code.
- [kCFLocaleCollatorIdentifier](collatoridentifier.md) — Specifies the collation identifier for the locale.
