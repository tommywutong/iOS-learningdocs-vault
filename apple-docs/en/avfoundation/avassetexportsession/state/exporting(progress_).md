---
title: 'AVAssetExportSession.State.exporting(progress:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/state/exporting(progress:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/state/exporting(progress:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/state/exporting%28progress%3A%29.json'
content_hash: 'sha256:f366f843cc45f506'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetExportSession](../../avassetexportsession.md) · [State](../state.md)

# AVAssetExportSession.State.exporting(progress:)

<sub>Case</sub>

An export session is currently exporting media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case exporting(progress: Progress)
```

## Parameters

- `progress` — A value that indicates the completion percentage of the export operation.

## See Also

### States

- [AVAssetExportSession.State.pending](pending.md) — An export operation is currently pending.
- [AVAssetExportSession.State.waiting](waiting.md) — An export session is currently waiting.
