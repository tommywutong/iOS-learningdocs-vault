---
title: 'CFBundleCopyLocalizationsForURL(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecopylocalizationsforurl(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizationsforurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecopylocalizationsforurl%28_%3A%29.json'
content_hash: 'sha256:79f6ca133568922d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCopyLocalizationsForURL(_:)

<sub>Function</sub>

Returns an array containing the localizations for a bundle or executable at a particular location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCopyLocalizationsForURL(_ url: CFURL!) -> CFArray!
```

## Parameters

- `url` — The location of a bundle’s localizations.

## Return Value

An array containing the localizations available at `url`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

For a directory URL, this is equivalent to calling the [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) function on the corresponding bundle. For a plain file URL representing an unbundled application, this will attempt to determine its localizations using the [kCFBundleLocalizationsKey](kcfbundlelocalizationskey.md) and [kCFBundleDevelopmentRegionKey](kcfbundledevelopmentregionkey.md) keys in the dictionary returned by [CFBundleCopyInfoDictionaryForURL](<cfbundlecopyinfodictionaryforurl(__).md>), or a `vers` resource if those are not present.

## See Also

### Managing Localizations

- [CFBundleCopyBundleLocalizations](<cfbundlecopybundlelocalizations(__).md>) — Returns an array containing a bundle’s localizations.
- [CFBundleCopyLocalizedString](<cfbundlecopylocalizedstring(________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleCopyLocalizationsForPreferences](<cfbundlecopylocalizationsforpreferences(____).md>) — Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [CFBundleCopyPreferredLocalizationsFromArray](<cfbundlecopypreferredlocalizationsfromarray(__).md>) — Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
