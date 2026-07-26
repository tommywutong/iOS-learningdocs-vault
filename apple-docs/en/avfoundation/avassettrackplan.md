---
title: AVAssetTrackPlan
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassettrackplan
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackplan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackplan.json'
content_hash: 'sha256:d3c0bd11f9afd599'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetTrackPlan

<sub>Class</sub>

AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetTrackPlan
```

## Overview

Call AVAssetWritingPlanner’s “planTrack:withSegmentsGeneratedBy:” method to add an AVAssetTrackPlan to the planner to include it in the incremental writing session.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVAssetVideoTrackPlan](avassetvideotrackplan.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a track plan

- [- initWithMediaType:segmentConfigurations:assemblyTrackID:](<avassettrackplan/init(mediatype_segmentconfigurations_assemblytrackid_).md>) — Returns an instance of AVAssetTrackPlan _(beta)_

### Inspecting the track plan

- [mediaType](avassettrackplan/mediatype.md) — The media type of this track. _(beta)_
- [segmentConfigurations](avassettrackplan/segmentconfigurations.md) — Array of AVPlannedSegmentConfigurations, each element specifying the configuration of a planned segment, ordered in output PTS order. _(beta)_
- [assemblyTrackID](avassettrackplan/assemblytrackid.md) — This is the track ID of this track when it is included in the assemblyComposition the planner passes to the completion handler to assemble all planned segments of all tracks into a single AVComposition. _(beta)_

## See Also

### Planned export

- [AVAssetWritingPlanner](avassetwritingplanner.md) — AVAssetWritingPlanner orchestrates incremental writing of media files. _(beta)_
- [AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md) — AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session. _(beta)_
- [AVAssetVideoTrackPlan](avassetvideotrackplan.md) — AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session. _(beta)_
- [AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md) — AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type. _(beta)_
- [AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md) — AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner. _(beta)_
- [AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md) — AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment. _(beta)_
- [AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md) — AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression. _(beta)_
