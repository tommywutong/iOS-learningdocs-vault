---
title: identifier
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalekey/identifier
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalekey/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalekey/identifier.json'
content_hash: 'sha256:affb3ae083a1c7d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFLocaleKey](../cflocalekey.md)

# identifier

<sub>Type Property</sub>

Specifies locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let identifier: CFLocaleKey!
```

## Discussion

The corresponding value is a CFString containing the POSIX locale identifier as used by ICU, such as “`ja_JP`”. If you have a variant locale or a different currency or calendar, it can be as complex as “`en_US_POSIX@calendar=japanese;currency=EUR`” or “`az_Cyrl_AZ@calendar=buddhist;currency=JPY`”.

## See Also

### Constants

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
- [kCFLocaleCollatorIdentifier](collatoridentifier.md) — Specifies the collation identifier for the locale.
