---
title: 'segmentBoundaryRecommendations(forVideoTrack:minimumSegmentDuration:minimumSegmentFrameCount:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/segmentboundaryrecommendations(forvideotrack:minimumsegmentduration:minimumsegmentframecount:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryrecommendations(forvideotrack:minimumsegmentduration:minimumsegmentframecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentboundaryrecommendations%28forvideotrack%3Aminimumsegmentduration%3Aminimumsegmentframecount%3A%29.json'
content_hash: 'sha256:6d9e8fd08cb958d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# segmentBoundaryRecommendations(forVideoTrack:minimumSegmentDuration:minimumSegmentFrameCount:)

<sub>Type Method</sub>

Returns segment boundary recommendations for a given source video asset track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func segmentBoundaryRecommendations(forVideoTrack videoAssetTrack: AVAssetTrack, minimumSegmentDuration: CMTime, minimumSegmentFrameCount: Int) -> [AVPlannedVideoSegmentConfiguration]
```

## Parameters

- `videoAssetTrack` — The source video AVAssetTrack to be analyzed.

- `minimumSegmentDuration` — The client selected minimum duration for the segments.

- `minimumSegmentFrameCount` — The minimum number of source frames in a segment.

## Return Value

Array of AVPlannedVideoSegmentConfiguration objects, each element specifying the configuration of a planned video segment, ordered in output PTS order

## Discussion

This is a convenience method that can help clients to pick optimal segmentation boundaries for a given source video AVAssetTrack based on the structure of the track and the minimumSegmentDuration and minimumSegmentFrameCount values provided.

The client needs to ensure that the minimumSegmentDuration is greater than or equal to the segment boundary guidelines for the codec type. The client should also ensure that minimumSegmentFrameCount also exceeds the segment boundary guidelines.

The segments returned will satisfy both the minimumSegmentDuration and minimumSegmentFrameCount requirements. The only exception is the very last segment, which may be shorter.

The returned array will ensure that segment boundaries occur on sample boundaries.

Clients can use these results to fill in the AVPlannedVideoSegmentConfiguration for this asset track, if the output maintains the source timing. If the output timing differs from the source, then the returned AVPlannedVideoSegmentConfiguration array’s results need to be modified accordingly by the client.

This method throws NSInvalidArgumentException if minimumSegmentDuration is not numeric or is less than or equal to zero, or if minimumSegmentFrameCount is less than or equal to 0.

## See Also

### Getting segment boundary guidance

- [segmentBoundaryGuidelinesForVideo(codecType:encoderSpecification:)](<segmentboundaryguidelinesforvideo(codectype_encoderspecification_).md>) — Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.
