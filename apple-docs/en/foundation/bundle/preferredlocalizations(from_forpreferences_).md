---
title: 'preferredLocalizations(from:forPreferences:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/preferredlocalizations(from:forpreferences:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/preferredlocalizations(from:forpreferences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/preferredlocalizations%28from%3Aforpreferences%3A%29.json'
content_hash: 'sha256:404ae85c09f6ee39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# preferredLocalizations(from:forPreferences:)

<sub>Type Method</sub>

Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func preferredLocalizations(from localizationsArray: [String], forPreferences preferencesArray: [String]?) -> [String]
```

## Parameters

- `localizationsArray` — An array of identifiers, each corresponding to a localization that a bundle can support.

- `preferencesArray` — An array of BCP 47 language codes corresponding to a user’s preferred languages. If this parameter is `nil`, the method uses the current user’s language preferences.

## Return Value

An array of locale identifiers, ordered according to user preference.  If none of the user-preferred localizations are available, this method returns one of the values in `localizationsArray`.

## Discussion

This method returns only the locale identifiers for which a bundle would  provide localized content. Typically, this means one of the following:

- A single localization that isn’t region-specific
- A region-specific localization, followed by a corresponding localization that isn’t region-specific, as a fallback

This method doesn’t return all localizations in order of user preference. To get this information, you can call this method repeatedly, each time removing the identifiers returned by the previous call.

## See Also

### Getting localization information

- [localizations](localizations.md) — A list of all the localizations contained in the bundle.
- [preferredLocalizations](preferredlocalizations.md) — An ordered list of preferred localizations contained in the bundle.
- [developmentLocalization](developmentlocalization.md) — The localization for the development language.
- [localizedInfoDictionary](localizedinfodictionary.md) — A dictionary with the keys from the bundle’s localized property list.
- [+ preferredLocalizationsFromArray:](<preferredlocalizations(from_).md>) — Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.
