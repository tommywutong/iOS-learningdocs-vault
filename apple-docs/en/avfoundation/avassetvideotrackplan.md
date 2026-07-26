---
title: AVAssetVideoTrackPlan
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetvideotrackplan
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvideotrackplan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvideotrackplan.json'
content_hash: 'sha256:e7ec3bb47e73935a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetVideoTrackPlan

<sub>Class</sub>

AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetVideoTrackPlan
```

## Overview

Call AVAssetWritingPlanner’s “planTrack:withSegmentsGeneratedBy:” method to add an AVAssetTrackPlan to the planner’s plan to include it in the incremental writing session. Use this class instead of the base class AVAssetTrackPlan if you are setting up AVAssetWriter with video compression. This configuration hints to the planner that it must coordinate segment boundaries transitions between segments. This is abstracted from the client via using either the resumableAssetWriterInputWithMediaType or createResumableCompressionSessionWithAllocator helper functions within the AVPlannedVideoSegmentWritingRequest.

## Relationships

- **Inherits From**: [AVAssetTrackPlan](avassettrackplan.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a video track plan

- [init(videoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:)](<avassetvideotrackplan/init(videocodectype_encoderspecification_mediatype_segmentconfigurations_assemblytrackid_).md>) — Creates an instance of AVAssetVideoTrackPlan.

### Inspecting the video track plan

- [videoCodecType](avassetvideotrackplan/videocodectype.md) — Video codec type of this track _(beta)_

## See Also

### Planned export

- [AVAssetWritingPlanner](avassetwritingplanner.md) — AVAssetWritingPlanner orchestrates incremental writing of media files. _(beta)_
- [AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md) — AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session. _(beta)_
- [AVAssetTrackPlan](avassettrackplan.md) — AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session. _(beta)_
- [AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md) — AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type. _(beta)_
- [AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md) — AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner. _(beta)_
- [AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md) — AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment. _(beta)_
- [AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md) — AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression. _(beta)_
