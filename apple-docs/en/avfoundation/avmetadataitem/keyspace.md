---
title: keySpace
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitem/keyspace
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/keyspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/keyspace.json'
content_hash: 'sha256:535ba72b8a106c46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# keySpace

<sub>Instance Property</sub>

The key space for the metadata item’s key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keySpace: AVMetadataKeySpace? { get }
```

## Discussion

The key space that this property value specifies is typically the default key space for the metadata container that stores the metadata item.

AVFoundation uses key spaces to group related sets of keys. For example, the framework defines different key spaces for common keys, iTunes keys, ID3 keys, and QuickTime keys. Key spaces aid in filtering arrays of metadata items.

## See Also

### Accessing keys and key spaces

- [key](key.md) — The key of the metadata item.
- [commonKey](commonkey.md) — The common key of the metadata item.
