---
title: 'identifier(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/identifier(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/identifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/identifier%28_%3A%29.json'
content_hash: 'sha256:b7f066812de9073f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# identifier(_:)

<sub>Instance Method</sub>

Returns the locale identifier, in the specified standard format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func identifier(_ type: Locale.IdentifierType) -> String
```

## Parameters

- `type` — The standard locale identifier format to use for the returned string.

## Return Value

The locale identifier, formatted in accordance with the specified identifier type.

## See Also

### Getting information about a locale

- [identifier](identifier.md) — The identifier of the locale.
- [IdentifierType](identifiertype.md) — A type that indicates the standard that defines a locale’s identifier.
- [calendar](calendar.md) — The calendar for the locale, or the Gregorian calendar as a fallback.
- [regionCode](regioncode.md) — The region code of the locale, or `nil` if it has none.
- [languageCode](languagecode-swift.property.md) — The language code of the locale, or `nil` if has none.
- [scriptCode](scriptcode.md) — The script code of the locale, or `nil` if has none.
- [variantCode](variantcode.md) — The variant code for the locale, or `nil` if it has none.
- [exemplarCharacterSet](exemplarcharacterset.md) — The exemplar character set for the locale, or `nil` if has none.
- [collationIdentifier](collationidentifier.md) — The collation identifier for the locale, or `nil` if it has none.
- [collatorIdentifier](collatoridentifier.md) — The collator identifier of the locale.
- [usesMetricSystem](usesmetricsystem.md) — A Boolean that is true if the locale uses the metric system. _(deprecated)_
- [decimalSeparator](decimalseparator.md) — The decimal separator of the locale.
- [groupingSeparator](groupingseparator.md) — The grouping separator of the locale.
- [currencyCode](currencycode.md) — The currency code of the locale.
- [currencySymbol](currencysymbol.md) — The currency symbol of the locale.
