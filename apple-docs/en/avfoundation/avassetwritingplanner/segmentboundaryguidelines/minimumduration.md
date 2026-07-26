---
title: minimumDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentboundaryguidelines/minimumduration.json'
content_hash: 'sha256:0af6f1a3fd15afa6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWritingPlanner](../../avassetwritingplanner.md) · [SegmentBoundaryGuidelines](../segmentboundaryguidelines.md)

# minimumDuration

<sub>Instance Property</sub>

The minimum duration of each incremental segment. kCMTimeZero means there is no minimum segment duration requirement. kCMTimePositiveInfinity means that incremental segmentation is not supported for this codecType.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minimumDuration: CMTime
```
