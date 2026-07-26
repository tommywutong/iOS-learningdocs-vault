---
title: AVMetadataGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatagroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatagroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatagroup.json'
content_hash: 'sha256:b38e3bbb4a733a61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataGroup

<sub>Class</sub>

A collection of metadata items associated with a timeline segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMetadataGroup
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md), [AVTimedMetadataGroup](avtimedmetadatagroup.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the metadata group

- [items](avmetadatagroup/items.md) — The array of metadata items associated with the metadata group.
- [uniqueID](avmetadatagroup/uniqueid.md) — The unique identifier for the metadata group.
- [classifyingLabel](avmetadatagroup/classifyinglabel.md) — The classifying label associated with the metadata group.

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
