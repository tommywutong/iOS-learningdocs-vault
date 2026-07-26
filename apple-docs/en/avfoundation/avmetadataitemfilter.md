---
title: AVMetadataItemFilter
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataitemfilter
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitemfilter.json'
content_hash: 'sha256:9dc9d9cc32862fd6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataItemFilter

<sub>Class</sub>

An object that filters selected information from a metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetadataItemFilter
```

## Overview

Filter instances are opaque, unmodifiable objects, that you create with the [+ metadataItemFilterForSharing](<avmetadataitemfilter/forsharing().md>) class method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a metadata item filter

- [+ metadataItemFilterForSharing](<avmetadataitemfilter/forsharing().md>) — Returns a metadata filter to use for sharing assets.

## See Also

### Metadata

- [Retrieving media metadata](retrieving-media-metadata.md) — Load descriptive metadata for media assets and their tracks.
- [AVMetadataItem](avmetadataitem.md) — A metadata item for an audiovisual asset or one of its tracks.
- [AVMutableMetadataItem](avmutablemetadataitem.md) — A mutable metadata item for an audiovisual asset or for one of its tracks.
- [AVMetadataIdentifier](avmetadataidentifier.md) — A structure that defines identifiers for metadata formats.
- [AVMetadataKey](avmetadatakey.md) — A structure that defines a metadata key.
- [AVMetadataKeySpace](avmetadatakeyspace.md) — A structure that defines a metadata key space.
- [AVMetadataExtraAttributeKey](avmetadataextraattributekey.md) — A structure that defines keys for extra metadata attributes.
- [AVMetadataFormat](avmetadataformat.md) — A structure that defines metadata formats.
