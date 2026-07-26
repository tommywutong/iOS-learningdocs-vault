---
title: exemplarCharacterSet
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/exemplarcharacterset
source_url: 'https://developer.apple.com/documentation/foundation/locale/exemplarcharacterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/exemplarcharacterset.json'
content_hash: 'sha256:d555ec87996ec801'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# exemplarCharacterSet

<sub>Instance Property</sub>

The exemplar character set for the locale, or `nil` if has none.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var exemplarCharacterSet: CharacterSet? { get }
```

## See Also

### Getting information about a locale

- [identifier](identifier.md) — The identifier of the locale.
- [identifier(_:)](<identifier(__).md>) — Returns the locale identifier, in the specified standard format.
- [IdentifierType](identifiertype.md) — A type that indicates the standard that defines a locale’s identifier.
- [calendar](calendar.md) — The calendar for the locale, or the Gregorian calendar as a fallback.
- [regionCode](regioncode.md) — The region code of the locale, or `nil` if it has none.
- [languageCode](languagecode-swift.property.md) — The language code of the locale, or `nil` if has none.
- [scriptCode](scriptcode.md) — The script code of the locale, or `nil` if has none.
- [variantCode](variantcode.md) — The variant code for the locale, or `nil` if it has none.
- [collationIdentifier](collationidentifier.md) — The collation identifier for the locale, or `nil` if it has none.
- [collatorIdentifier](collatoridentifier.md) — The collator identifier of the locale.
- [usesMetricSystem](usesmetricsystem.md) — A Boolean that is true if the locale uses the metric system. _(deprecated)_
- [decimalSeparator](decimalseparator.md) — The decimal separator of the locale.
- [groupingSeparator](groupingseparator.md) — The grouping separator of the locale.
- [currencyCode](currencycode.md) — The currency code of the locale.
- [currencySymbol](currencysymbol.md) — The currency symbol of the locale.
