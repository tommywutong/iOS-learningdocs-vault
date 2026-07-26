---
title: 'AVAssetWritingPlanner.SegmentResult.successWithState(_:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplanner/segmentresult/successwithstate(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/segmentresult/successwithstate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplanner/segmentresult/successwithstate%28_%3A%29.json'
content_hash: 'sha256:5ce82ffc30529bb9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWritingPlanner](../../avassetwritingplanner.md) · [SegmentResult](../segmentresult.md)

# AVAssetWritingPlanner.SegmentResult.successWithState(_:)

<sub>Case</sub>

Finish the segment successfully with custom client state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case successWithState(Data)
```

## Parameters

- `clientState` — Custom data to save for this segment. Commonly used to save algorithm state, progress information, or metadata needed for resumption.

## Discussion

Use this case to save custom state data that will be restored if the export session is interrupted and later resumed. The client state is available via [clientStateToRestore](../../avplannedsegmentwritingrequest/clientstatetorestore.md) when the segment is resumed. Only the last successful state data is persisted. Any previous state data will be overwritten.

## See Also

### Completion Options

- [AVAssetWritingPlanner.SegmentResult.success](success.md) — Finish the segment successfully without saving state.
- [AVAssetWritingPlanner.SegmentResult.cancelled](cancelled.md) — Cancel the current segment while allowing future resumption.
