---
title: CFCopyLocalizedStringFromTable
framework: Core Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcopylocalizedstringfromtable
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcopylocalizedstringfromtable.json'
content_hash: 'sha256:deab6404f77f6f49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCopyLocalizedStringFromTable

<sub>Macro</sub>

Searches the specified strings file for the string associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define CFCopyLocalizedStringFromTable(key, tbl, comment)
```

## Parameters

- `key` — The development language version of the string. This string is used as the search key to locate the localized version of the string.

- `tbl` — The name of the strings file to search. The name should not include the `strings` filename extension. The case of the string must match that of the file name, even on file systems (such as HFS+) that are not case sensitive with regards to file names

- `comment` — A comment to provide the translators with contextual information necessary for proper translation.

## Return Value

The localized version of the requested string, or `key` if no value corresponding to `key` is found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This is a macro variant of [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) for use with the `genstrings` tool.

## See Also

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) — Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) — Returns an array containing the localizations for a bundle or executable at a particular location.
- [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>) — Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
- [CFCopyLocalizedString](cfcopylocalizedstring.md) — Searches the default strings file `Localizable.strings` for the string associated with the specified key.
- [CFCopyLocalizedStringFromTableInBundle](cfcopylocalizedstringfromtableinbundle.md) — Returns a localized version of the specified string.
- [CFCopyLocalizedStringWithDefaultValue](cfcopylocalizedstringwithdefaultvalue.md) — Returns a localized version of a localization string.
