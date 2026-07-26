---
title: 'localizedString(forLocaleIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localizedstring(forlocaleidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forlocaleidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localizedstring%28forlocaleidentifier%3A%29.json'
content_hash: 'sha256:9c9925623830c6c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localizedString(forLocaleIdentifier:)

<sub>Instance Method</sub>

Returns the localized string for the specified locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(forLocaleIdentifier localeIdentifier: String) -> String
```

## Parameters

- `localeIdentifier` — The identifier for which you want the localized name.

## Return Value

The localized name of the locale.

## Discussion

For example, calling this method on an American English (`en_US`) locale, passing `"fr_FR"` for `localeIdentifier`, produces the string `"French (France)"`.

This method is equivalent to calling the [- displayNameForKey:value:](<displayname(forkey_value_).md>) method passing the [NSLocaleIdentifier](key/identifier.md) key and `localeIdentifier` value.

## See Also

### Related Documentation

- [availableLocaleIdentifiers](availablelocaleidentifiers.md) — The list of locale identifiers available on the system.

### Getting Display Information About a Locale

- [- localizedStringForCountryCode:](<localizedstring(forcountrycode_).md>) — Returns the localized string for a country or region code.
- [- localizedStringForLanguageCode:](<localizedstring(forlanguagecode_).md>) — Returns the localized string for the specified language code.
- [- localizedStringForScriptCode:](<localizedstring(forscriptcode_).md>) — Returns the localized string for the specified script code.
- [- localizedStringForVariantCode:](<localizedstring(forvariantcode_).md>) — Returns the localized string for the specified variant code.
- [- localizedStringForCollationIdentifier:](<localizedstring(forcollationidentifier_).md>) — Returns the localized string for the specified collation identifier.
- [- localizedStringForCollatorIdentifier:](<localizedstring(forcollatoridentifier_).md>) — Returns the localized string for the specified collator identifier.
- [- localizedStringForCurrencyCode:](<localizedstring(forcurrencycode_).md>) — Returns the localized string for the specified currency code.
- [- localizedStringForCalendarIdentifier:](<localizedstring(forcalendaridentifier_).md>) — Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md) — The types of calendars.
