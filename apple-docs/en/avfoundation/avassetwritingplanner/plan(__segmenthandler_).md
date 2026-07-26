---
title: 'plan(_:segmentHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/plan(_:segmenthandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/plan(_:segmenthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/plan%28_%3Asegmenthandler%3A%29.json'
content_hash: 'sha256:0e3b6719bbf98cae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# plan(_:segmentHandler:)

<sub>Instance Method</sub>

Adds a track plan with manual segment completion control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func plan(_ trackPlan: AVAssetTrackPlan, segmentHandler: @escaping @Sendable (AVPlannedSegmentWritingRequest) async throws -> AVAssetWritingPlanner.SegmentResult)
```

## Parameters

- `trackPlan` — The track plan contains information about the track and boundaries of all the segments.

- `segmentHandler` — Handler that returns a [SegmentResult](segmentresult.md) for manual control.

## Discussion

This variant provides fine-grained control over segment completion, allowing you to return a [SegmentResult](segmentresult.md) that explicitly controls how the segment completes.

## Topics

### See Also

- [SegmentResult](segmentresult.md) — Result type for manual segment completion control.
