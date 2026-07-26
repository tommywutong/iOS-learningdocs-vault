---
title: resumptionConfigured
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsessionresumptionstate/resumptionconfigured
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate/resumptionconfigured'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsessionresumptionstate/resumptionconfigured.json'
content_hash: 'sha256:06c770a324bd9658'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSessionResumptionState](../avassetexportsessionresumptionstate.md)

# resumptionConfigured

<sub>Instance Property</sub>

Reports whether or not the export session has been successfully configure as resumable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, getter=isResumptionConfigured) BOOL resumptionConfigured;
```

## Discussion

If YES, the export session in configured as resumable. If NO, the export session will remain as non-resumable (default). exportAsynchronouslyWithCompletionHandler may still be called if this returns as NO.

## See Also

### Inspecting the resumption state

- [resumingFromPreviousState](resumingfrompreviousstate.md) — Reports whether or not a resuming export is continuing from a previous state. _(beta)_
- [configurationFailureReason](configurationfailurereason.md) — Provides details on why the session was not able to be configured as resumable. _(beta)_
