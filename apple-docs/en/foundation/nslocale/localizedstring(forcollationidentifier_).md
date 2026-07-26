---
title: 'localizedString(forCollationIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localizedstring(forcollationidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcollationidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localizedstring%28forcollationidentifier%3A%29.json'
content_hash: 'sha256:979f3791be9771f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localizedString(forCollationIdentifier:)

<sub>Instance Method</sub>

Returns the localized string for the specified collation identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(forCollationIdentifier collationIdentifier: String) -> String?
```

## Parameters

- `collationIdentifier` — The identifier for the collation whose name you want.

## Return Value

The localized name for the collation.

## Discussion

For example, calling this method on an American English (`en_US`) locale, passing `"phonebook"` for `collationIdentifier`, produces the string `"Phonebook Sort Order"`.

This method is equivalent to calling the [- displayNameForKey:value:](<displayname(forkey_value_).md>) method passing the [NSLocaleCollationIdentifier](key/collationidentifier.md) key and `collationIdentifier` value.

## See Also

### Getting Display Information About a Locale

- [- localizedStringForLocaleIdentifier:](<localizedstring(forlocaleidentifier_).md>) — Returns the localized string for the specified locale identifier.
- [- localizedStringForCountryCode:](<localizedstring(forcountrycode_).md>) — Returns the localized string for a country or region code.
- [- localizedStringForLanguageCode:](<localizedstring(forlanguagecode_).md>) — Returns the localized string for the specified language code.
- [- localizedStringForScriptCode:](<localizedstring(forscriptcode_).md>) — Returns the localized string for the specified script code.
- [- localizedStringForVariantCode:](<localizedstring(forvariantcode_).md>) — Returns the localized string for the specified variant code.
- [- localizedStringForCollatorIdentifier:](<localizedstring(forcollatoridentifier_).md>) — Returns the localized string for the specified collator identifier.
- [- localizedStringForCurrencyCode:](<localizedstring(forcurrencycode_).md>) — Returns the localized string for the specified currency code.
- [- localizedStringForCalendarIdentifier:](<localizedstring(forcalendaridentifier_).md>) — Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md) — The types of calendars.
