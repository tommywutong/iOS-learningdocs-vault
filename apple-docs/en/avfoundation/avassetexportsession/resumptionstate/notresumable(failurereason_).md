---
title: 'AVAssetExportSession.ResumptionState.notResumable(failureReason:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/resumptionstate/notresumable(failurereason:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate/notresumable(failurereason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/resumptionstate/notresumable%28failurereason%3A%29.json'
content_hash: 'sha256:306f0fb81593b753'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetExportSession](../../avassetexportsession.md) · [ResumptionState](../resumptionstate.md)

# AVAssetExportSession.ResumptionState.notResumable(failureReason:)

<sub>Case</sub>

The export session could not be configured for resumption.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case notResumable(failureReason: AVAssetExportSession.ResumptionFailureReason)
```

## Parameters

- `failureReason` — The reason why resumption was not successfully configured.

## See Also

### Resumption states

- [AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)](<resumable(isresumingfrompreviousstate_).md>) — The export session is successfully configured for resumption.
