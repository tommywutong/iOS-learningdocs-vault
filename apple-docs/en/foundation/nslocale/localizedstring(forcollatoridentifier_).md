---
title: 'localizedString(forCollatorIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localizedstring(forcollatoridentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcollatoridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localizedstring%28forcollatoridentifier%3A%29.json'
content_hash: 'sha256:0e75ef57be17102a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localizedString(forCollatorIdentifier:)

<sub>Instance Method</sub>

Returns the localized string for the specified collator identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(forCollatorIdentifier collatorIdentifier: String) -> String?
```

## Parameters

- `collatorIdentifier` — The identifier for the collator whose name you want.

## Return Value

The localized name of the collator.

## Discussion

This method is equivalent to calling the [- displayNameForKey:value:](<displayname(forkey_value_).md>) method passing the [NSLocaleCollatorIdentifier](key/collatoridentifier.md) key and `collatorIdentifier` value.

## See Also

### Getting Display Information About a Locale

- [- localizedStringForLocaleIdentifier:](<localizedstring(forlocaleidentifier_).md>) — Returns the localized string for the specified locale identifier.
- [- localizedStringForCountryCode:](<localizedstring(forcountrycode_).md>) — Returns the localized string for a country or region code.
- [- localizedStringForLanguageCode:](<localizedstring(forlanguagecode_).md>) — Returns the localized string for the specified language code.
- [- localizedStringForScriptCode:](<localizedstring(forscriptcode_).md>) — Returns the localized string for the specified script code.
- [- localizedStringForVariantCode:](<localizedstring(forvariantcode_).md>) — Returns the localized string for the specified variant code.
- [- localizedStringForCollationIdentifier:](<localizedstring(forcollationidentifier_).md>) — Returns the localized string for the specified collation identifier.
- [- localizedStringForCurrencyCode:](<localizedstring(forcurrencycode_).md>) — Returns the localized string for the specified currency code.
- [- localizedStringForCalendarIdentifier:](<localizedstring(forcalendaridentifier_).md>) — Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md) — The types of calendars.
