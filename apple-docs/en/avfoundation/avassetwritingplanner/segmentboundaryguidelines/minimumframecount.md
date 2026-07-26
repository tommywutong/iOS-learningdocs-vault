---
title: minimumFrameCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumframecount
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumframecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumframecount.json'
content_hash: 'sha256:e4beebafaa05a1a6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWritingPlanner](../../avassetwritingplanner.md) · [SegmentBoundaryGuidelines](../segmentboundaryguidelines.md)

# minimumFrameCount

<sub>Instance Property</sub>

The minimum number of frames in each incremental segment. 0 means that incremental segmentation is not supported for this codecType. 1 means there is no frame count restriction for incremental encoding for this codecType. Using 1 for segment frame count is not recommended because of the performance overhead, so the client should choose a value that represents a reasonable amount of work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minimumFrameCount: Int
```
