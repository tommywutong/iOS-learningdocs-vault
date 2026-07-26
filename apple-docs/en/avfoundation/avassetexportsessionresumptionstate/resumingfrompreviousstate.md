---
title: resumingFromPreviousState
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsessionresumptionstate/resumingfrompreviousstate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate/resumingfrompreviousstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsessionresumptionstate/resumingfrompreviousstate.json'
content_hash: 'sha256:850f49ec2a26e826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSessionResumptionState](../avassetexportsessionresumptionstate.md)

# resumingFromPreviousState

<sub>Instance Property</sub>

Reports whether or not a resuming export is continuing from a previous state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, getter=isResumingFromPreviousState) BOOL resumingFromPreviousState;
```

## Discussion

This indicates whether or not the export is resuming (YES) or starting from the beginning (NO). Valid only if resumptionConfigured is YES.

## See Also

### Inspecting the resumption state

- [resumptionConfigured](resumptionconfigured.md) — Reports whether or not the export session has been successfully configure as resumable. _(beta)_
- [configurationFailureReason](configurationfailurereason.md) — Provides details on why the session was not able to be configured as resumable. _(beta)_
