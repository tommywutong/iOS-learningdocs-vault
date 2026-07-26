---
title: 'initWithVideoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetvideotrackplan/initwithvideocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvideotrackplan/initwithvideocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvideotrackplan/initwithvideocodectype%3Aencoderspecification%3Amediatype%3Asegmentconfigurations%3Aassemblytrackid%3A.json'
content_hash: 'sha256:f134e50db67f5719'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVideoTrackPlan](../avassetvideotrackplan.md)

# initWithVideoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:

<sub>Instance Method</sub>

Returns an instance of AVAssetVideoTrackPlan

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithVideoCodecType:(AVVideoCodecType) videoCodecType encoderSpecification:(NSDictionary *) encoderSpecification mediaType:(AVMediaType) mediaType segmentConfigurations:(NSArray<AVPlannedSegmentConfiguration *> *) segmentConfigurations assemblyTrackID:(CMPersistentTrackID) trackID;
```

## Parameters

- `videoCodecType` — Video codec type of the track

- `encoderSpecification` — The encoder specification the client will use to write planned segments of this track

- `mediaType` — Media type of the track. Only AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture are supported.

- `segmentConfigurations` — Segment configurations of the track

- `trackID` — The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.

## Discussion

This initializer throws NSInvalidArgumentException in the following cases.

1. mediaType is not supported. Supported media types are AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture
2. The encoder specified by videoCodecType and encoderSpecification does not support video encoding in segments
