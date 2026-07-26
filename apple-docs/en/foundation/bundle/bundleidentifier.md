---
title: bundleIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/bundleidentifier
source_url: 'https://developer.apple.com/documentation/foundation/bundle/bundleidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/bundleidentifier.json'
content_hash: 'sha256:7ba3d5d9550c06ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# bundleIdentifier

<sub>Instance Property</sub>

The receiver’s bundle identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bundleIdentifier: String? { get }
```

## Discussion

The bundle identifier is defined by the `CFBundleIdentifier` key in the bundle’s information property list.

## See Also

### Getting bundle information

- [bundleURL](bundleurl.md) — The full URL of the receiver’s bundle directory.
- [bundlePath](bundlepath.md) — The full pathname of the receiver’s bundle directory.
- [infoDictionary](infodictionary.md) — A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
- [- objectForInfoDictionaryKey:](<object(forinfodictionarykey_).md>) — Returns the value associated with the specified key in the receiver’s information property list.
