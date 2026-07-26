---
title: 'key(forIdentifier:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/key(foridentifier:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/key(foridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/key%28foridentifier%3A%29.json'
content_hash: 'sha256:67e1b53d668a5db8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# key(forIdentifier:)

<sub>Type Method</sub>

Returns a metadata key for the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func key(forIdentifier identifier: AVMetadataIdentifier) -> Any?
```

## Parameters

- `identifier` — The metadata identifier.

## Return Value

A metadata key.

## See Also

### Translating metadata items

- [+ identifierForKey:keySpace:](<identifier(forkey_keyspace_).md>) — Returns a metadata identifier for the specified key and key space.
- [+ keySpaceForIdentifier:](<keyspace(foridentifier_).md>) — Returns a metadata key space for the specified identifier.
