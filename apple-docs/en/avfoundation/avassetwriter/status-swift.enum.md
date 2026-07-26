---
title: AVAssetWriter.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/status-swift.enum.json'
content_hash: 'sha256:fa7e1ce50aaed5ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# AVAssetWriter.Status

<sub>Enumeration</sub>

Values that indicate the state of an asset writer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVAssetWriterStatusUnknown](status-swift.enum/unknown.md) — The asset writer’s status isn’t known.
- [AVAssetWriterStatusWriting](status-swift.enum/writing.md) — The asset writer is writing.
- [AVAssetWriterStatusCompleted](status-swift.enum/completed.md) — The asset writer finishes writing successfully.
- [AVAssetWriterStatusFailed](status-swift.enum/failed.md) — The asset writer fails to write the output file.
- [AVAssetWriterStatusCancelled](status-swift.enum/cancelled.md) — The asset writer canceled the writing operation.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Inspecting writing status

- [status](status-swift.property.md) — The status of writing samples to the output file.
- [error](error.md) — An error object that describes an asset-writing failure.
