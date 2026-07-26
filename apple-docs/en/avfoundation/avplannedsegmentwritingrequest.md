---
title: AVPlannedSegmentWritingRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplannedsegmentwritingrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest.json'
content_hash: 'sha256:ae814cadb6fec433'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlannedSegmentWritingRequest

<sub>Class</sub>

AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlannedSegmentWritingRequest
```

## Overview

The client should respond to this request by writing the specified time range of data to a movie file at the specified segmentFileOutputURL, with start PTS zero. The client’s writing work may be completed asynchronously. If it completes successfully, clients must call the `-finish` or `-finishWithClientState` method on the request object. If writing the segment fails, clients must call the `-finishWithError:` method on the request object. If segment writing needs to be stopped before reaching the end of the segment, clients must call `-cancel`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the request

- [timeRange](avplannedsegmentwritingrequest/timerange.md) — The PTS range for this segment. _(beta)_
- [segmentFileOutputURL](avplannedsegmentwritingrequest/segmentfileoutputurl.md) — The URL of the file where this incremental segment should be written to. _(beta)_
- [progress](avplannedsegmentwritingrequest/progress.md) — The current progress for the track identified by assemblyTrackID. _(beta)_
- [assemblyTrackID](avplannedsegmentwritingrequest/assemblytrackid.md) — The trackID identifies which track should be written to this segment file. This is the same track ID in the AVAssetTrackPlan object. This is also the trackID the AVAssetWritingPlanner uses to build the assembled AVComposition before it calls the completion handler. _(beta)_

### Managing client state

- [clientStateToRestore](avplannedsegmentwritingrequest/clientstatetorestore.md) — The client state persisted from the previous segment, if any. Specifically, this is the NSData provided to the previous segment’s finishWithClientState: method. The client is responsible to restore its client state before writing the current segment. For example, clients such as compositors with a temporal element may need some processing history of previous samples in order to generate an output sample at time N. This will be nil for algorithms that are stateless. _(beta)_

## See Also

### Planned export

- [AVAssetWritingPlanner](avassetwritingplanner.md) — AVAssetWritingPlanner orchestrates incremental writing of media files. _(beta)_
- [AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md) — AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session. _(beta)_
- [AVAssetTrackPlan](avassettrackplan.md) — AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session. _(beta)_
- [AVAssetVideoTrackPlan](avassetvideotrackplan.md) — AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session. _(beta)_
- [AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md) — AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type. _(beta)_
- [AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md) — AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner. _(beta)_
- [AVPlannedVideoSegmentWritingRequest](avplannedvideosegmentwritingrequest.md) — AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression. _(beta)_
