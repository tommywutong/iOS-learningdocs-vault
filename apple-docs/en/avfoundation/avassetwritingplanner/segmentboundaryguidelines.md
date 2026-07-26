---
title: AVAssetWritingPlanner.SegmentBoundaryGuidelines
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines.json'
content_hash: 'sha256:c5dfe2a8503efd43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# AVAssetWritingPlanner.SegmentBoundaryGuidelines

<sub>Structure</sub>

AVPlannedVideoSegmentBoundaryGuidelines provides guidance on determining planned segment boundaries for a video track in an incremental writing session executed by the AVAssetWritingPlanner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct SegmentBoundaryGuidelines
```

## Overview

The properties provide guidance on determining segment boundaries for a video track in an incremental writing session. All conditions should be supported for best results. The client should choose frame count and minimum duration that meet the minimum requirement. However, the client should also consider the balance between overhead caused by completing and saving states for small segments, and the cost of having to redo a large segment if the incremental session stopped in the middle of a segment due to errors or crashes. For example, use 1 minute segments for 4K60fps video.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Sendable](../../swift/sendable.md)

## Topics

### Initializers

- [init()](<segmentboundaryguidelines/init().md>) _(beta)_
- [init(minimumFrameCount:minimumDuration:)](<segmentboundaryguidelines/init(minimumframecount_minimumduration_).md>) _(beta)_

### Instance Properties

- [minimumDuration](segmentboundaryguidelines/minimumduration.md) — The minimum duration of each incremental segment. kCMTimeZero means there is no minimum segment duration requirement. kCMTimePositiveInfinity means that incremental segmentation is not supported for this codecType. _(beta)_
- [minimumFrameCount](segmentboundaryguidelines/minimumframecount.md) — The minimum number of frames in each incremental segment. 0 means that incremental segmentation is not supported for this codecType. 1 means there is no frame count restriction for incremental encoding for this codecType. Using 1 for segment frame count is not recommended because of the performance overhead, so the client should choose a value that represents a reasonable amount of work. _(beta)_
