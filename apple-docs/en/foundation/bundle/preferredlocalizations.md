---
title: preferredLocalizations
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/preferredlocalizations
source_url: 'https://developer.apple.com/documentation/foundation/bundle/preferredlocalizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/preferredlocalizations.json'
content_hash: 'sha256:fe982572c7d9de43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# preferredLocalizations

<sub>Instance Property</sub>

An ordered list of preferred localizations contained in the bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredLocalizations: [String] { get }
```

## Discussion

An array of [NSString](../nsstring.md) objects containing language IDs for localizations in the bundle. The strings are ordered according to the user’s language preferences and available localizations.

## See Also

### Getting localization information

- [localizations](localizations.md) — A list of all the localizations contained in the bundle.
- [developmentLocalization](developmentlocalization.md) — The localization for the development language.
- [localizedInfoDictionary](localizedinfodictionary.md) — A dictionary with the keys from the bundle’s localized property list.
- [+ preferredLocalizationsFromArray:](<preferredlocalizations(from_).md>) — Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.
- [+ preferredLocalizationsFromArray:forPreferences:](<preferredlocalizations(from_forpreferences_).md>) — Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.
