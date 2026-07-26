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
doc_path: /documentation/avfoundation/avplannedsegmentwritingrequest/assemblytrackid
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/assemblytrackid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest/assemblytrackid.json'
content_hash: 'sha256:d0f8f60eae0d0c5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentWritingRequest](../avplannedsegmentwritingrequest.md)

# assemblyTrackID

<sub>Instance Property</sub>

The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var assemblyTrackID: CMPersistentTrackID { get }
```

## See Also

### Inspecting the request

- [timeRange](timerange.md) — The PTS range for this segment. _(beta)_
- [segmentFileOutputURL](segmentfileoutputurl.md) — The URL of the file where this incremental segment should be written to. _(beta)_
- [progress](progress.md) — The current progress for the track identified by assemblyTrackID. _(beta)_
