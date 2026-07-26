---
title: AVAssetExportSession.ResumptionState
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/resumptionstate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/resumptionstate.json'
content_hash: 'sha256:ec37a12ed0cecd7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# AVAssetExportSession.ResumptionState

<sub>Enumeration</sub>

Represents the resumption state of the export session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum ResumptionState
```

## Overview

After calling `configureForResumableExport()`, this returned state details whether the export is successfully configured as resumable or not, and provides additional relevant information.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Resumption states

- [AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)](<resumptionstate/resumable(isresumingfrompreviousstate_).md>) — The export session is successfully configured for resumption.
- [AVAssetExportSession.ResumptionState.notResumable(failureReason:)](<resumptionstate/notresumable(failurereason_).md>) — The export session could not be configured for resumption.

## See Also

### Configuring resumable export

- [configureForResumableExport()](<configureforresumableexport().md>) — Configures the export session for resumable export.
- [ResumptionFailureReason](resumptionfailurereason.md) — An enum that identifies various reasons why resumable export configuration has failed. _(beta)_
