---
title: AVPlannedVideoSegmentWritingRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplannedvideosegmentwritingrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedvideosegmentwritingrequest.json'
content_hash: 'sha256:d64b5a45f835b35a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlannedVideoSegmentWritingRequest

<sub>Class</sub>

AVPlannedVideoSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental video track segment with compression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlannedVideoSegmentWritingRequest
```

## Overview

The client should respond to this request by writing the specified time range of data to a movie file at the specified segmentFileOutputURL, with start PTS zero. The client’s writing work may be completed asynchronously. If it completes successfully, it must call the `-finish` method on the request object. If writing the segment fails, it must call the `-finishWithError:` method on the request object.

## Relationships

- **Inherits From**: [AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the request

- [frameCount](avplannedvideosegmentwritingrequest/framecount.md) — The number of frames in this planned video segment. This is provided for convenience, and is the same value that was configured for the segment in AVPlannedVideoSegmentConfiguration. _(beta)_

### Creating resumable compression sessions

- [createResumableCompressionSession(width:height:codecType:encoderSpecification:sourceImageBufferAttributes:outputHandler:)](<avplannedvideosegmentwritingrequest/createresumablecompressionsession(width_height_codectype_encoderspecification_sourceimagebufferattributes_outputhandler_).md>) — Helper function to create a VTCompressionSession that restores the video encoder state persisted at the end of the previous segment.

### Creating resumable writer inputs

- [makeResumableWriterInput(for:outputSettings:sourceFormatHint:)](<avplannedvideosegmentwritingrequest/makeresumablewriterinput(for_outputsettings_sourceformathint_).md>) — Helper function that returns a minimally configured AVAssetWriterInput object for writing the current segment.

## See Also

### Planned export

- [AVAssetWritingPlanner](avassetwritingplanner.md) — AVAssetWritingPlanner orchestrates incremental writing of media files. _(beta)_
- [AVAssetWritingPlannerProgress](avassetwritingplannerprogress.md) — AVAssetWritingPlannerProgress tracks the progress of incremental writing for each track in an AVAssetWritingPlanner session. _(beta)_
- [AVAssetTrackPlan](avassettrackplan.md) — AVAssetTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session. _(beta)_
- [AVAssetVideoTrackPlan](avassetvideotrackplan.md) — AVAssetVideoTrackPlan holds information about a track and how it should be segmented and executed in an incremental writing session. _(beta)_
- [AVPlannedSegmentConfiguration](avplannedsegmentconfiguration.md) — AVPlannedSegmentConfiguration describes the requirements for a planned segment in an incremental writing session executed by the AVAssetWritingPlanner. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type. _(beta)_
- [AVPlannedVideoSegmentConfiguration](avplannedvideosegmentconfiguration.md) — AVPlannedVideoSegmentConfiguration describes the requirements for a planned video segment in an incremental writing session executed by the AVAssetWritingPlanner. _(beta)_
- [AVPlannedSegmentWritingRequest](avplannedsegmentwritingrequest.md) — AVPlannedSegmentWritingRequest encompasses a request from the AVAssetWritingPlanner to the client code to write one incremental track segment. _(beta)_
