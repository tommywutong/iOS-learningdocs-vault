---
title: AVAssetSegmentReportSampleInformation
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetsegmentreportsampleinformation
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetsegmentreportsampleinformation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetsegmentreportsampleinformation.json'
content_hash: 'sha256:7cdcacf2869f63b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetSegmentReportSampleInformation

<sub>Class</sub>

An object that provides information about sample data in a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetSegmentReportSampleInformation
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the information

- [presentationTimeStamp](avassetsegmentreportsampleinformation/presentationtimestamp.md) — The presentation timestamp (PTS) of a sample.
- [offset](avassetsegmentreportsampleinformation/offset.md) — The offset of a sample in the segment.
- [length](avassetsegmentreportsampleinformation/length.md) — The length of the sample data.
- [isSyncSample](avassetsegmentreportsampleinformation/issyncsample.md) — A Boolean value that indicates whether the sample is a key frame.

## See Also

### Inspecting a report

- [trackID](avassetsegmenttrackreport/trackid.md) — A persistent unique identifier for a track.
- [mediaType](avassetsegmenttrackreport/mediatype.md) — The type of media a track contains.
- [duration](avassetsegmenttrackreport/duration.md) — The duration of a track.
- [earliestPresentationTimeStamp](avassetsegmenttrackreport/earliestpresentationtimestamp.md) — The earliest presentation timestamp (PTS) for this track.
- [firstVideoSampleInformation](avassetsegmenttrackreport/firstvideosampleinformation.md) — Information about the first video sample in a track.
