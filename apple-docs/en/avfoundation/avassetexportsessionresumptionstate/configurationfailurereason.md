---
title: configurationFailureReason
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsessionresumptionstate/configurationfailurereason
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate/configurationfailurereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsessionresumptionstate/configurationfailurereason.json'
content_hash: 'sha256:c8a34a3c51a8e43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSessionResumptionState](../avassetexportsessionresumptionstate.md)

# configurationFailureReason

<sub>Instance Property</sub>

Provides details on why the session was not able to be configured as resumable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, nullable) AVAssetExportSessionResumptionFailureReason configurationFailureReason;
```

## Discussion

Reasons for failure include incompatible session settings and incompatible directoryForTemporaryFiles contents. Valid only if resumptionConfigured is NO.

## See Also

### Inspecting the resumption state

- [resumptionConfigured](resumptionconfigured.md) — Reports whether or not the export session has been successfully configure as resumable. _(beta)_
- [resumingFromPreviousState](resumingfrompreviousstate.md) — Reports whether or not a resuming export is continuing from a previous state. _(beta)_
