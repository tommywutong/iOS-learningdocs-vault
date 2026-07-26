---
title: key
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitem/key
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/key'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/key.json'
content_hash: 'sha256:99e773f6f4665c9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# key

<sub>Instance Property</sub>

The key of the metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var key: (any NSCopying & NSObjectProtocol)? { get }
```

## Discussion

The key property contains the true key used to identify the contents of the metadata item. This value is specific to the key space of the metadata item.

## See Also

### Accessing keys and key spaces

- [commonKey](commonkey.md) — The common key of the metadata item.
- [keySpace](keyspace.md) — The key space for the metadata item’s key.
