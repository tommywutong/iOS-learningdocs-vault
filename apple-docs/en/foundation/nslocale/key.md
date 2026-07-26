---
title: NSLocale.Key
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/key
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/key'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/key.json'
content_hash: 'sha256:6b1952bbf846f9d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# NSLocale.Key

<sub>Structure</sub>

The keys used to access components of a locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Key
```

## Discussion

Use these keys with the methods [- objectForKey:](<object(forkey_).md>) and [- displayNameForKey:value:](<displayname(forkey_value_).md>).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<key/init(rawvalue_).md>)

### Keys

- [NSLocaleIdentifier](key/identifier.md) — The locale identifier.
- [NSLocaleCountryCode](key/countrycode.md) — The locale country or region code.
- [NSLocaleLanguageCode](key/languagecode.md) — The locale language code.
- [NSLocaleScriptCode](key/scriptcode.md) — The locale script code.
- [NSLocaleVariantCode](key/variantcode.md) — The locale variant code.
- [NSLocaleExemplarCharacterSet](key/exemplarcharacterset.md) — The exemplar character set for the locale.
- [NSLocaleCalendar](key/calendar.md) — The calendar associated with the locale.
- [NSLocaleCollationIdentifier](key/collationidentifier.md) — The collation associated with the locale.
- [NSLocaleCollatorIdentifier](key/collatoridentifier.md) — The collation identifier for the locale.
- [NSLocaleUsesMetricSystem](key/usesmetricsystem.md) — A flag that indicates whether the locale uses the metric system.
- [NSLocaleMeasurementSystem](key/measurementsystem.md) — The measurement system associated with the locale.
- [NSLocaleDecimalSeparator](key/decimalseparator.md) — The decimal separator associated with the locale.
- [NSLocaleGroupingSeparator](key/groupingseparator.md) — The numeric grouping separator associated with the locale.
- [NSLocaleCurrencySymbol](key/currencysymbol.md) — The currency symbol associated with the locale.
- [NSLocaleCurrencyCode](key/currencycode.md) — The currency code associated with the locale.
- [NSLocaleQuotationEndDelimiterKey](key/quotationenddelimiterkey.md) — The end quotation symbol associated with the locale.
- [NSLocaleQuotationBeginDelimiterKey](key/quotationbegindelimiterkey.md) — The begin quotation symbol associated with the locale.
- [NSLocaleAlternateQuotationEndDelimiterKey](key/alternatequotationenddelimiterkey.md) — The alternate end quotation symbol associated with the locale.
- [NSLocaleAlternateQuotationBeginDelimiterKey](key/alternatequotationbegindelimiterkey.md) — The alternating begin quotation symbol associated with the locale.

## See Also

### Accessing Locale Information by Key

- [- objectForKey:](<object(forkey_).md>) — Returns the value of the component corresponding to the specified key.
- [- displayNameForKey:value:](<displayname(forkey_value_).md>) — Returns the display name for the given locale component value.
