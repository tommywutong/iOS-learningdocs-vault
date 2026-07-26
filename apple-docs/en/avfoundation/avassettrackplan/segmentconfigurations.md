---
title: segmentConfigurations
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassettrackplan/segmentconfigurations
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackplan/segmentconfigurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackplan/segmentconfigurations.json'
content_hash: 'sha256:612b8c388ed18da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackPlan](../avassettrackplan.md)

# segmentConfigurations

<sub>Instance Property</sub>

Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var segmentConfigurations: [AVPlannedSegmentConfiguration] { get }
```

## See Also

### Inspecting the track plan

- [mediaType](mediatype.md) — The media type of this track. _(beta)_
- [assemblyTrackID](assemblytrackid.md) — This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition. _(beta)_
