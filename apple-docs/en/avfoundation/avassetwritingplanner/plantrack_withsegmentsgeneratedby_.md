---
title: 'planTrack:withSegmentsGeneratedBy:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/plantrack:withsegmentsgeneratedby:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/plantrack:withsegmentsgeneratedby:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/plantrack%3Awithsegmentsgeneratedby%3A.json'
content_hash: 'sha256:16c7834121f922f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# planTrack:withSegmentsGeneratedBy:

<sub>Instance Method</sub>

Adds an AVAssetTrackPlan to this AVAssetWritingPlanner, with a block to be called by the planner to generate each segment of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) planTrack:(AVAssetTrackPlan *) trackPlan withSegmentsGeneratedBy:(void (^)(AVPlannedSegmentWritingRequest *segmentWriteRequest)) writingSegmentCallbackBlock;
```

## Parameters

- `trackPlan` — The track plan contains information about the track and boundaries of all the segments.

- `writingSegmentCallbackBlock` — A block to be called by the AVAssetWritingPlanner on each incremental segment for this track to write the segment to an intermediate file, according to the specifications in the “segmentWriteRequest” object passed to the block.

## Discussion

This method throws NSInternalInconsistencyException if a trackPlan with the same assemblyTrackID already exists in the planner, or if called after executePlanWithCompletionHandler: has been invoked.
