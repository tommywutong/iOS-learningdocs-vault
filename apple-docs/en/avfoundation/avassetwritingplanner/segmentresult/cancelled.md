---
title: AVAssetWritingPlanner.SegmentResult.cancelled
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplanner/segmentresult/cancelled
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult/cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentresult/cancelled.json'
content_hash: 'sha256:0dced1c81f6c1559'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWritingPlanner](../../avassetwritingplanner.md) · [SegmentResult](../segmentresult.md)

# AVAssetWritingPlanner.SegmentResult.cancelled

<sub>Case</sub>

Cancel the current segment while allowing future resumption.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case cancelled
```

## Discussion

Use this case when the segment should be canceled (for example, due to background task expiration) but you expect to resume the export later. This preserves the ability to restart from this segment in a future export session.

This is equivalent to calling `cancel()` on the segment request.

## Use Cases

- Background task expiration handler called
- System resources unavailable
- User-initiated pause operation

## See Also

### Completion Options

- [AVAssetWritingPlanner.SegmentResult.success](success.md) — Finish the segment successfully without saving state.
- [AVAssetWritingPlanner.SegmentResult.successWithState(_:)](<successwithstate(__).md>) — Finish the segment successfully with custom client state.
