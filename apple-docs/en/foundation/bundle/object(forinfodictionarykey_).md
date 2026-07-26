---
title: 'object(forInfoDictionaryKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/object(forinfodictionarykey:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/object(forinfodictionarykey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/object%28forinfodictionarykey%3A%29.json'
content_hash: 'sha256:21124c1333e8f1b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# object(forInfoDictionaryKey:)

<sub>Instance Method</sub>

Returns the value associated with the specified key in the receiver’s information property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(forInfoDictionaryKey key: String) -> Any?
```

## Parameters

- `key` — A key in the receiver’s property list.

## Return Value

The value associated with `key` in the receiver’s property list (`Info.plist`). The localized value of a key is returned when one is available.

## Discussion

Use of this method is preferred over other access methods because it returns the localized value of a key when one is available.

## See Also

### Getting bundle information

- [bundleURL](bundleurl.md) — The full URL of the receiver’s bundle directory.
- [bundlePath](bundlepath.md) — The full pathname of the receiver’s bundle directory.
- [bundleIdentifier](bundleidentifier.md) — The receiver’s bundle identifier.
- [infoDictionary](infodictionary.md) — A dictionary, constructed from the bundle’s `Info.plist` file, that contains information about the receiver.
