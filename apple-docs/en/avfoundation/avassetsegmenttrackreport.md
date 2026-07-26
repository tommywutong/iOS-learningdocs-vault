---
title: AVAssetSegmentTrackReport
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetsegmenttrackreport
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetsegmenttrackreport.json'
content_hash: 'sha256:76a172b7ca495c59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetSegmentTrackReport

<sub>Class</sub>

An object that provides information on a track in segment data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetSegmentTrackReport
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting a report

- [trackID](avassetsegmenttrackreport/trackid.md) — A persistent unique identifier for a track.
- [mediaType](avassetsegmenttrackreport/mediatype.md) — The type of media a track contains.
- [duration](avassetsegmenttrackreport/duration.md) — The duration of a track.
- [earliestPresentationTimeStamp](avassetsegmenttrackreport/earliestpresentationtimestamp.md) — The earliest presentation timestamp (PTS) for this track.
- [firstVideoSampleInformation](avassetsegmenttrackreport/firstvideosampleinformation.md) — Information about the first video sample in a track.
- [AVAssetSegmentReportSampleInformation](avassetsegmentreportsampleinformation.md) — An object that provides information about sample data in a track.

## See Also

### Inspecting a report

- [segmentType](avassetsegmentreport/segmenttype.md) — The type of segment data.
- [AVAssetSegmentType](avassetsegmenttype.md) — Constants that define the type of a segment.
- [trackReports](avassetsegmentreport/trackreports.md) — The reports for the segment’s track data.
