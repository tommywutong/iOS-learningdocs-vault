---
title: alternateQuotationBeginDelimiterKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/key/alternatequotationbegindelimiterkey
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/key/alternatequotationbegindelimiterkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/key/alternatequotationbegindelimiterkey.json'
content_hash: 'sha256:38b4fc0da6b3e4e4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSLocale](../../nslocale.md) · [Key](../key.md)

# alternateQuotationBeginDelimiterKey

<sub>Type Property</sub>

The alternating begin quotation symbol associated with the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let alternateQuotationBeginDelimiterKey: NSLocale.Key
```

## Discussion

The corresponding value is an `NSString` object; for example, `"‘"`, `"‹"`, or `"『"`.

In some locales, when quotations are nested, the quotation characters alternate. Thus, [NSLocaleQuotationBeginDelimiterKey](quotationbegindelimiterkey.md), then [NSLocaleAlternateQuotationBeginDelimiterKey](alternatequotationbegindelimiterkey.md), etc.

## See Also

### Keys

- [NSLocaleIdentifier](identifier.md) — The locale identifier.
- [NSLocaleCountryCode](countrycode.md) — The locale country or region code.
- [NSLocaleLanguageCode](languagecode.md) — The locale language code.
- [NSLocaleScriptCode](scriptcode.md) — The locale script code.
- [NSLocaleVariantCode](variantcode.md) — The locale variant code.
- [NSLocaleExemplarCharacterSet](exemplarcharacterset.md) — The exemplar character set for the locale.
- [NSLocaleCalendar](calendar.md) — The calendar associated with the locale.
- [NSLocaleCollationIdentifier](collationidentifier.md) — The collation associated with the locale.
- [NSLocaleCollatorIdentifier](collatoridentifier.md) — The collation identifier for the locale.
- [NSLocaleUsesMetricSystem](usesmetricsystem.md) — A flag that indicates whether the locale uses the metric system.
- [NSLocaleMeasurementSystem](measurementsystem.md) — The measurement system associated with the locale.
- [NSLocaleDecimalSeparator](decimalseparator.md) — The decimal separator associated with the locale.
- [NSLocaleGroupingSeparator](groupingseparator.md) — The numeric grouping separator associated with the locale.
- [NSLocaleCurrencySymbol](currencysymbol.md) — The currency symbol associated with the locale.
- [NSLocaleCurrencyCode](currencycode.md) — The currency code associated with the locale.
