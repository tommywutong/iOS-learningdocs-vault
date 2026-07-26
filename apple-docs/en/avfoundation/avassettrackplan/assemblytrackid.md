---
title: assemblyTrackID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassettrackplan/assemblytrackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackplan/assemblytrackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackplan/assemblytrackid.json'
content_hash: 'sha256:9bed3c982c74d957'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackPlan](../avassettrackplan.md)

# assemblyTrackID

<sub>Instance Property</sub>

This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var assemblyTrackID: CMPersistentTrackID { get }
```

## Discussion

The assemblyTrackID serves the purpose as a unique identifier of the track in the incremental writing session. This does not necessarily match the trackID of the source asset. The client is responsible for remembering the relationship between assemblyTrackID and the trackID in the source asset.

## See Also

### Inspecting the track plan

- [mediaType](mediatype.md) — The media type of this track. _(beta)_
- [segmentConfigurations](segmentconfigurations.md) — Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order. _(beta)_
