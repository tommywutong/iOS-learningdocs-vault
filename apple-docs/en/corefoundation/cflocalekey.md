---
title: CFLocaleKey
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalekey
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalekey.json'
content_hash: 'sha256:8472a2b4df3ad74c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFLocaleKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kCFLocaleAlternateQuotationBeginDelimiterKey](cflocalekey/alternatequotationbegindelimiterkey.md) — Specifies the alternating begin quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationBeginDelimiterKey`, then `NSLocaleAlternateQuotationBeginDelimiterKey`, and so on.
- [kCFLocaleAlternateQuotationEndDelimiterKey](cflocalekey/alternatequotationenddelimiterkey.md) — Specifies the alternating end quotation symbol associated with the locale. In some locales, when quotations are nested, the quotation characters alternate. Thus, `NSLocaleQuotationEndDelimiterKey`, then `NSLocaleAlternateQuotationEndDelimiterKey`, and so on.
- [kCFLocaleCalendar](cflocalekey/calendar.md) — Specifies the locale calendar.
- [kCFLocaleCalendarIdentifier](cflocalekey/calendaridentifier.md) — Specifies the locale calendar identifier.
- [kCFLocaleCollationIdentifier](cflocalekey/collationidentifier.md) — Specifies the locale collation identifier.
- [kCFLocaleCollatorIdentifier](cflocalekey/collatoridentifier.md) — Specifies the collation identifier for the locale.
- [kCFLocaleCountryCode](cflocalekey/countrycode.md) — Specifies the locale country code.
- [kCFLocaleCurrencyCode](cflocalekey/currencycode.md) — Specifies the locale currency code.
- [kCFLocaleCurrencySymbol](cflocalekey/currencysymbol.md) — Specifies the currency symbol.
- [kCFLocaleDecimalSeparator](cflocalekey/decimalseparator.md) — Specifies the decimal point string.
- [kCFLocaleExemplarCharacterSet](cflocalekey/exemplarcharacterset.md) — Specifies the locale character set.
- [kCFLocaleGroupingSeparator](cflocalekey/groupingseparator.md) — Specifies the separator string between groups of digits.
- [kCFLocaleIdentifier](cflocalekey/identifier.md) — Specifies locale identifier.
- [kCFLocaleLanguageCode](cflocalekey/languagecode.md) — Specifies the locale language code.
- [kCFLocaleMeasurementSystem](cflocalekey/measurementsystem.md) — Specifies the measurement system used.
- [kCFLocaleQuotationBeginDelimiterKey](cflocalekey/quotationbegindelimiterkey.md) — Specifies the begin quotation symbol associated with the locale.
- [kCFLocaleQuotationEndDelimiterKey](cflocalekey/quotationenddelimiterkey.md) — Specifies the end quotation symbol associated with the locale.
- [kCFLocaleScriptCode](cflocalekey/scriptcode.md) — Specifies the locale script code.
- [kCFLocaleUsesMetricSystem](cflocalekey/usesmetricsystem.md) — Specifies the whether the locale uses the metric system.
- [kCFLocaleVariantCode](cflocalekey/variantcode.md) — Specifies the locale variant code.

### Initializers

- [init(rawValue:)](<cflocalekey/init(rawvalue_).md>)

## See Also

### Data Types

- [CFAllocatorTypeID](cfallocatortypeid.md)
- [CFCalendarIdentifier](cfcalendaridentifier.md)
- [CFDateFormatterKey](cfdateformatterkey.md)
- [CFErrorDomain](cferrordomain.md)
- [CFLocaleIdentifier](cflocaleidentifier.md)
- [CFNotificationName](cfnotificationname.md)
- [CFNumberFormatterKey](cfnumberformatterkey.md)
- [CFRunLoopMode](cfrunloopmode.md)
- [CFStreamPropertyKey](cfstreampropertykey.md)
- [CFTypeRef](cftyperef.md) — An untyped “generic” reference to any Core Foundation object.
