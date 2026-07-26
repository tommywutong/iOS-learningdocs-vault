---
title: trackID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetsegmenttrackreport/trackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetsegmenttrackreport/trackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetsegmenttrackreport/trackid.json'
content_hash: 'sha256:3bb89f773f7d3943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetSegmentTrackReport](../avassetsegmenttrackreport.md)

# trackID

<sub>Instance Property</sub>

A persistent unique identifier for a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var trackID: CMPersistentTrackID { get }
```

## See Also

### Inspecting a report

- [mediaType](mediatype.md) — The type of media a track contains.
- [duration](duration.md) — The duration of a track.
- [earliestPresentationTimeStamp](earliestpresentationtimestamp.md) — The earliest presentation timestamp (PTS) for this track.
- [firstVideoSampleInformation](firstvideosampleinformation.md) — Information about the first video sample in a track.
- [AVAssetSegmentReportSampleInformation](../avassetsegmentreportsampleinformation.md) — An object that provides information about sample data in a track.
