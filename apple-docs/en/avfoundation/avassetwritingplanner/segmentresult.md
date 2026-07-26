---
title: AVAssetWritingPlanner.SegmentResult
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/segmentresult
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentresult.json'
content_hash: 'sha256:fb98c10e6f719fc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlanner](../avassetwritingplanner.md)

# AVAssetWritingPlanner.SegmentResult

<sub>Enumeration</sub>

Result type for manual segment completion control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum SegmentResult
```

## Overview

Return this type from the segment handler to explicitly control how each segment completes, including saving custom client state for resumable exports or canceling segments.

## Topics

### Completion Options

- [AVAssetWritingPlanner.SegmentResult.success](segmentresult/success.md) — Finish the segment successfully without saving state.
- [AVAssetWritingPlanner.SegmentResult.successWithState(_:)](<segmentresult/successwithstate(__).md>) — Finish the segment successfully with custom client state.
- [AVAssetWritingPlanner.SegmentResult.cancelled](segmentresult/cancelled.md) — Cancel the current segment while allowing future resumption.
