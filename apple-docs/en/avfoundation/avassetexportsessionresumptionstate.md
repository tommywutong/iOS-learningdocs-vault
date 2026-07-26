---
title: AVAssetExportSessionResumptionState
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsessionresumptionstate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsessionresumptionstate.json'
content_hash: 'sha256:1f206b221683de08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetExportSessionResumptionState

<sub>Class</sub>

AVAssetExportSessionResumptionState details the current resumption state of the export session. A resumable export session is configured via configureForResumableExportWithCompletionHandler:.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface AVAssetExportSessionResumptionState : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Inspecting the resumption state

- [resumptionConfigured](avassetexportsessionresumptionstate/resumptionconfigured.md) — Reports whether or not the export session has been successfully configure as resumable. _(beta)_
- [resumingFromPreviousState](avassetexportsessionresumptionstate/resumingfrompreviousstate.md) — Reports whether or not a resuming export is continuing from a previous state. _(beta)_
- [configurationFailureReason](avassetexportsessionresumptionstate/configurationfailurereason.md) — Provides details on why the session was not able to be configured as resumable. _(beta)_

## See Also

### Configuring resumable export

- [configureForResumableExportWithCompletionHandler:](avassetexportsession/configureforresumableexportwithcompletionhandler_.md) — Attempt to configure the exportSession into resumption mode. _(beta)_
- [ResumptionFailureReason](avassetexportsession/resumptionfailurereason.md) — An enum that identifies various reasons why resumable export configuration has failed. _(beta)_
