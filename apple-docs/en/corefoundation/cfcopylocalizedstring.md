---
title: CFCopyLocalizedString
framework: Core Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcopylocalizedstring
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcopylocalizedstring.json'
content_hash: 'sha256:76bd489b2e724335'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCopyLocalizedString

<sub>Macro</sub>

Searches the default strings file `Localizable.strings` for the string associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define CFCopyLocalizedString(key, comment)
```

## Parameters

- `key` — The development language version of the string. This string is used as the search key to locate the localized version of the string.

- `comment` — A comment to provide the translators with contextual information necessary for proper translation.

## Return Value

The localized version of the requested string. Returns `key` if no value corresponding to `key` is found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This is a macro variant of [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) for use with the `genstrings` tool.

## See Also

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) — Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) — Returns an array containing the localizations for a bundle or executable at a particular location.
- [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>) — Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
- [CFCopyLocalizedStringFromTable](cfcopylocalizedstringfromtable.md) — Searches the specified strings file for the string associated with the specified key.
- [CFCopyLocalizedStringFromTableInBundle](cfcopylocalizedstringfromtableinbundle.md) — Returns a localized version of the specified string.
- [CFCopyLocalizedStringWithDefaultValue](cfcopylocalizedstringwithdefaultvalue.md) — Returns a localized version of a localization string.
