---
title: 'preferredLocalizations(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/preferredlocalizations(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/preferredlocalizations(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/preferredlocalizations%28from%3A%29.json'
content_hash: 'sha256:e5f364ded0a73fff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# preferredLocalizations(from:)

<sub>Type Method</sub>

Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func preferredLocalizations(from localizationsArray: [String]) -> [String]
```

## Parameters

- `localizationsArray` — An array of `NSString` objects, each of which specifies the language ID for a localization that the bundle supports.

## Return Value

An array of `NSString` objects containing the preferred localizations. These strings are ordered in the array according to the user’s language preferences and are taken from the strings in the `localizationsArray` parameter.

## Discussion

This method does not return all localizations in preference order but only those from which `NSBundle` would get localized content, typically either a single non-region-specific localization or a region-specific localization followed by a corresponding non-region-specific localization as a fallback.

However, clients who want all localizations in preference order can make repeated calls, each time taking the top localizations out of the list of localizations passed in.

## See Also

### Getting localization information

- [localizations](localizations.md) — A list of all the localizations contained in the bundle.
- [preferredLocalizations](preferredlocalizations.md) — An ordered list of preferred localizations contained in the bundle.
- [developmentLocalization](developmentlocalization.md) — The localization for the development language.
- [localizedInfoDictionary](localizedinfodictionary.md) — A dictionary with the keys from the bundle’s localized property list.
- [+ preferredLocalizationsFromArray:forPreferences:](<preferredlocalizations(from_forpreferences_).md>) — Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.
