---
title: commonKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitem/commonkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/commonkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/commonkey.json'
content_hash: 'sha256:d7176ea9667aa90c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# commonKey

<sub>Instance Property</sub>

The common key of the metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var commonKey: AVMetadataKey? { get }
```

## Discussion

This value contains the key that most closely corresponds to the [key](key.md) property, but that belongs to the common key space. You can use this key to locate metadata items irrespective of the underlying media format.

If the value of the [keySpace](keyspace.md) property is [AVMetadataKeySpaceCommon](../avmetadatakeyspace/common.md), this property value contains the same key as the [key](key.md) property.

## See Also

### Accessing keys and key spaces

- [key](key.md) — The key of the metadata item.
- [keySpace](keyspace.md) — The key space for the metadata item’s key.
