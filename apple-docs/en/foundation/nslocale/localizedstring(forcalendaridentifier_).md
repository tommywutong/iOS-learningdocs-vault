---
title: 'localizedString(forCalendarIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/localizedstring(forcalendaridentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcalendaridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/localizedstring%28forcalendaridentifier%3A%29.json'
content_hash: 'sha256:01e061d6abbbb2cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# localizedString(forCalendarIdentifier:)

<sub>Instance Method</sub>

Returns the localized string for the specified calendar identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(forCalendarIdentifier calendarIdentifier: String) -> String?
```

## Parameters

- `calendarIdentifier` — The calendar identifier indicating the calendar whose name you want. Use one of the values listed in `Calendar Identifiers`.

## Return Value

A human readable string suitable for display to the user corresponding to the given calendar.

## Discussion

For example, on an American English (`en_US`) locale, passing [NSCalendarIdentifierGregorian](../nscalendar/identifier/gregorian.md) as the identifier, produces the string `"Gregorian Calendar"`.

## See Also

### Getting Display Information About a Locale

- [- localizedStringForLocaleIdentifier:](<localizedstring(forlocaleidentifier_).md>) — Returns the localized string for the specified locale identifier.
- [- localizedStringForCountryCode:](<localizedstring(forcountrycode_).md>) — Returns the localized string for a country or region code.
- [- localizedStringForLanguageCode:](<localizedstring(forlanguagecode_).md>) — Returns the localized string for the specified language code.
- [- localizedStringForScriptCode:](<localizedstring(forscriptcode_).md>) — Returns the localized string for the specified script code.
- [- localizedStringForVariantCode:](<localizedstring(forvariantcode_).md>) — Returns the localized string for the specified variant code.
- [- localizedStringForCollationIdentifier:](<localizedstring(forcollationidentifier_).md>) — Returns the localized string for the specified collation identifier.
- [- localizedStringForCollatorIdentifier:](<localizedstring(forcollatoridentifier_).md>) — Returns the localized string for the specified collator identifier.
- [- localizedStringForCurrencyCode:](<localizedstring(forcurrencycode_).md>) — Returns the localized string for the specified currency code.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md) — The types of calendars.
