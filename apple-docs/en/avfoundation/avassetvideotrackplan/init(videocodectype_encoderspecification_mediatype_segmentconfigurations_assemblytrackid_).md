---
title: 'init(videoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetvideotrackplan/init(videocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvideotrackplan/init(videocodectype:encoderspecification:mediatype:segmentconfigurations:assemblytrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvideotrackplan/init%28videocodectype%3Aencoderspecification%3Amediatype%3Asegmentconfigurations%3Aassemblytrackid%3A%29.json'
content_hash: 'sha256:5c2b2edbaf36ea2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetVideoTrackPlan](../avassetvideotrackplan.md)

# init(videoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:)

<sub>Initializer</sub>

Creates an instance of AVAssetVideoTrackPlan.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(videoCodecType: AVVideoCodecType, encoderSpecification: [String : any Sendable]? = nil, mediaType: AVMediaType, segmentConfigurations: [AVPlannedVideoSegmentConfiguration], assemblyTrackID: CMPersistentTrackID)
```

## Parameters

- `videoCodecType` — Video codec type of the track.

- `encoderSpecification` — A dictionary describing the characteristics of a video encoder to use. Pass nil to let the system choose an encoder. If the client provides a specification, it should omit the following keys: kVTCompressionPropertyKey_SourceFrameCount, kVTCompressionPropertyKey_MoreFramesBeforeStart, and kVTCompressionPropertyKey_MoreFramesAfterEnd, since such keys will be overwritten by the underlying implementation.

- `mediaType` — Media type of the track. Only AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture are supported.

- `segmentConfigurations` — Segment configurations of the track.

- `assemblyTrackID` — The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.

## Discussion

This initializer throws NSInvalidArgumentException in the following cases:

1. mediaType is not supported. Supported media types are AVMediaTypeVideo and AVMediaTypeAuxiliaryPicture
2. The encoder specified by videoCodecType and encoderSpecification does not support video encoding in segments
