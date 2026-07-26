---
title: AVMutableTimedMetadataGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutabletimedmetadatagroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutabletimedmetadatagroup.json'
content_hash: 'sha256:8146846d32910c7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableTimedMetadataGroup

<sub>Class</sub>

A mutable collection of metadata items that are valid for use during a specific time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMutableTimedMetadataGroup
```

## Relationships

- **Inherits From**: [AVTimedMetadataGroup](avtimedmetadatagroup.md)

- **Conforms To**: [SupportedPayload](avassetreaderoutput/supportedpayload.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the group

- [items](avmutabletimedmetadatagroup/items.md) — An array of metadata items in the timed metadata group.
- [timeRange](avmutabletimedmetadatagroup/timerange.md) — The time range of the timed metadata.

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
