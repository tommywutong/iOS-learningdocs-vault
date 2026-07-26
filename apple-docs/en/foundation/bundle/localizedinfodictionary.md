---
title: localizedInfoDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/localizedinfodictionary
source_url: 'https://developer.apple.com/documentation/foundation/bundle/localizedinfodictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/localizedinfodictionary.json'
content_hash: 'sha256:cc1ef7507664e789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# localizedInfoDictionary

<sub>Instance Property</sub>

A dictionary with the keys from the bundle’s localized property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedInfoDictionary: [String : Any]? { get }
```

## Discussion

This property uses the preferred localization for the current user when determining which resources to include. If the preferred localization is not available, this property chooses the most appropriate localization found in the bundle.

## See Also

### Getting localization information

- [localizations](localizations.md) — A list of all the localizations contained in the bundle.
- [preferredLocalizations](preferredlocalizations.md) — An ordered list of preferred localizations contained in the bundle.
- [developmentLocalization](developmentlocalization.md) — The localization for the development language.
- [+ preferredLocalizationsFromArray:](<preferredlocalizations(from_).md>) — Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.
- [+ preferredLocalizationsFromArray:forPreferences:](<preferredlocalizations(from_forpreferences_).md>) — Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.
