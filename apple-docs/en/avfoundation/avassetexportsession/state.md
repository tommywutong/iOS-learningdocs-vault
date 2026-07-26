---
title: AVAssetExportSession.State
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/state
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/state.json'
content_hash: 'sha256:4904b1f70dea2002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# AVAssetExportSession.State

<sub>Enumeration</sub>

Constants that indicate the state of an export operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [AVAssetExportSession.State.pending](state/pending.md) — An export operation is currently pending.
- [AVAssetExportSession.State.exporting(progress:)](<state/exporting(progress_).md>) — An export session is currently exporting media.
- [AVAssetExportSession.State.waiting](state/waiting.md) — An export session is currently waiting.

## See Also

### Monitoring export progress

- [states(updateInterval:)](<states(updateinterval_).md>) — Monitors the progress state of an export operation.
- [Status](status-swift.enum.md) — Values that indicate the state of an export session.
