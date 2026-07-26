---
title: 'segmentBoundaryGuidelinesForVideoCodecType:videoEncoderSpecification:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideocodectype:videoencoderspecification:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideocodectype:videoencoderspecification:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideocodectype%3Avideoencoderspecification%3A.json'
content_hash: 'sha256:c18f093fe738d1e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# segmentBoundaryGuidelinesForVideoCodecType:videoEncoderSpecification:

<sub>Type Method</sub>

Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (AVPlannedVideoSegmentBoundaryGuidelines) segmentBoundaryGuidelinesForVideoCodecType:(AVVideoCodecType) videoCodecType videoEncoderSpecification:(NSDictionary *) videoEncoderSpecification;
```

## Parameters

- `videoCodecType` — The output videoCodecType for the video track.

- `videoEncoderSpecification` — The video encoder specification includes options for choosing a specific video encoder. This is a dictionary containing kVTVideoEncoderSpecification_* keys specified in the VideoToolbox framework.

## Return Value

An AVPlannedVideoSegmentBoundaryGuidelines.

## Discussion

The videoEncoderSpecification parameter here is the same encoder specification the client uses to compress the video track.

## See Also

### Getting segment boundary guidance

- [+ segmentBoundaryRecommendationsForVideoAVAssetTrack:minimumSegmentDuration:minimumSegmentFrameCount:](<segmentboundaryrecommendations(forvideotrack_minimumsegmentduration_minimumsegmentframecount_).md>) — Returns segment boundary recommendations for a given source video asset track. _(beta)_
