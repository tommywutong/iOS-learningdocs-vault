---
title: AVAssetSegmentReport
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetsegmentreport
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetsegmentreport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetsegmentreport.json'
content_hash: 'sha256:7c8e39c1927ea12a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetSegmentReport

<sub>Class</sub>

An object that provides information about segment data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetSegmentReport
```

## Overview

You receive a segment report through the [- assetWriter:didOutputSegmentData:segmentType:segmentReport:](<avassetwriterdelegate/assetwriter(__didoutputsegmentdata_segmenttype_segmentreport_).md>) delegate method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting a report

- [segmentType](avassetsegmentreport/segmenttype.md) — The type of segment data.
- [AVAssetSegmentType](avassetsegmenttype.md) — Constants that define the type of a segment.
- [trackReports](avassetsegmentreport/trackreports.md) — The reports for the segment’s track data.
- [AVAssetSegmentTrackReport](avassetsegmenttrackreport.md) — An object that provides information on a track in segment data.

## See Also

### Responding to segment output

- [- assetWriter:didOutputSegmentData:segmentType:](<avassetwriterdelegate/assetwriter(__didoutputsegmentdata_segmenttype_).md>) — Tells the delegate that the asset writer output segment data.
- [- assetWriter:didOutputSegmentData:segmentType:segmentReport:](<avassetwriterdelegate/assetwriter(__didoutputsegmentdata_segmenttype_segmentreport_).md>) — Tells the delegate that the asset writer output segment data and a report.
