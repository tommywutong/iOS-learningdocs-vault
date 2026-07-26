---
title: alternateQuotationBeginDelimiterKey
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalekey/alternatequotationbegindelimiterkey
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalekey/alternatequotationbegindelimiterkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalekey/alternatequotationbegindelimiterkey.json'
content_hash: 'sha256:f9ab080a8dc8098e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFLocaleKey](../cflocalekey.md)

# alternateQuotationBeginDelimiterKey

<sub>Type Property</sub>

Specifies the alternating begin quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationBeginDelimiterKey`, then `NSLocaleAlternateQuotationBeginDelimiterKey`, and so on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let alternateQuotationBeginDelimiterKey: CFLocaleKey!
```

## Discussion

The corresponding value is a CFString object.

## See Also

### Constants

- [kCFLocaleIdentifier](identifier.md) — Specifies locale identifier.
- [kCFLocaleLanguageCode](languagecode.md) — Specifies the locale language code.
- [kCFLocaleCountryCode](countrycode.md) — Specifies the locale country code.
- [kCFLocaleScriptCode](scriptcode.md) — Specifies the locale script code.
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
