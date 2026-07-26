---
title: kCFBundleDevelopmentRegionKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfbundledevelopmentregionkey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfbundledevelopmentregionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfbundledevelopmentregionkey.json'
content_hash: 'sha256:a681bfd6e9e345f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFBundleDevelopmentRegionKey

<sub>Global Variable</sub>

The name of the development language of the bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFBundleDevelopmentRegionKey: CFString!
```

## Discussion

When CFBundle looks for resources, the fallback is to look in the lproj whose name is given by the `kCFBundleDevelopmentRegionKey` in the `Info.plist` file. You must, therefore, ensure that a bundle contains an lproj with that exact name containing a copy of every localized resource, otherwise CFBundle cannot guarantee the fallback mechanism will work.

## See Also

### Constants

- [kCFBundleInfoDictionaryVersionKey](kcfbundleinfodictionaryversionkey.md) — The version of the information property list format.
- [kCFBundleExecutableKey](kcfbundleexecutablekey.md) — The name of the executable in this bundle (if any).
- [kCFBundleIdentifierKey](kcfbundleidentifierkey.md) — The bundle identifier.
- [kCFBundleVersionKey](kcfbundleversionkey.md) — The version number of the bundle.
- [kCFBundleNameKey](kcfbundlenamekey.md) — The human-readable name of the bundle.
- [kCFBundleLocalizationsKey](kcfbundlelocalizationskey.md) — Allows an unbundled application that handles localization itself to specify which localizations it has available.
