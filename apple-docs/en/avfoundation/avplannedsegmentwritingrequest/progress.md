---
title: progress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplannedsegmentwritingrequest/progress
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest/progress.json'
content_hash: 'sha256:02c93bcd42afbb9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentWritingRequest](../avplannedsegmentwritingrequest.md)

# progress

<sub>Instance Property</sub>

The current progress for the track identified by assemblyTrackID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progress: Float { get }
```

## Discussion

Returns a float value between 0.0 and 1.0 representing the percentage of duration completed for this track. This value is updated as segments are completed.

## See Also

### Inspecting the request

- [timeRange](timerange.md) — The PTS range for this segment. _(beta)_
- [segmentFileOutputURL](segmentfileoutputurl.md) — The URL of the file where this incremental segment should be written to. _(beta)_
- [assemblyTrackID](assemblytrackid.md) — The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler. _(beta)_
