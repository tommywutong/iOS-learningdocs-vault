---
title: AVAssetWritingPlanner.SegmentResult.success
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/segmentresult/success
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult/success'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentresult/success.json'
content_hash: 'sha256:cd542496a621848d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWritingPlanner](../../avassetwritingplanner.md) · [SegmentResult](../segmentresult.md)

# AVAssetWritingPlanner.SegmentResult.success

<sub>Case</sub>

Finish the segment successfully without saving state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case success
```

## Discussion

Use this case when the segment completed successfully and you don’t need to save any custom state for resumption.

This is equivalent to calling `finish()` on the segment request.

## See Also

### Completion Options

- [AVAssetWritingPlanner.SegmentResult.successWithState(_:)](<successwithstate(__).md>) — Finish the segment successfully with custom client state.
- [AVAssetWritingPlanner.SegmentResult.cancelled](cancelled.md) — Cancel the current segment while allowing future resumption.
