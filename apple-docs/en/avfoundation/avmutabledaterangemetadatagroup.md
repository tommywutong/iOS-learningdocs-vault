---
title: AVMutableDateRangeMetadataGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutabledaterangemetadatagroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutabledaterangemetadatagroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutabledaterangemetadatagroup.json'
content_hash: 'sha256:1e83f2d362c9c1f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableDateRangeMetadataGroup

<sub>Class</sub>

A mutable collection of metadata items that are valid for use within a specific range of dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMutableDateRangeMetadataGroup
```

## Relationships

- **Inherits From**: [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the metadata

- [items](avmutabledaterangemetadatagroup/items.md) — An array of associated metadata items.

### Configuring the date range

- [startDate](avmutabledaterangemetadatagroup/startdate.md) — The start date for the metadata date range group.
- [endDate](avmutabledaterangemetadatagroup/enddate.md) — The end date for the metadata date range group.

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
