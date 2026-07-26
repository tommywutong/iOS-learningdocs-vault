---
title: usesMetricSystem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/key/usesmetricsystem
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/key/usesmetricsystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/key/usesmetricsystem.json'
content_hash: 'sha256:1c21bac0eadf8d57'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSLocale](../../nslocale.md) · [Key](../key.md)

# usesMetricSystem

<sub>Type Property</sub>

A flag that indicates whether the locale uses the metric system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let usesMetricSystem: NSLocale.Key
```

## Discussion

The corresponding value is a `NSNumber` object containing a Boolean value. If the value is [false](../../../swift/false.md), you can typically assume American measurement units (for example, the statute mile).

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
- [NSLocaleMeasurementSystem](measurementsystem.md) — The measurement system associated with the locale.
- [NSLocaleDecimalSeparator](decimalseparator.md) — The decimal separator associated with the locale.
- [NSLocaleGroupingSeparator](groupingseparator.md) — The numeric grouping separator associated with the locale.
- [NSLocaleCurrencySymbol](currencysymbol.md) — The currency symbol associated with the locale.
- [NSLocaleCurrencyCode](currencycode.md) — The currency code associated with the locale.
- [NSLocaleQuotationEndDelimiterKey](quotationenddelimiterkey.md) — The end quotation symbol associated with the locale.
