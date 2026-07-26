---
title: 'segmentBoundaryGuidelinesForVideo(codecType:encoderSpecification:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideo(codectype:encoderspecification:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideo(codectype:encoderspecification:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelinesforvideo%28codectype%3Aencoderspecification%3A%29.json'
content_hash: 'sha256:eafb2282a6bd1110'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# segmentBoundaryGuidelinesForVideo(codecType:encoderSpecification:)

<sub>Type Method</sub>

Returns segment boundary guidelines that help clients determine how to segment compression video tracks with best results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static func segmentBoundaryGuidelinesForVideo(codecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]) -> AVAssetWritingPlanner.SegmentBoundaryGuidelines
```

## Parameters

- `codecType` — The output video codec type for the video track.

- `encoderSpecification` — A dictionary of kVTVideoEncoderSpecification_* keys describing the video encoder. This is the same specification the client uses to compress the video track.

## Return Value

An AVAssetWritingPlanner.SegmentBoundaryGuidelines with the minimum frame count and duration for the given codec and encoder.

## Discussion

The encoderSpecification parameter here is the same encoder specification the client uses to compress the video track.

## See Also

### Getting segment boundary guidance

- [+ segmentBoundaryRecommendationsForVideoAVAssetTrack:minimumSegmentDuration:minimumSegmentFrameCount:](<segmentboundaryrecommendations(forvideotrack_minimumsegmentduration_minimumsegmentframecount_).md>) — Returns segment boundary recommendations for a given source video asset track. _(beta)_
