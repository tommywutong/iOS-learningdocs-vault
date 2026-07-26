---
title: AVPlayerItemMediaDataCollector
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmediadatacollector
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmediadatacollector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmediadatacollector.json'
content_hash: 'sha256:a6e42fff95483b3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemMediaDataCollector

<sub>Class</sub>

The abstract base for media data collectors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemMediaDataCollector
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
