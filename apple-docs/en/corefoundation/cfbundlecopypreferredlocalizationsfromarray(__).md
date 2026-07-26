---
title: 'CFBundleCopyPreferredLocalizationsFromArray(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopypreferredlocalizationsfromarray(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopypreferredlocalizationsfromarray(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopypreferredlocalizationsfromarray%28_%3A%29.json'
content_hash: 'sha256:7f187495fa0f2bf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyPreferredLocalizationsFromArray(_:)

<sub>Function</sub>

Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyPreferredLocalizationsFromArray(_ locArray: CFArray!) -> CFArray!
```

## Parameters

- `locArray` — An array of possible localizations.

## Return Value

A subset of `locArray` that CFBundle would use in the current application context. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You can obtain `locArray` using the [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) function.

## See Also

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) — Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [CFBundleCopyLocalizationsForURL](<cfbundlecopylocalizationsforurl(__).md>) — Returns an array containing the localizations for a bundle or executable at a particular location.
