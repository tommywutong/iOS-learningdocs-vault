---
title: 'CFBundleCopyLocalizedString(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopylocalizedstring(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizedstring(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopylocalizedstring%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:904c957e80a3fb20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyLocalizedString(_:_:_:_:)

<sub>Function</sub>

Returns a localized string from a bundle’s strings file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyLocalizedString(_ bundle: CFBundle!, _ key: CFString!, _ value: CFString!, _ tableName: CFString!) -> CFString!
```

## Parameters

- `bundle` — The bundle to examine.

- `key` — The key for the localized string to retrieve. This key will be used to look up the localized string in the strings file. Typically the key is identical to the value of the localized string in the development language.

- `value` — A default value to return if no value exists for `key`.

- `tableName` — The name of the strings file to search. The name should not include the `strings` filename extension. The case of the string must match that of the file name, even on file systems (such as HFS+) that are not case sensitive with regards to file names

## Return Value

A CFString object that contains the localized string. If no value exists for `key`, returns `value` unless `value` is `NULL` or an empty string, in which case `key` is returned instead. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This is the base function from which the other localized string macros are derived. In general you should not use this function because the `genstrings` development tool only recognizes the macro version of this call when generating strings files. See [CFCopyLocalizedString](cfcopylocalizedstring.md) for details on how to use these macros.

## See Also

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) — Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) — Returns an array containing the localizations for a bundle or executable at a particular location.
- [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>) — Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
