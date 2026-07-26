---
title: 'localizedString(forCountryCode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localizedstring(forcountrycode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcountrycode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localizedstring%28forcountrycode%3A%29.json'
content_hash: 'sha256:8bc94008e5cc57ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localizedString(forCountryCode:)

<sub>Instance Method</sub>

Returns the localized string for a country or region code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(forCountryCode countryCode: String) -> String?
```

## Parameters

- `countryCode` — The code of the country or region that indicates the name you want.

## Return Value

The localized name of the country or region.

## Discussion

For example, calling this method on an American English (`en_US`) locale, passing `"GB"` for `countryCode`, produces the string `"United Kingdom"`.

This method is equivalent to calling the [- displayNameForKey:value:](<displayname(forkey_value_).md>) method passing the [NSLocaleCountryCode](key/countrycode.md) key and `countryCode` value.

## See Also

### Related Documentation

- [ISOCountryCodes](isocountrycodes.md) — The list of known country or region codes.

### Getting Display Information About a Locale

- [- localizedStringForLocaleIdentifier:](<localizedstring(forlocaleidentifier_).md>) — Returns the localized string for the specified locale identifier.
- [- localizedStringForLanguageCode:](<localizedstring(forlanguagecode_).md>) — Returns the localized string for the specified language code.
- [- localizedStringForScriptCode:](<localizedstring(forscriptcode_).md>) — Returns the localized string for the specified script code.
- [- localizedStringForVariantCode:](<localizedstring(forvariantcode_).md>) — Returns the localized string for the specified variant code.
- [- localizedStringForCollationIdentifier:](<localizedstring(forcollationidentifier_).md>) — Returns the localized string for the specified collation identifier.
- [- localizedStringForCollatorIdentifier:](<localizedstring(forcollatoridentifier_).md>) — Returns the localized string for the specified collator identifier.
- [- localizedStringForCurrencyCode:](<localizedstring(forcurrencycode_).md>) — Returns the localized string for the specified currency code.
- [- localizedStringForCalendarIdentifier:](<localizedstring(forcalendaridentifier_).md>) — Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md) — The types of calendars.
