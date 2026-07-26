---
title: 'CFBundleCopyLocalizationsForPreferences(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopylocalizationsforpreferences(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizationsforpreferences(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopylocalizationsforpreferences%28_%3A_%3A%29.json'
content_hash: 'sha256:9603743d6d0538c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyLocalizationsForPreferences(_:_:)

<sub>Function</sub>

Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyLocalizationsForPreferences(_ locArray: CFArray!, _ prefArray: CFArray!) -> CFArray!
```

## Parameters

- `locArray` — An array of possible localizations to search.

- `prefArray` — An array of preferred localizations. If `NULL`, the user’s actual preferred localizations will be used.

## Return Value

An array containing the localizations that CFBundle would use. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This is not the same as [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>), because that function takes the current application context into account. To determine the localizations that another application would use, apply this function to the result of [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>).

## See Also

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) — Returns an array containing the localizations for a bundle or executable at a particular location.
- [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>) — Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
