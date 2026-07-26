---
title: 'localizedString(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/localizedstring(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/localizedstring(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/localizedstring%28for%3A%29.json'
content_hash: 'sha256:ecc99e68d8202004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# localizedString(for:)

<sub>Instance Method</sub>

Returns a localized string for a specified calendar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localizedString(for calendarIdentifier: Calendar.Identifier) -> String?
```

## Discussion

For example, in the “en” locale, the result for `.buddhist` is `"Buddhist Calendar"`.

## See Also

### Getting display information about a locale

- [localizedString(forCollationIdentifier:)](<localizedstring(forcollationidentifier_).md>) — Returns a localized string for a specified ICU collation identifier.
- [localizedString(forCollatorIdentifier:)](<localizedstring(forcollatoridentifier_).md>) — Returns a localized string for a specified ICU collator identifier.
- [localizedString(forCurrencyCode:)](<localizedstring(forcurrencycode_).md>) — Returns a localized string for a specified ISO 4217 currency code.
- [localizedString(forIdentifier:)](<localizedstring(foridentifier_).md>) — Returns a localized string for a specified locale identifier.
- [localizedString(forLanguageCode:)](<localizedstring(forlanguagecode_).md>) — Returns a localized string for a specified language code.
- [localizedString(forRegionCode:)](<localizedstring(forregioncode_).md>) — Returns a localized string for a specified region code.
- [localizedString(forScriptCode:)](<localizedstring(forscriptcode_).md>) — Returns a localized string for a specified script code.
- [localizedString(forVariantCode:)](<localizedstring(forvariantcode_).md>) — Returns a localized string for a specified variant code.
