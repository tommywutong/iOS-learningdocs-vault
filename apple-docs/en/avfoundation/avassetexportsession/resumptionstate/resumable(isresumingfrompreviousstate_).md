---
title: 'AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/resumptionstate/resumable(isresumingfrompreviousstate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate/resumable(isresumingfrompreviousstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/resumptionstate/resumable%28isresumingfrompreviousstate%3A%29.json'
content_hash: 'sha256:332d73055b781096'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetExportSession](../../avassetexportsession.md) · [ResumptionState](../resumptionstate.md)

# AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)

<sub>Case</sub>

The export session is successfully configured for resumption.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case resumable(isResumingFromPreviousState: Bool)
```

## Parameters

- `isResumingFromPreviousState` — `true` if the export will continue from a previously interrupted state; `false` if starting/restarting from beginning.

## See Also

### Resumption states

- [AVAssetExportSession.ResumptionState.notResumable(failureReason:)](<notresumable(failurereason_).md>) — The export session could not be configured for resumption.
