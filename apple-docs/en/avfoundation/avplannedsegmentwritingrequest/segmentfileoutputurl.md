---
title: segmentFileOutputURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplannedsegmentwritingrequest/segmentfileoutputurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/segmentfileoutputurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest/segmentfileoutputurl.json'
content_hash: 'sha256:13a1b3556656e51c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentWritingRequest](../avplannedsegmentwritingrequest.md)

# segmentFileOutputURL

<sub>Instance Property</sub>

The URL of the file where this incremental segment should be written to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var segmentFileOutputURL: URL { get }
```

## Discussion

AVAssetWritingPlanner will request each incremental segment to be written to a different file. If the file already exists from a previous session, the client should delete it to allow the subsequent asset writer session to succeed.

## See Also

### Inspecting the request

- [timeRange](timerange.md) — The PTS range for this segment. _(beta)_
- [progress](progress.md) — The current progress for the track identified by assemblyTrackID. _(beta)_
- [assemblyTrackID](assemblytrackid.md) — The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler. _(beta)_
