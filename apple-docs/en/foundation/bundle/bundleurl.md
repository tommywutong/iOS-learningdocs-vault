---
title: bundleURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/bundleurl
source_url: 'https://developer.apple.com/documentation/foundation/bundle/bundleurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/bundleurl.json'
content_hash: 'sha256:208a3f441c1b8823'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# bundleURL

<sub>Instance Property</sub>

The full URL of the receiver’s bundle directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bundleURL: URL { get }
```

## See Also

### Getting bundle information

- [bundlePath](bundlepath.md) — The full pathname of the receiver’s bundle directory.
- [bundleIdentifier](bundleidentifier.md) — The receiver’s bundle identifier.
- [infoDictionary](infodictionary.md) — A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
- [- objectForInfoDictionaryKey:](<object(forinfodictionarykey_).md>) — Returns the value associated with the specified key in the receiver’s information property list.
