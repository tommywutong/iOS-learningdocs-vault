---
title: Locale Property Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/locale-property-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/locale-property-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/locale-property-keys.json'
content_hash: 'sha256:df2e8d0467eb4022'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFLocale](cflocale.md)

# Locale Property Keys

<sub>API Collection</sub>

Predefined locale keys used to get property values.

## Overview

Locale objects use key-value pairs to store property values. Use the [CFLocaleGetValue](<cflocalegetvalue(____).md>) function to get the value of a specific property listed above.

## Topics

### Constants

- [kCFLocaleIdentifier](cflocalekey/identifier.md) — Specifies locale identifier.
- [kCFLocaleLanguageCode](cflocalekey/languagecode.md) — Specifies the locale language code.
- [kCFLocaleCountryCode](cflocalekey/countrycode.md) — Specifies the locale country code.
- [kCFLocaleScriptCode](cflocalekey/scriptcode.md) — Specifies the locale script code.
- [kCFLocaleVariantCode](cflocalekey/variantcode.md) — Specifies the locale variant code.
- [kCFLocaleExemplarCharacterSet](cflocalekey/exemplarcharacterset.md) — Specifies the locale character set.
- [kCFLocaleCalendarIdentifier](cflocalekey/calendaridentifier.md) — Specifies the locale calendar identifier.
- [kCFLocaleCalendar](cflocalekey/calendar.md) — Specifies the locale calendar.
- [kCFLocaleCollationIdentifier](cflocalekey/collationidentifier.md) — Specifies the locale collation identifier.
- [kCFLocaleUsesMetricSystem](cflocalekey/usesmetricsystem.md) — Specifies the whether the locale uses the metric system.
- [kCFLocaleMeasurementSystem](cflocalekey/measurementsystem.md) — Specifies the measurement system used.
- [kCFLocaleDecimalSeparator](cflocalekey/decimalseparator.md) — Specifies the decimal point string.
- [kCFLocaleGroupingSeparator](cflocalekey/groupingseparator.md) — Specifies the separator string between groups of digits.
- [kCFLocaleCurrencySymbol](cflocalekey/currencysymbol.md) — Specifies the currency symbol.
- [kCFLocaleCurrencyCode](cflocalekey/currencycode.md) — Specifies the locale currency code.
- [kCFLocaleCollatorIdentifier](cflocalekey/collatoridentifier.md) — Specifies the collation identifier for the locale.
- [kCFLocaleQuotationBeginDelimiterKey](cflocalekey/quotationbegindelimiterkey.md) — Specifies the begin quotation symbol associated with the locale.
- [kCFLocaleQuotationEndDelimiterKey](cflocalekey/quotationenddelimiterkey.md) — Specifies the end quotation symbol associated with the locale.
- [kCFLocaleAlternateQuotationBeginDelimiterKey](cflocalekey/alternatequotationbegindelimiterkey.md) — Specifies the alternating begin quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationBeginDelimiterKey`, then `NSLocaleAlternateQuotationBeginDelimiterKey`, and so on.
- [kCFLocaleAlternateQuotationEndDelimiterKey](cflocalekey/alternatequotationenddelimiterkey.md) — Specifies the alternating end quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationEndDelimiterKey`, then `NSLocaleAlternateQuotationEndDelimiterKey`, and so on.

## See Also

### Constants

- [CFLocaleLanguageDirection](cflocalelanguagedirection.md) — These constants describe the text direction for a language. They are returned by the functions [CFLocaleGetLanguageCharacterDirection](<cflocalegetlanguagecharacterdirection(__).md>) and [CFLocaleGetLanguageLineDirection](<cflocalegetlanguagelinedirection(__).md>).
- [Locale Calendar Identifiers](locale-calendar-identifiers.md) — Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](locale-change-notification.md) — Identifier for notification sent if the current locale changes.
