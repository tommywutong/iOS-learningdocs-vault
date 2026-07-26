---
title: 'identifier(forKey:keySpace:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/identifier(forkey:keyspace:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/identifier(forkey:keyspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/identifier%28forkey%3Akeyspace%3A%29.json'
content_hash: 'sha256:ed12ae69a2d7de25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# identifier(forKey:keySpace:)

<sub>Type Method</sub>

Returns a metadata identifier for the specified key and key space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func identifier(forKey key: Any, keySpace: AVMetadataKeySpace) -> AVMetadataIdentifier?
```

## Parameters

- `key` — A key to return an identifier for.

- `keySpace` — A key space to return an identifier for.

## Return Value

A metadata identifier, or `nil` if no equivalent identifier exists.

## See Also

### Translating metadata items

- [+ keyForIdentifier:](<key(foridentifier_).md>) — Returns a metadata key for the specified identifier.
- [+ keySpaceForIdentifier:](<keyspace(foridentifier_).md>) — Returns a metadata key space for the specified identifier.
