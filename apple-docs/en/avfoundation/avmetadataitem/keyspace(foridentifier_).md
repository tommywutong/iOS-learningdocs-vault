---
title: 'keySpace(forIdentifier:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/keyspace(foridentifier:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/keyspace(foridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/keyspace%28foridentifier%3A%29.json'
content_hash: 'sha256:40ca87e6ab123805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# keySpace(forIdentifier:)

<sub>Type Method</sub>

Returns a metadata key space for the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func keySpace(forIdentifier identifier: AVMetadataIdentifier) -> AVMetadataKeySpace?
```

## Parameters

- `identifier` — The metadata identifier.

## Return Value

A metadata key space.

## See Also

### Translating metadata items

- [+ identifierForKey:keySpace:](<identifier(forkey_keyspace_).md>) — Returns a metadata identifier for the specified key and key space.
- [+ keyForIdentifier:](<key(foridentifier_).md>) — Returns a metadata key for the specified identifier.
