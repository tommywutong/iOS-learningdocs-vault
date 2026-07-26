---
title: 'init(mediaType:segmentConfigurations:assemblyTrackID:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassettrackplan/init(mediatype:segmentconfigurations:assemblytrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrackplan/init(mediatype:segmentconfigurations:assemblytrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrackplan/init%28mediatype%3Asegmentconfigurations%3Aassemblytrackid%3A%29.json'
content_hash: 'sha256:ea45e0273ad5d83f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrackPlan](../avassettrackplan.md)

# init(mediaType:segmentConfigurations:assemblyTrackID:)

<sub>Initializer</sub>

Returns an instance of AVAssetTrackPlan

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mediaType: AVMediaType, segmentConfigurations: [AVPlannedSegmentConfiguration], assemblyTrackID trackID: CMPersistentTrackID)
```

## Parameters

- `mediaType` — Media type of the track

- `segmentConfigurations` — Segment configurations of the track

- `trackID` — The trackID that identifies this track in the assemblyComposition the planner passes to the completion handler of the incremental writing session.

## Discussion

This initializer throws NSInvalidArgumentException if trackID is kCMPersistentTrackID_Invalid.
