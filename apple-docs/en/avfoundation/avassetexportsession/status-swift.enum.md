---
title: AVAssetExportSession.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/status-swift.enum.json'
content_hash: 'sha256:6c44b2701a0e9cc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# AVAssetExportSession.Status

<sub>Enumeration</sub>

Values that indicate the state of an export session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVAssetExportSessionStatusUnknown](status-swift.enum/unknown.md) — The session status is unknown.
- [AVAssetExportSessionStatusWaiting](status-swift.enum/waiting.md) — The session is waiting to export more data.
- [AVAssetExportSessionStatusExporting](status-swift.enum/exporting.md) — The export is in progress.
- [AVAssetExportSessionStatusCompleted](status-swift.enum/completed.md) — The export completes successfully.
- [AVAssetExportSessionStatusFailed](status-swift.enum/failed.md) — The export fails.
- [AVAssetExportSessionStatusCancelled](status-swift.enum/cancelled.md) — You canceled the export.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Monitoring export progress

- [states(updateInterval:)](<states(updateinterval_).md>) — Monitors the progress state of an export operation.
- [State](state.md) — Constants that indicate the state of an export operation.
