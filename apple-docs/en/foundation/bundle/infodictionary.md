---
title: infoDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/infodictionary
source_url: 'https://developer.apple.com/documentation/foundation/bundle/infodictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/infodictionary.json'
content_hash: 'sha256:06fe8ea999e058b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# infoDictionary

<sub>Instance Property</sub>

A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var infoDictionary: [String : Any]? { get }
```

## Discussion

If the bundle does not contain an `Info.plist` file, this dictionary contains only private keys that are used internally by the [Bundle](../bundle.md) class. The [Bundle](../bundle.md) class may add extra keys to this dictionary for its own use. Common keys for accessing the values of the dictionary are `CFBundleIdentifier`, `NSMainNibFile`, and `NSPrincipalClass`.

## See Also

### Related Documentation

- [principalClass](principalclass.md) — The bundle’s principal class.

### Getting bundle information

- [bundleURL](bundleurl.md) — The full URL of the receiver’s bundle directory.
- [bundlePath](bundlepath.md) — The full pathname of the receiver’s bundle directory.
- [bundleIdentifier](bundleidentifier.md) — The receiver’s bundle identifier.
- [- objectForInfoDictionaryKey:](<object(forinfodictionarykey_).md>) — Returns the value associated with the specified key in the receiver’s information property list.
