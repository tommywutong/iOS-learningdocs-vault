---
title: CFCopyLocalizedStringWithDefaultValue
framework: Core Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcopylocalizedstringwithdefaultvalue
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringwithdefaultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcopylocalizedstringwithdefaultvalue.json'
content_hash: 'sha256:a7514253c5c7667b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCopyLocalizedStringWithDefaultValue

<sub>Macro</sub>

Returns a localized version of a localization string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define CFCopyLocalizedStringWithDefaultValue(key, tbl, bundle, value, comment)
```

## Parameters

- `key` — The development language version of the string. This string is used as the search key to locate the localized version of the string.

- `tbl` — The name of the strings file to search. The name should not include the `strings` filename extension.

- `bundle` — The bundle to examine.

- `value` — The default value for the requested localization string.

- `comment` — A comment to provide the translators with contextual information necessary for proper translation.

## Return Value

The localized version of the requested string. If no value corresponding to `key` is found, returns `value`, unless `value` is `NULL` or an empty string, in which case `key` is returned instead. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

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
- [CFCopyLocalizedStringFromTable](cfcopylocalizedstringfromtable.md) — Searches the specified strings file for the string associated with the specified key.
- [CFCopyLocalizedStringFromTableInBundle](cfcopylocalizedstringfromtableinbundle.md) — Returns a localized version of the specified string.
