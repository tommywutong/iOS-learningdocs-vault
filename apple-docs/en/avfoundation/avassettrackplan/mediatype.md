---
title: mediaType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassettrackplan/mediatype
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackplan/mediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackplan/mediatype.json'
content_hash: 'sha256:e187c76714d65c8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackPlan](../avassettrackplan.md)

# mediaType

<sub>Instance Property</sub>

The media type of this track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mediaType: AVMediaType { get }
```

## See Also

### Inspecting the track plan

- [segmentConfigurations](segmentconfigurations.md) — Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order. _(beta)_
- [assemblyTrackID](assemblytrackid.md) — This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition. _(beta)_
