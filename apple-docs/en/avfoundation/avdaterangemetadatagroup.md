---
title: AVDateRangeMetadataGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdaterangemetadatagroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdaterangemetadatagroup.json'
content_hash: 'sha256:d1081572b9ada9af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDateRangeMetadataGroup

<sub>Class</sub>

A collection of metadata items that are valid for use within a specific date range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVDateRangeMetadataGroup
```

## Relationships

- **Inherits From**: [AVMetadataGroup](avmetadatagroup.md)

- **Inherited By**: [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a date range group

- [- initWithItems:startDate:endDate:](<avdaterangemetadatagroup/init(items_start_end_).md>) — Initializes an instance of `AVDateRangeMetadataGroup` with a collection of metadata items.

### Accessing the metadata

- [items](avdaterangemetadatagroup/items.md) — An array of associated metadata items.

### Accessing the date range

- [startDate](avdaterangemetadatagroup/startdate.md) — The start date for the metadata date range group.
- [endDate](avdaterangemetadatagroup/enddate.md) — The end date for the metadata date range group.

### Initializers

- [init(items:startDate:endDate:)](<avdaterangemetadatagroup/init(items_startdate_enddate_).md>)

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — A collection of metadata items that are valid for use during a specific time range.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
