---
title: developmentLocalization
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/developmentlocalization
source_url: 'https://developer.apple.com/documentation/foundation/bundle/developmentlocalization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/developmentlocalization.json'
content_hash: 'sha256:4cecac2e90e7ca7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# developmentLocalization

<sub>Instance Property</sub>

The localization for the development language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var developmentLocalization: String? { get }
```

## Discussion

This property corresponds to the value in the `CFBundleDevelopmentRegion` key of the bundle’s property list (`Info.plist`).

## See Also

### Getting localization information

- [localizations](localizations.md) — A list of all the localizations contained in the bundle.
- [preferredLocalizations](preferredlocalizations.md) — An ordered list of preferred localizations contained in the bundle.
- [localizedInfoDictionary](localizedinfodictionary.md) — A dictionary with the keys from the bundle’s localized property list.
- [+ preferredLocalizationsFromArray:](<preferredlocalizations(from_).md>) — Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.
- [+ preferredLocalizationsFromArray:forPreferences:](<preferredlocalizations(from_forpreferences_).md>) — Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.
