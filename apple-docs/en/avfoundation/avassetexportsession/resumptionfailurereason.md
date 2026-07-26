---
title: AVAssetExportSession.ResumptionFailureReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/resumptionfailurereason
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/resumptionfailurereason.json'
content_hash: 'sha256:ab89c59685a1ff93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# AVAssetExportSession.ResumptionFailureReason

<sub>Structure</sub>

An enum that identifies various reasons why resumable export configuration has failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct ResumptionFailureReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a failure reason

- [init(_:)](<resumptionfailurereason/init(__).md>) _(beta)_
- [init(rawValue:)](<resumptionfailurereason/init(rawvalue_).md>) _(beta)_

### Failure reasons

- [AVAssetExportSessionResumptionFailureReasonIncompatiblePreset](resumptionfailurereason/incompatiblepreset.md) _(beta)_
- [AVAssetExportSessionResumptionFailureReasonIncompatibleSessionSettings](resumptionfailurereason/incompatiblesessionsettings.md) _(beta)_
- [AVAssetExportSessionResumptionFailureReasonIncompatibleTemporaryDirectoryContents](resumptionfailurereason/incompatibletemporarydirectorycontents.md) _(beta)_
- [AVAssetExportSessionResumptionFailureReasonTemporaryDirectoryDoesNotExist](resumptionfailurereason/temporarydirectorydoesnotexist.md) _(beta)_
- [AVAssetExportSessionResumptionFailureReasonUnsupportedForPresetOnPlatform](resumptionfailurereason/unsupportedforpresetonplatform.md) _(beta)_

## See Also

### Configuring resumable export

- [configureForResumableExport()](<configureforresumableexport().md>) — Configures the export session for resumable export.
- [ResumptionState](resumptionstate.md) — Represents the resumption state of the export session.
