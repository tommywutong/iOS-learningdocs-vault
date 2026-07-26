---
title: variantCode
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalekey/variantcode
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalekey/variantcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalekey/variantcode.json'
content_hash: 'sha256:e2b03af864ae2704'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFLocaleKey](../cflocalekey.md)

# variantCode

<sub>Type Property</sub>

Specifies the locale variant code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let variantCode: CFLocaleKey!
```

## Discussion

The corresponding value is a CFString containing the variant name. The variant code is arbitrary and application-specific. ICU adds “`_EURO`”  to its locale designations for locales that support the Euro currency. For  “`en_US_POSIX`” the variant is “`POSIX`”, and for “`hy_AM_REVISED`” it is “`REVISED`”.

## See Also

### Constants

- [kCFLocaleIdentifier](identifier.md) — Specifies locale identifier.
- [kCFLocaleLanguageCode](languagecode.md) — Specifies the locale language code.
- [kCFLocaleCountryCode](countrycode.md) — Specifies the locale country code.
- [kCFLocaleScriptCode](scriptcode.md) — Specifies the locale script code.
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
