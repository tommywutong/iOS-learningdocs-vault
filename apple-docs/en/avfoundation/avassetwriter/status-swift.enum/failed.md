---
title: AVAssetWriter.Status.failed
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/status-swift.enum/failed
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.enum/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/status-swift.enum/failed.json'
content_hash: 'sha256:c280221b8556bd9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriter](../../avassetwriter.md) · [Status](../status-swift.enum.md)

# AVAssetWriter.Status.failed

<sub>Case</sub>

The asset writer fails to write the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case failed
```

## Discussion

Query the [error](../error.md) property value to determine the cause of the failure.

## See Also

### Status values

- [AVAssetWriterStatusUnknown](unknown.md) — The asset writer’s status isn’t known.
- [AVAssetWriterStatusWriting](writing.md) — The asset writer is writing.
- [AVAssetWriterStatusCompleted](completed.md) — The asset writer finishes writing successfully.
- [AVAssetWriterStatusCancelled](cancelled.md) — The asset writer canceled the writing operation.
