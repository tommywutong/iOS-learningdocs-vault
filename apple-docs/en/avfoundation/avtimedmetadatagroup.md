---
title: AVTimedMetadataGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avtimedmetadatagroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtimedmetadatagroup.json'
content_hash: 'sha256:5e83ac4ff4f8c83e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVTimedMetadataGroup

<sub>Class</sub>

A collection of metadata items that are valid for use during a specific time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVTimedMetadataGroup
```

## Overview

For example, `AVTimedMetadataGroups` are used to represent chapters, optionally containing metadata items for chapter titles and chapter images.

## Relationships

- **Inherits From**: [AVMetadataGroup](avmetadatagroup.md)

- **Inherited By**: [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md)

- **Conforms To**: [SupportedPayload](avassetreaderoutput/supportedpayload.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a timed metadata group

- [init(sampleBuffer:)](<avtimedmetadatagroup/init(samplebuffer_)-6atlv.md>) — Creates a timed metadata group with a sample buffer.
- [- initWithItems:timeRange:](<avtimedmetadatagroup/init(items_timerange_).md>) — Creates a timed metadata group initialized with the given metadata items.
- [- initWithSampleBuffer:](<avtimedmetadatagroup/init(samplebuffer_)-bjuo.md>) _(deprecated)_

### Accessing group attributes

- [items](avtimedmetadatagroup/items.md) — An array of metadata items in the timed metadata group.
- [timeRange](avtimedmetadatagroup/timerange.md) — The time range for the timed metadata.

### Creating a format description

- [- copyFormatDescription](<avtimedmetadatagroup/copyformatdescription().md>) — Creates a format description based on the receiver’s items.

## See Also

### Timed metadata

- [Presenting chapter markers](presenting-chapter-markers.md) — Add chapter markers to enable users to quickly navigate your content.
- [AVMetadataGroup](avmetadatagroup.md) — A collection of metadata items associated with a timeline segment.
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — A mutable collection of metadata items that are valid for use during a specific time range.
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — A collection of metadata items that are valid for use within a specific date range.
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — A mutable collection of metadata items that are valid for use within a specific range of dates.
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — The abstract base for media data collectors.
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — An object used to capture the date range metadata defined for an HTTP Live Streaming asset.
