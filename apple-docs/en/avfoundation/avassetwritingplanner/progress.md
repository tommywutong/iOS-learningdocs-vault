---
title: progress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/progress
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/progress.json'
content_hash: 'sha256:66422f1fd64418ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# progress

<sub>Instance Property</sub>

The current progress of the AVAssetWritingPlanner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var progress: AVAssetWritingPlannerProgress { get }
```

## Discussion

Returns an AVAssetWritingPlannerProgress object that can be queried for per-track and overall progress information.
