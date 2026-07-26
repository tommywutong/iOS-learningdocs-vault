---
title: kCFBundleNameKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfbundlenamekey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfbundlenamekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfbundlenamekey.json'
content_hash: 'sha256:ee2c813c0ef361b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFBundleNameKey

<sub>Global Variable</sub>

The human-readable name of the bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFBundleNameKey: CFString!
```

## Discussion

This key is often found in the `InfoPlist.strings` since it is usually localized.

## See Also

### Constants

- [kCFBundleInfoDictionaryVersionKey](kcfbundleinfodictionaryversionkey.md) — The version of the information property list format.
- [kCFBundleExecutableKey](kcfbundleexecutablekey.md) — The name of the executable in this bundle (if any).
- [kCFBundleIdentifierKey](kcfbundleidentifierkey.md) — The bundle identifier.
- [kCFBundleVersionKey](kcfbundleversionkey.md) — The version number of the bundle.
- [kCFBundleDevelopmentRegionKey](kcfbundledevelopmentregionkey.md) — The name of the development language of the bundle.
- [kCFBundleLocalizationsKey](kcfbundlelocalizationskey.md) — Allows an unbundled application that handles localization itself to specify which localizations it has available.
