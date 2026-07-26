---
title: AVMetadataKeySpace
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatakeyspace
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatakeyspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatakeyspace.json'
content_hash: 'sha256:7a5ac7b9728bfa00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataKeySpace

<sub>Structure</sub>

A structure that defines a metadata key space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVMetadataKeySpace
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Common key space

- [AVMetadataKeySpaceCommon](avmetadatakeyspace/common.md) — The common key space.

### Format-specific key spaces

- [AVMetadataKeySpaceAudioFile](avmetadatakeyspace/audiofile.md) — The AudioToolbox audio file key space.
- [AVMetadataKeySpaceHLSDateRange](avmetadatakeyspace/hlsdaterange.md) — The HTTP Live Streaming key space.
- [AVMetadataKeySpaceiTunes](avmetadatakeyspace/itunes.md) — The iTunes key space.
- [AVMetadataKeySpaceIcy](avmetadatakeyspace/icy.md) — The Icecast/ShoutCAST streaming key space.
- [AVMetadataKeySpaceID3](avmetadatakeyspace/id3.md) — The ID3 key space.
- [AVMetadataKeySpaceISOUserData](avmetadatakeyspace/isouserdata.md) — The ISO key space.
- [AVMetadataKeySpaceQuickTimeMetadata](avmetadatakeyspace/quicktimemetadata.md) — The QuickTime metadata key space.
- [AVMetadataKeySpaceQuickTimeUserData](avmetadatakeyspace/quicktimeuserdata.md) — The QuickTime user data key space.

### Initializers

- [init(_:)](<avmetadatakeyspace/init(__).md>) — Creates a key space with a string.
- [init(rawValue:)](<avmetadatakeyspace/init(rawvalue_).md>) — Creates a key space with a raw string value.

## See Also

### Metadata

- [Retrieving media metadata](retrieving-media-metadata.md) — Load descriptive metadata for media assets and their tracks.
- [AVMetadataItem](avmetadataitem.md) — A metadata item for an audiovisual asset or one of its tracks.
- [AVMutableMetadataItem](avmutablemetadataitem.md) — A mutable metadata item for an audiovisual asset or for one of its tracks.
- [AVMetadataIdentifier](avmetadataidentifier.md) — A structure that defines identifiers for metadata formats.
- [AVMetadataKey](avmetadatakey.md) — A structure that defines a metadata key.
- [AVMetadataExtraAttributeKey](avmetadataextraattributekey.md) — A structure that defines keys for extra metadata attributes.
- [AVMetadataFormat](avmetadataformat.md) — A structure that defines metadata formats.
- [AVMetadataItemFilter](avmetadataitemfilter.md) — An object that filters selected information from a metadata item.
