---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplannedsegmentwritingrequest/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest/timerange.json'
content_hash: 'sha256:c1286dd7e2b3153c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentWritingRequest](../avplannedsegmentwritingrequest.md)

# timeRange

<sub>Instance Property</sub>

The PTS range for this segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## Discussion

The client is responsible for delivering the appropriate sample corresponding to timeRange.start if we are resuming a previous session that has already made incremental progress for this track.

## See Also

### Inspecting the request

- [segmentFileOutputURL](segmentfileoutputurl.md) — The URL of the file where this incremental segment should be written to. _(beta)_
- [progress](progress.md) — The current progress for the track identified by assemblyTrackID. _(beta)_
- [assemblyTrackID](assemblytrackid.md) — The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler. _(beta)_
