---
title: AVMetadataExtraAttributeKey
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataextraattributekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataextraattributekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataextraattributekey.json'
content_hash: 'sha256:2128b77da58b33c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataExtraAttributeKey

<sub>Structure</sub>

A structure that defines keys for extra metadata attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVMetadataExtraAttributeKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Extra attribute keys

- [AVMetadataExtraAttributeValueURIKey](avmetadataextraattributekey/valueuri.md) — A key that identifies a resource to use as the item’s value.
- [AVMetadataExtraAttributeBaseURIKey](avmetadataextraattributekey/baseuri.md) — A key that identifies the base URI the item uses to resolve its related URIs.
- [AVMetadataExtraAttributeInfoKey](avmetadataextraattributekey/info.md) — A key that identifies more information about the item.

### Initializers

- [init(_:)](<avmetadataextraattributekey/init(__).md>) — Creates an extra attribute key with a string.
- [init(rawValue:)](<avmetadataextraattributekey/init(rawvalue_).md>) — Creates an extra attribute key with a raw string value.

## See Also

### Metadata

- [Retrieving media metadata](retrieving-media-metadata.md) — Load descriptive metadata for media assets and their tracks.
- [AVMetadataItem](avmetadataitem.md) — A metadata item for an audiovisual asset or one of its tracks.
- [AVMutableMetadataItem](avmutablemetadataitem.md) — A mutable metadata item for an audiovisual asset or for one of its tracks.
- [AVMetadataIdentifier](avmetadataidentifier.md) — A structure that defines identifiers for metadata formats.
- [AVMetadataKey](avmetadatakey.md) — A structure that defines a metadata key.
- [AVMetadataKeySpace](avmetadatakeyspace.md) — A structure that defines a metadata key space.
- [AVMetadataFormat](avmetadataformat.md) — A structure that defines metadata formats.
- [AVMetadataItemFilter](avmetadataitemfilter.md) — An object that filters selected information from a metadata item.
