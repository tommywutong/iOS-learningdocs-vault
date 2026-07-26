---
title: earliestPresentationTimeStamp
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetsegmenttrackreport/earliestpresentationtimestamp
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport/earliestpresentationtimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetsegmenttrackreport/earliestpresentationtimestamp.json'
content_hash: 'sha256:fefb2290cb6cb005'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetSegmentTrackReport](../avassetsegmenttrackreport.md)

# earliestPresentationTimeStamp

<sub>Instance Property</sub>

The earliest presentation timestamp (PTS) for this track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var earliestPresentationTimeStamp: CMTime { get }
```

## Discussion

The value is [invalid](../../coremedia/cmtime/invalid.md) if there’s no information available.

## See Also

### Inspecting a report

- [trackID](trackid.md) — A persistent unique identifier for a track.
- [mediaType](mediatype.md) — The type of media a track contains.
- [duration](duration.md) — The duration of a track.
- [firstVideoSampleInformation](firstvideosampleinformation.md) — Information about the first video sample in a track.
- [AVAssetSegmentReportSampleInformation](../avassetsegmentreportsampleinformation.md) — An object that provides information about sample data in a track.
